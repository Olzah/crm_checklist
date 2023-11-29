from odoo import api, fields, models, Command
import logging

logger = logging.getLogger(__name__)
class Lead(models.Model):
    _inherit="crm.lead"

    tasks_list_ids = fields.One2many('task.checklist.line', 'task_list_id')
    progress = fields.Integer(string="Progress", compute="_compute_progress")
    # template_ids = fields.One2many('crm.checklist.template', 'temp_id', string='Checklist Tasks')
    temp_id = fields.Many2one('crm.checklist.template', string='Checklist Templates', index=True, ondelete='set null')

    @api.depends("tasks_list_ids.is_done")
    def _compute_progress(self):
        for elem in self:
            all_task_list = len(elem.tasks_list_ids)
            if all_task_list > 0:
                done_state = len(elem.tasks_list_ids.filtered(lambda l: l.is_done == True))
                elem.progress += done_state/all_task_list*100
            else:
                elem.progress = 0

    @api.onchange('temp_id')
    def _onchange_template(self):
        list_uses_templ_id = set([x.id for x in self.tasks_list_ids.template_parent_id])

        for temp_el in self.temp_id.template_ids:
            if self.temp_id.id not in list_uses_templ_id:
                # self.tasks_list_ids |= self.tasks_list_ids.new(
                #     dict(name=temp_el.name,
                #          description=temp_el.description,
                #          is_done=False,
                #          task_list_id=self._origin.id,
                #          template_parent_id=self.temp_id.id)
                # )
                self.tasks_list_ids = [((0, 0, {'name':temp_el.name,
                                                 'description': temp_el.description,
                                                'is_done': False,
                                                'task_list_id': self._origin.id,
                                                'template_parent_id':self.temp_id.id}))]