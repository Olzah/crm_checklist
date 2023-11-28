from odoo import api, models, fields

class ElemChecklist(models.Model):
    _name = 'task.checklist.line'
    _description = "Task checklist line"

    name = fields.Char('Task Name', required=True, size=40)
    description = fields.Char('Description', required=False, size=50)
    task_list_id = fields.Many2one('crm.lead', string='Task List')
    is_done = fields.Boolean('Done', default=False)
    template_parent_id = fields.Many2one('crm.checklist.template', string='Template Parent')

    def setStatusTaskTrue(self):
        self.write({'is_done': True})

    def setStatusTaskFalse(self):
        self.write({'is_done': False})
