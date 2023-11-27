from odoo import models, fields



class TemplateLine(models.Model):
    _name = 'checklist.template.line'

    name = fields.Char('Title Line', required=True)
    description = fields.Char('Description', required=False, size=30)
    checklist_id = fields.Many2one('crm.checklist.template', required=True)
