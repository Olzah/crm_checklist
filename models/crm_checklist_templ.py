from odoo import models, fields



class CrmChecklist(models.Model):
    _name = 'crm.checklist.template'

    name = fields.Char('Title', required=True)
    description = fields.Char('Description', required=False, size=30)
    template_ids = fields.One2many('checklist.template.line', 'checklist_id', string="Template line")
    lead_ids = fields.One2many('crm.lead', 'temp_id')
    template_parent_ids = fields.One2many('task.checklist.line', 'template_parent_id')