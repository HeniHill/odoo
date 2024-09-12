from odoo import models,fields


class LocalRequisitionDetail(models.Model):
    _name='local.requisition.detail'
    _description='requisition detailse'

    
    name=fields.Char("remark",required=True)
    qty=fields.Integer("qty",required=True)
    unit_cost=fields.Integer("unit cost",required=True)
    unit_of_measure=fields.Char("unit of measure",required=False)
    product_id=fields.Many2one("product.product",string="Product")
    requsition_id=fields.Many2one(comodel_name="local.requisition",name="requisition_id",required=True)
 
   