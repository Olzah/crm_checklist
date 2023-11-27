from odoo import api, fields, models, Command
import logging

logger = logging.getLogger(__name__)
class Lead(models.Model):
    _inherit="crm.lead"

    tasks_list_ids = fields.One2many('task.checklist.line', 'task_list_id', string='Checklist Tasks')
    progress = fields.Integer(string="Progress", compute="_compute_progress")
    # template_ids = fields.One2many('crm.checklist.template', 'temp_id', string='Checklist Tasks')
    temp_id = fields.Many2one('crm.checklist.template', string='Checklist Templates', index=True, ondelete='cascade')

    @api.depends("tasks_list_ids.is_done")
    def _compute_progress(self):
        all_task_list = len(self.tasks_list_ids)
        if all_task_list > 0:
            done_state = len(self.tasks_list_ids.filtered(lambda l: l.is_done == True))
            self.progress += done_state/all_task_list*100
        else:
            self.progress = 0

    @api.onchange('temp_id')
    def _onchange_template(self):
        # template_elem = self.tasks_list_ids.filtered(lambda l: l.template_patent_id.id != False)
        # for el in template_elem:
        #     el.unlink()
        list_uses_templ_id = set([x.id for x in self.tasks_list_ids.template_patent_id])

        for temp_el in self.temp_id.template_ids:
            if self.temp_id.id not in list_uses_templ_id:
                self.tasks_list_ids |= self.tasks_list_ids.new(
                    dict(name=temp_el.name,
                         description=temp_el.description,
                         is_done=False,
                         task_list_id=self._origin.id,
                         template_patent_id=self.temp_id.id)
                )
