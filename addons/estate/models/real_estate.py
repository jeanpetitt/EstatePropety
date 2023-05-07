from odoo import models, fields, api
import datetime

# model buyer
class EStateBuyer(models.Model):
    _name = "estate.buyer"
    name = fields.Char(required=True)
    
# model buyer
class EstateSeller(models.Model):
    _name = "estate.seller"
    name = fields.Char(required=True)

# model estate type property example House, Appartement...
class EstateType(models.Model):
    _name = "estate.property.type" 
    name = fields.Char(required=True)
# model estate tag property example renovated, 
class EstateTag(models.Model):
    _name = "estate.property.tag"
    name = fields.Char(required=True)
    
# model offer 
class Estateoffer(models.Model):
    _name = "estate.property.offer"
    price = fields.Float()
    status = fields.Selection(selection=[("Accepted", "Accepted"), ("Refused", "Refused")], copy=False)
    partener_id = fields.Many2one("res.partner", string="Partener", required=True)
    validity = fields.Integer("Validity(days)",default=7)
    date_deadline = fields.Date("Dealine")

class Estate(models.Model):
    choices = [
        ("North", "North"),
        ("South", "South"),
        ("East", "East"),
        ("West", "West")
    ]
    _name = "estate.property"
    _description  = "Estate Model"
    
    title = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False, default=25000)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation =  fields.Selection(selection=choices)
    active = fields.Boolean(default=True)
    status = fields.Selection(selection=[("New", "New"), ("Offer Recived", "Offer Recived")])
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("estate.buyer", string="Salesman", index=True, default=lambda self: self.env.user)
    seller_id = fields.Many2one("estate.seller", string="Seller", index=True, copy=False)
    tag_id = fields.Many2many("estate.property.tag")
    offer_ids =  fields.Many2many("estate.property.offer")
    total_area = fields.Integer(compute="_compute_total")
    best_price = fields.Char(compute="_compute_best_price_offer")

    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
            
    @api.depends("offer_ids.price")
    def _compute_best_price_offer(self):
        for record in self:
            record.best_price = max(record.mapped("offer_ids.price"))          

    def solde(self):
        for record in self:
            if record.best_price <= record.selling_price:
                record.selling_price += 100
        return True
    