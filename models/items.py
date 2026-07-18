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

    def action_open_message_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Send Message',
            'res_model': 'message.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('office_supplies.view_message_wizard_form').id,
            'target': 'new',
        }