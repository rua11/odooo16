from odoo import models, fields, api
from odoo.exceptions import ValidationError
import base64


class DungDz(models.Model):
    _name = 'dungdz'
    STATE_SELECTION = [('draft', 'Nháp'), ('confirm', 'Xác Nhận'),
                       ('done', 'Hoàn Thành'), ('cancelled', 'Hủy bỏ')]
    
    video_dz = fields.Binary(string="video")
    
    
    document_fname = fields.Char()
    
    # video_url = fields.Char('video URL', help="URL of a video for showcasing your profile")
    # embed_code = fields.Char(compute="_compute_embed_code")
    pdf_dz = fields.Binary(string="PDF")
    document_f = fields.Char(string="Cat")
    document_fa = fields.Char(string="Dog", translate=True)
    document_fa1 = fields.Text(string="Monkey", translate=True)
    # state = fields.Selection(STATE_SELECTION, default='draft', string="Trạng Thái Đăng Ký", translate = True)
    
    # def decode_binary(self):
    #     if self.pdf_dz:
    #         base64.b64decode(self.pdf_dz)
    
    
    video_file = fields.Binary(string='Video File')
    video_preview = fields.Binary(string='Video Preview', compute='_compute_video_preview', store=True)

    @api.onchange('video_file')
    def _compute_video_preview(self):
            if self.video_file:
                video_preview = self.env['ir.attachment'].search([('res_model', '=', 'dungdz'), ('res_id', '=', self.id), ('name', 'ilike', 'video_preview')], limit=1)
            if not video_preview:
                video_preview = self.env['ir.attachment'].create({
                'name': 'video_preview',
                'datas': self.env['video.converter'].convert(self.video_file),
                'res_model': 'dungdz',
                'res_id': self.id,
                })
            self.video_preview = video_preview.datas if video_preview else False
            
    @api.onchange('document_fname')
    def decode_binary1(self):
        if self.document_fname:
            fh = open("video.mp4", "wb")
            de_video = base64.b64decode(self.video_dz)
            fh.write(de_video)
            fh.close()
            
            # return open("video.mp4", "wb")
            
            
 
   