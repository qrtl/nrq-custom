# -*- coding: utf-8 -*-
# Copyright 2017-2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    approval = fields.Boolean(
        string="Approved", readonly=True, default=False, copy=False,
    )
    approval_user_id = fields.Many2one(
        "res.users", string="Approver", readonly=True, copy=False
    )
    self_approval_permission = fields.Boolean(
        string="Self-approval Permission", default=False,
    )
    approval_availability = fields.Boolean(
        string="Approval Availability", compute="_compute_approval_availability",
    )

    @api.multi
    def write(self, vals):
        if "state" in vals:
            for quote in self:
                if vals["state"] == "cancel":
                    vals["approval"] = False
                elif (quote.state == "draft" and quote.approval) or vals["state"] in [
                    "sale",
                    "done",
                ]:
                    vals["approval"] = True
                elif quote.state != "draft":
                    vals["approval"] = False
        if "approval" in vals:
            for quote in self:
                if quote.approval != vals["approval"]:
                    self.send_track_notification_email(
                        _("Approval"), str(quote.approval), str(vals["approval"])
                    )
        return super(SaleOrder, self).write(vals)

    @api.multi
    def action_approve(self):
        for quote in self:
            quote.approval = True
            quote.approval_user_id = quote.env.user.id

    @api.multi
    def action_cancel_approval(self):
        for quote in self:
            quote.approval = False
            quote.approval_user_id = False

    @api.multi
    def _compute_approval_availability(self):
        user = self.env.user
        for order in self:
            order.approval_availability = user.has_group(
                "sales_team.group_sale_manager"
            ) and (user != order.user_id or order.self_approval_permission)

    @api.multi
    def send_track_notification_email(self, field, old_value, new_value):
        self.ensure_one()
        email_act = self.action_track_notification_email_send(
            field, old_value, new_value
        )
        if email_act and email_act.get("context"):
            email_ctx = email_act["context"]
            self.with_context(email_ctx).message_post_with_template(
                email_ctx.get("default_template_id")
            )
        return True

    @api.multi
    def action_track_notification_email_send(self, field, old_value, new_value):
        self.ensure_one()
        ir_model_data = self.env["ir.model.data"]
        try:
            template_id = ir_model_data.get_object_reference(
                "sale_quotation_approval", "sale_order_track_notification"
            )[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference(
                "mail", "email_compose_message_wizard_form"
            )[1]
        except ValueError:
            compose_form_id = False
        ctx = dict()
        ctx.update(
            {
                "default_model": "sale.order",
                "default_res_id": self.ids[0],
                "default_use_template": bool(template_id),
                "default_template_id": template_id,
                "default_composition_mode": "comment",
                "user_name": self.env.user.name,
                "track_field": field,
                "old_value": old_value,
                "new_value": new_value,
            }
        )
        return {
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "mail.compose.message",
            "views": [(compose_form_id, "form")],
            "view_id": compose_form_id,
            "target": "new",
            "context": ctx,
        }
