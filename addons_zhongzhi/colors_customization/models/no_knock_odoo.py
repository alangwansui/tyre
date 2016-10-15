# -*- coding: utf-8 -*-
from openerp.osv import osv
class Waranty(osv.osv):
    _inherit = 'publisher_warranty.contract'
    
    def update_notification(self, cr, uid, ids, cron_mode=True,
                            context=None):
        return True
