from odoo import models,fields

class EstateProperty(models.Model):
    _name='estate.property'
    _description='Estate Property'

    name=fields.Char("name",required=True)
    description=fields.Text()
    property_type_id=fields.Many2one("estate.type")
    postcode=fields.Char()
    date_availability=fields.Date(default=fields.Date.today)
    expected_price=fields.Float(digits=(6,0),help="expected price of the property",readonly=True)
    bedrooms=fields.Integer(default=2,help="Number of the property's bedrooms")
    living_area=fields.Float()
    factory_size=fields.Float()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garder_area=fields.Integer()
    garden_orientation=fields.Selection( selection=[('South', 'South'), ('North', 'North'),('East', 'East'),('West', 'West'	)],)
    active=fields.Boolean(default=False)
    state=fields.Selection(selection=[('new','new'),('offer received','offer received'),('offer accepted','offer accepted'),('sold','sold'),('canceled','canceled')],default='new')
