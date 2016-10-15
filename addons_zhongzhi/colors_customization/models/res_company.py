# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class res_company(models.Model):
    _inherit = 'res.company'

    user_own_theme = fields.Boolean('Allow users to change an interface theme through preferences',default=True)

class res_users(models.Model):
    _inherit = 'res.users'

    def __init__(self, pool, cr):
        init_res = super(res_users, self).__init__(pool, cr)
        self.SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        self.SELF_WRITEABLE_FIELDS.extend(['company_color_theme'])
        return init_res

    def get_default_theme(self):
        themes = self.env['colors.customization.theme'].search([('default_for_new_users','=',True)])
        if themes and len(themes) > 0:
            return themes[0].id
        else:
            return themes

    company_color_theme = fields.Many2one('colors.customization.theme', string="Interface theme",default=get_default_theme)
    user_own_theme = fields.Boolean(related='company_id.user_own_theme')    