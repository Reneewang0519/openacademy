# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'

    # 在向导中为课务字段定义一个默认值；使用上下文参数self._context来获取当前课务
    def _default_session(self):
        return self.env['openacademy.session'].browse(self._context.get('active_id'))
    # session_id = fields.Many2one('openacademy.session', string="Session", required=True)
    session_ids = fields.Many2many('openacademy.session', string="Sessions", required=True, default='_default_sessions')
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    # 把参与者添加到给定课务
    @api.multi
    def subscribe(self):
        self.session_id.attendee_ids |= self.attendee_ids
        return {}
