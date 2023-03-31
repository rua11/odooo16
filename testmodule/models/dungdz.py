from odoo import models, fields, api
from odoo.exceptions import ValidationError



class DungDz(models.Model):
    _name = 'dungdz'
    STATE_SELECTION = [('draft', 'Nháp'), ('confirm', 'Xác Nhận'),
                       ('done', 'Hoàn Thành'), ('cancelled', 'Hủy bỏ')]
    
    video_dz = fields.Binary(string="video")
    document_fname = fields.Char()
    
    # video_url = fields.Char('video URL', help="URL of a video for showcasing your profile")
    # embed_code = fields.Char(compute="_compute_embed_code")
    pdf_dz = fields.Binary(string="PDF")
    document_f = fields.Char(string="Má ơi")
    document_fa = fields.Char(string="Dượng ơi", translate=True)
    document_fa1 = fields.Text(string="Bà Nội ơi", translate=True)
    # state = fields.Selection(STATE_SELECTION, default='draft', string="Trạng Thái Đăng Ký", translate = True)
    
    
 
   