# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import UserError




class Test(models.Model):
    _name = 'testmodule'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _description = 'demo'
    STATE_SELECTION = [('draft', 'Nháp'), ('confirm', 'Xác Nhận'),
                       ('done', 'Hoàn Thành'), ('cancelled', 'Hủy bỏ')]
    GENDER_SELECTION = [('male', 'Nam'), ('female', 'Nữ'), ("other", "Khác")]
    img_test = fields.Binary(string="mèo méo meo")
    name = fields.Char(string="Tên", required=True)
    gender = fields.Selection(GENDER_SELECTION, string="Giới tính", required=True)
    # year2 = fields.Datetime(string="Năm sinh 2", default=datetime.now().strftime('%Y'))
    year2 = fields.Datetime(string="Năm sinh 2", default=datetime(2000,1,1).strftime('%Y'))
    year = fields.Integer(string='Năm Sinh')
    age = fields.Integer(string="Tuổi")
    province_id = fields.Many2one(comodel_name='res.province', ondelete='restrict', string='Tỉnh/Thành phố', required=True)
    district_id = fields.Many2one(comodel_name='res.district', ondelete='restrict',string='Quận/huyện', required=True)
    ward_id = fields.Many2one(comodel_name='res.ward', ondelete='restrict',string='Xã/phường', required=True)
    address = fields.Char(string="Địa chỉ")
    phone = fields.Integer(string="SĐT")
    state = fields.Selection(STATE_SELECTION, default='draft', string="Trạng Thái Đăng Ký")

    @api.onchange('year2')
    def _age(self):
        if self.year2:
            a = self.year2.year
            currentYear = datetime.now().year
            if a>= currentYear:
                raise UserError('Tuổi của mày không thể  nhập linh tinh')
            else:
                self.age = currentYear - a
                if self.age >= 18:
                    print("Đã đủ tuổi đi tù")
                else:
                    print("Vẫn còn xanh lắm")

    @api.onchange('province_id')
    def _onchange_province_id(self):
        res = {}
        self.district_id = False
        if self.province_id:
            list_district = self.env['res.district'].search([('depend_province', '=', self.province_id.id)])
            if len(list_district) > 0:
                parent_code = list_district[0].parent_code
                res = {'domain': {'district_id': [('parent_code', '=', parent_code)]}}
            else:
                res = {}
        return res

    @api.onchange('district_id')
    def _onchange_district_id(self):
        res = {}
        self.ward_id = False
        if self.district_id:
            list_ward = self.env['res.ward'].search([('depend_district', '=', self.district_id.id)])
            if len(list_ward) > 0:
                parent_code = list_ward[0].parent_code
                res = {'domain': {'ward_id': [('parent_code', '=', parent_code)]}}
        else:
            res = {}
        return res


    # @api.depends('value2222222')
    # def _value_pc(self):
    #     self.value2222222 = float(self.value2) / 100

    def action_confirm(self):
        self.state = 'confirm'
        self.message_post(body='%s đã xác nhận bản đăng ký %s' % (self.env.user.name, self.name))

    def action_done(self):
        self.state = 'done'
        self.message_post(body='%s đã hoàn thành bản đăng ký %s' % (self.env.user.name, self.name))

    def action_draft(self):
        self.state = 'draft'
        self.message_post(body='%s đã tạo nháp bản đăng ký %s' % (self.env.user.name, self.name))

    def action_cancelled(self):
        self.state = 'cancelled'
        self.message_post(body='%s đã huỷ bỏ bản đăng ký %s' % (self.env.user.name, self.name))



