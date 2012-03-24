# -*- encoding: utf-8 -*-

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import decimal_precision as dp
import time
import netsvc
import pooler, tools
import math
from tools.translate import _

from osv import fields, osv

class FiscalDocHeader(osv.osv):
    _inherit = "fiscaldoc.header"
   
    def on_change_colli(self, cr, uid, ids, magazzino_id, totale_colli, context):
        #import pdb;pdb.set_trace()
        v = {}
        delivery_obj=self.pool.get('delivery.grid')
        filtro=[('magazzino_id','=',magazzino_id)]
        testa_regola = delivery_obj.search(cr, uid, filtro)
        if testa_regola:
            for linee_regola in delivery_obj.browse(cr, uid, testa_regola[0]).line_ids:
                if linee_regola.type2 == 'colli':
                    #import pdb;pdb.set_trace()
                    price_dict = {'colli' : totale_colli}
                    test = eval(linee_regola.type2+linee_regola.operator+str(linee_regola.max_value), price_dict)
                    if test:
                        #import pdb;pdb.set_trace()
                        v['spese_trasporto'] = 0
                        v['spese_trasporto'] = linee_regola.list_price
                        #if totale_colli >= 11:
                            #v['spese_trasporto'] = 0
                        
                        return {'value': v}
FiscalDocHeader()