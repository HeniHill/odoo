from odoo import models,fields,api

class LocalRequisition(models.Model):
    _name='local.requisition'
    _description='Stock Requisition'
    _inherit=['mail.thread']
    _rec_name='reference'

    reference=fields.Char("reference",default="New",readonly=True)
    description=fields.Char("desc",tracking=True)
    request_line = fields.One2many(
        comodel_name='local.requisition.detail',
        inverse_name='requsition_id',
        string="Request Details",
        copy=True, auto_join=True)
    status=fields.Selection([('Draft','Draft'),('Posted','Posted'),('Cancelled','Cancelled')],"status",default='Draft',tracking=True)

    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if  not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code(
                    'local.requisition')
        
        print(vals_list)

        return super().create(vals_list)

    

    def post_request(self):
        self.write({'status':'Posted'})

    def cancel_request(self):
        self.write({'status':'Cancelled'})