from odoo import api, models, fields

class ElemChecklist(models.Model):
    _name = 'task.checklist.line'
    _description = "Task checklist line"

    name = fields.Char('Task Name', required=True, size=15)
    description = fields.Char('Description', required=False, size=30)
    task_list_id = fields.Many2one('crm.lead', required=True, readonly=True)
    is_done = fields.Boolean('Done', default=False)
    state = fields.Selection([
        ('new', 'New'),
        ('done', 'Completed'),], 'State', default='new',
        store=True)