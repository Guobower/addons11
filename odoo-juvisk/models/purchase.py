from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('temp.value') or '/'
        return super(PurchaseOrder, self).create(vals)

    @api.multi
    def button_approve(self, force=False):
        if self.spk:
            name = self.env['ir.sequence'].next_by_code('purchase.order.spk')
        else:
            name = self.env['ir.sequence'].next_by_code('purchase.order')
        self.write({'state': 'purchase', 'name': name})
        self._create_picking()
        if self.company_id.po_lock == 'lock':
            self.write({'state': 'done'})
        return {}