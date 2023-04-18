from odoo import SUPERUSER_ID, models, fields, api, _
import uuid

from odoo.http import request

from odoo.exceptions import ValidationError

class TestLinhTinh(models.Model):
    _name = 'test.linhtinh'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Một Hai Ba Bốn'
    
    lt_id = fields.Char('UUID', default=lambda self: str(uuid.uuid4()))
    so1 = fields.Float(string='Float')
    email_formm = fields.Char(string="Email_form")
    mail_too = fields.Char(string="Email_to")
    subject = fields.Char(string = "Subject")
    name = fields.Char(string = "Name")

    # def action_send_email(self):
    #     mail_template = self.env.ref('testmodule.maiz_template')
    #     mail_template.send_mail(self.id, force_send=True)
    
    def action_send_email(self):
        self.ensure_one()
        user_company = self.env.user.company_id
        company_ids = []
        mail_template1 = request.env["mail.template"].sudo().search([('model','=','test.linhtinh')])
        for rec in mail_template1:
            company_ids.append(rec.create_uid.company_id.id)
            if rec.create_uid.company_id.id == user_company.id:
                rec.send_mail(self.id, force_send=True)
        if user_company.id not in company_ids:
            mail_template = request.env["mail.template"].sudo().search([('model','=','test.linhtinh'),('create_uid','=',1)], limit=1)
            mail_template.send_mail(self.id, force_send=True)
            
    
    @api.constrains('lt_id') 
    def _check_field_is_uuid(self): 
        for record in self: 
            try: 
                uuid.UUID(record.lt_id) 
            except ValueError: 
                raise ValidationError(_('Field must be a valid UUID.'))
    # gui email
    # def action_send_email(self):
    #     '''
    #     This function opens a window to compose an email, with the emai template message loaded by default
    #     '''
        
    #     self.ensure_one()
    #     ir_model_data = self.env['ir.model.data']
    #     try:
    #         template_id = ir_model_data._xmlid_lookup('testmodule.maiz_template')
    #         a = template_id[2]
    #     except ValueError:
    #         template_id = False
    #     try:
    #         compose_form_id = ir_model_data._xmlid_lookup('mail.email_compose_message_wizard_form')[2]
    #     except ValueError:
    #         compose_form_id = False
    #     ctx = {
    #         'default_model': 'test.linhtinh',
    #         'default_res_id': self.ids[0],
    #         'default_use_template': bool(template_id),
    #         'default_template_id': a,
    #         'default_composition_mode': 'comment',
    #     }
    #     form_mail = {
    #         'name': _('Compose Email'),
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'mail.compose.message',
    #         'views': [(compose_form_id, 'form')],
    #         'view_id': compose_form_id,
    #         'target': 'new',
    #         'context': ctx,
    #     }
    #     return form_mail

    def action_post(self):
        self.message_post(self, body="ớ ớ ớ sssssss")
    
    