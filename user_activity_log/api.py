# # -*- coding: utf-8 -*-
# # Copyright 2020 Quartile Limited
# # License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api
from odoo.api import split_context

_logger = logging.getLogger(__name__)

call_kw_org = api.call_kw


def call_kw(model, name, args, kwargs):
    res = call_kw_org(model, name, args, kwargs)
    user = model.env.user
    if user.track_user_activity and 'user.activity.log' != model._name:
        method_args = args
        # Borrow the original logic to identify the ids and args
        # https://github.com/odoo/odoo/blob/e66e2e2fe4a7c748278c3bb71c2fe10ad36e1245/odoo/api.py#L668-L689
        method = getattr(type(model), name)
        if getattr(method, '_api', None) == 'model':
            recs = model
        else:
            ids, method_args = args[0], args[1:]
            recs = model.browse(ids)
        method_args = split_context(method, method_args, kwargs)
        if recs or method_args:
            model.env['user.activity.log'].create_activity_log(
                model, name, recs, method_args)
    return res


_logger.info('monkey patching api.call_kw')
api.call_kw = call_kw
