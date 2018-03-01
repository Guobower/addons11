from odoo import models, fields, api

import amount_to_text_id


class purchase_order(models.Model):
    _inherit = "purchase.order"

    @api.one
    @api.depends('amount_total')
    def _amount_in_words(self):
        # self.amount_to_text = amount_to_text_id(self.amount_total, self.currency_id.symbol)
        self.amount_to_text = amount_to_text_id.amount_to_text_id_call(self.amount_total)

    spk = fields.Boolean('SPK', select=True, help="It indicates that a surat perintah kerja selected")
    amount_to_text = fields.Text(string='In Words',
                                 store=True, readonly=True, compute='_amount_in_words')
