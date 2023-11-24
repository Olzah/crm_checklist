from odoo import api, fields, models, Command
import logging

logger = logging.getLogger(__name__)
class Lead(models.Model):
    _inherit="crm.lead"

    tasks_list_ids = fields.One2many('task.checklist.line', 'task_list_id', string='Checklist Tasks')
    progress = fields.Integer(string="Progress", compute="_compute_progress")
    # template_ids = fields.One2many('crm.checklist.template', 'temp_id', string='Checklist Tasks')
    temp_id = fields.Many2one('crm.checklist.template', string='Checklist Templates')

    @api.depends("tasks_list_ids.is_done")
    def _compute_progress(self):
        all_task_list = len(self.tasks_list_ids)
        if all_task_list > 0:
            done_state = len(self.tasks_list_ids.filtered(lambda l: l.is_done == True))
            self.progress += done_state/all_task_list*100
        else:
            self.progress = 0