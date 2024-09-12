from odoo import models,fields,api

class StockPicking(models.Model):
    _inherit='stock.picking'

    req_id=fields.Many2one(comodel_name="local.requisition",name="req_id",help="Request No from Local Requisition",string="Request No",required=True)