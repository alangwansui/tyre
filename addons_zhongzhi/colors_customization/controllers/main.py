# -*- coding: utf-8 -*-

import openerp
from openerp import http
from openerp.http import request
from openerp.addons.web.controllers.main import Session
from werkzeug.wrappers import Request, Response


class CustomCss(http.Controller):

    @http.route('/custom_colors', type='http', auth="none")
    def get_colors(self):
        custom_css = ''
        current_user = request.env['res.users'].sudo().search([('id', '=', request.context.get('uid'))])
        if current_user and current_user[0].company_color_theme:
            custom_css = current_user[0].company_color_theme.css
        return Response(str(custom_css), mimetype='text/css')