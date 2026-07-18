from odoo import models, fields

class MessageWizard(models.TransientModel):
    _name = "message.wizard"
    _description = "Send Message"

    message = fields.Text(string="Message")

    def action_submit(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Success',
                'message': 'Message submitted successfully!',
                'type': 'success',
                'sticky': False,
            }
        }