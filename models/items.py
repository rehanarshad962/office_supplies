from  odoo import  fields,models
class items(models.Model):
    _name='office.items'
    _description='office items'

    item_name=fields.Char(string="Item Name")
    category=fields.Char(string="Category")
    quantity=fields.Integer(string="Quantity")
    price=fields.Float(string="Price")
    supplier=fields.Char(string="Supplier")
    reorder_level=fields.Integer(string="Reorder Level")