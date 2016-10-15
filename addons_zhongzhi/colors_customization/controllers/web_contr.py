# -*- coding: utf-8 -*-

import re
import openerp
import functools

from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
from openerp.tools.translate import _
from openerp.addons.web.controllers.main import Home
from openerp.addons.web.controllers.main import Binary
from openerp.addons.web.controllers.main import ensure_db
import json
import werkzeug.utils
import werkzeug.wrappers

from openerp.modules import get_module_resource
from cStringIO import StringIO

def db_info():
    version_info = openerp.service.common.exp_version()
    return {
        'server_version': version_info.get('server_version'),
        'server_version_info': version_info.get('server_version_info'),
    }

class HomeStyle(Home):

    @http.route('/web', type='http', auth="none")
    def web_client(self, s_action=None, **kw):
        ensure_db()
        if not request.session.uid:
            return werkzeug.utils.redirect('/web/login', 303)
        if kw.get('redirect'):
            return werkzeug.utils.redirect(kw.get('redirect'), 303)

        request.uid = request.session.uid

        theme_id = request.registry['res.users'].browse(request.cr,request.uid,request.uid, context=request.context).company_color_theme
        theme_data = False
        if theme_id:
            if theme_id.footer_color:
                footer_color = theme_id.footer_color
            else:
                footer_color = '#a24689'

            if theme_id.footer_url:
                footer_url = theme_id.footer_url
            else:
                footer_url = '/web'                

            theme_data = {
                'footer_text':theme_id.footer_text,
                'footer_url':footer_url,
                'url_favicon':theme_id.url_favicon,
                'footer_color':footer_color,
                'meta_title':theme_id.meta_title
            }
        else:
            theme_data = {
                'footer_text':False,
                'footer_url':False,
                'url_favicon':False,
                'footer_color':False,
                'meta_title':False,
            } 

        menu_data = request.registry['ir.ui.menu'].load_menus(request.cr, request.uid, request.debug, context=request.context)
        return request.render('web.webclient_bootstrap', qcontext={'theme_data':theme_data,'menu_data': menu_data, 'db_info': json.dumps(db_info())})



class Binary_ITL(Binary):

    @http.route([
        '/web/binary/company_logo',
        '/logo',
        '/logo.png',
    ], type='http', auth="none", cors="*")
    def company_logo(self, dbname=None, **kw):
        imgname = 'placeholder.png'
        placeholder = functools.partial(get_module_resource, 'web', 'static', 'src', 'img')
        uid = None
        if request.session.db:
            dbname = request.session.db
            uid = request.session.uid
        elif dbname is None:
            dbname = db_monodb()

        if not uid:
            uid = openerp.SUPERUSER_ID

        if not dbname:
            response = http.send_file(placeholder(imgname))
        else:
            try:
                # create an empty registry
                registry = openerp.modules.registry.Registry(dbname)
                with registry.cursor() as cr:
                    cr.execute("""SELECT c.logo_web, c.write_date
                                    FROM res_users u
                               LEFT JOIN res_company c
                                      ON c.id = u.company_id
                                   WHERE u.id = %s
                               """, (uid,))
                    row = cr.fetchone()
                    if row and row[0]:
                        image_data = StringIO(str(row[0]).decode('base64'))
                        response = http.send_file(image_data, filename=imgname, mtime=row[1])
                    else:
                        response = http.send_file(placeholder('placeholder.png'))
            except Exception:
                response = http.send_file(placeholder(imgname))

        return response          
