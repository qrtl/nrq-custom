odoo.define('hr_weekly_timesheet_widget_adj.sheet', function (require) {
"use strict";

    var core = require('web.core');
    var form_common = require('web.form_common');

    core.form_custom_registry.get("weekly_timesheet").include({
        init_add_project: function() {
            if (this.dfm) {
                this.dfm.destroy();
            }

            var self = this;
            this.$(".oe_timesheet_weekly_add_row").show();
            this.dfm = new form_common.DefaultFieldManager(this);
            this.dfm.extend_field_desc({
                project: {
                    relation: "project.project",
                },
            });
            var FieldMany2One = core.form_widget_registry.get('many2one');
            this.project_m2o = new FieldMany2One(this.dfm, {
                attrs: {
                    name: "project",
                    type: "many2one",
                    domain: [
                        ['id', 'not in', _.pluck(this.projects, "project")],
                        // Add by QRTL
                        ['allow_timesheets', '=', true],
                    ],
                    modifiers: '{"required": true}',
                },
            });
            this.project_m2o.prependTo(this.$(".o_add_timesheet_line > div")).then(function() {
                self.project_m2o.$el.addClass('oe_edit_only');
            });
            this.$(".oe_timesheet_button_add").click(function() {
                var id = self.project_m2o.get_value();
                if (id === false) {
                    self.dfm.set({display_invalid_fields: true});
                    return;
                }

                var ops = self.generate_o2m_value();
                ops.push(_.extend({}, self.default_get, {
                    name: self.description_line,
                    unit_amount: 0,
                    date: time.date_to_str(self.dates[0]),
                    project_id: id,
                }));

                self.set({sheets: ops});
                self.destroy_content();
            });
        },
        
    });
});
