from odoo import models, fields, api

class Invoice(models.Model):
    _inherit = 'account.invoice'

    sign_by = fields.Many2one('res.users', string='Sign by')
    sign_employee_id = fields.Many2one('hr.employee', compute='compute_employee_id')

    @api.one
    @api.depends('sign_by')
    def compute_employee_id(self):
        employee_id = self.env['hr.employee'].search([('user_id', '=', self.sign_by.id)],limit=1)
        self.sign_employee_id = employee_id and employee_id.id or False


