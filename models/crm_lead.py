from odoo import api, fields, models, Command
import logging

logger = logging.getLogger(__name__)
class Lead(models.Model):
    _inherit="crm.lead"

    tasks_list_ids = fields.One2many('task.checklist.line', 'task_list_id', string='Checklist Tasks')
    progress = fields.Integer(string="Progress", compute="_compute_progress")
    @api.depends("tasks_list_ids.state")
    def _compute_progress(self):
        all_task_list = len(self.tasks_list_ids)
        if all_task_list > 0:
            done_state = len(self.tasks_list_ids.filtered(lambda l: l.state == "done"))
            self.progress += done_state/all_task_list*100
        else:
            self.progress = 0