from odoo import models, fields



class CrmChecklist(models.Model):
    _name = 'crm.checklist.template'

    name = fields.Char('Title', required=True)
    description = fields.Char('Description', required=False, size=30)
    lead_ids = fields.One2many('crm.lead', 'temp_id')
    # task_checklist_ids = fields.One2many('task.checklist', 'crm_checklist_id', 'Checklist Tasks')
    # lead_ids = fields.One2many('crm.lead', 'crm_checklist_id', 'CEM Lead')