from odoo import models, api, _
import re

class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    def get_date_order(self, DATA):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', str(DATA))