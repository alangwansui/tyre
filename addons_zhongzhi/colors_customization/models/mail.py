# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from openerp import tools, SUPERUSER_ID
from openerp.tools.translate import _
from openerp.tools.mail import plaintext2html
from urlparse import urljoin

"""class mail_mail(osv.Model):
    _name = "mail.mail"
    _inherit = "mail.mail"

    def send_get_mail_body(self, cr, uid, mail, partner=None, context=None):
        body = mail.body_html
        link = None
        user = self.pool.get("res.users").browse(cr, SUPERUSER_ID, uid, context=context)[0]

        signature_company = ""
        if user.company_id.custom_email_footer and user.company_id.custom_email_footer != '':
            signature_company = '<br />' + user.company_id.custom_email_footer
            if partner and partner.lang:
                signature_company = '<br />' + user.with_context(lang=partner.lang).company_id.custom_email_footer

            body = tools.append_content_to_html(body, signature_company, plaintext=False, container_tag='div')

        if user.company_id.footer_link and user.company_id.footer_link.find('*'):
            if mail.notification or (mail.model and mail.res_id and not mail.no_auto_thread):
                link = self._get_partner_access_link(cr, uid, mail, partner, context=context)
            if link:
                index_begin = link.find('<a style')
                index_end = link.find('</a>') +4
                url = link[index_begin:index_end]

                footer_link = user.company_id.footer_link
                if partner and partner.lang:
                    footer_link = user.with_context(lang=partner.lang).company_id.footer_link

                link = footer_link.replace('*',url)
                body = tools.append_content_to_html(body, link, plaintext=False, container_tag='div')
        return body


class mail_notification(osv.Model):
    _name = "mail.notification"
    _inherit = "mail.notification"

    def get_signature_footer(self, cr, uid, user_id, res_model=None, res_id=None, context=None, user_signature=True):
        footer = ""
        if not user_id:
            return footer

        # add user signature
        user = self.pool.get("res.users").browse(cr, SUPERUSER_ID, [user_id], context=context)[0]
        if user_signature:
            if user.signature:
                signature = user.signature
            else:
                signature = "--<br />%s" % user.name
            footer = tools.append_content_to_html(footer, signature, plaintext=False)
        
        return footer

mail_notification()      """  