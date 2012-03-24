# -*- coding: utf-8 -*-
import time
from osv import fields,osv
from tools.translate import _

class delivery_grid_line(osv.osv):
    _inherit = 'delivery.grid.line' 
   
    _columns = { 'type2': fields.selection([('colli','Nr. Colli'),('weight','Weight'),('volume','Volume'),('wv','Weight * Volume'), ('price','Price')], 'Variable', required=True),
               # 'stock_warehouse':fields.many2one('stock.warehouse', 'Magazzino'),
                }
    _order = "list_price" 
delivery_grid_line()

class delivery_grid(osv.osv):
    _inherit = "delivery.grid"
    _columns = { 'carrier_id': fields.many2one('delivery.carrier', 'Carrier',  ondelete='cascade'),
                'magazzino_id':fields.many2one('stock.location', 'Magazzino', required=True),
                }
    
delivery_grid()