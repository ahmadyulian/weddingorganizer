from odoo import http, fields, models
from odoo.http import request
import json

class KursiTamuController(http.Controller):
   @http.route('/kursitamu', auth='public', methods=['GET'])
   def getKursiTamu(self, **kwargs):
        kursi = request.env['wedding.kursitamu'].search([])
        value = []
        for k in kursi:
            value.append({"namakursi" : k.name,
                         "tipe_bahan" : k.tipe,
                         "stok_tersedia" : k.stok,
                         "harga_sewa" : k.harga})
        return json.dumps(value)
    else:
            kursiid = request.env['wedding.kursitamu'].search([('id','=',idnya)])
            for k in kursiid:
                value.append({"id": k.id,
                            "namakursi" : k.name,
                            "tipe_bahan" : k.tipe,
                            "stok_tersedia" : k.stok,
                            "harga_sewa" : k.harga})
            return json.dumps(value)
    
    @http.route('/createkursi',auth='user', type='json', methods=['POST'])
    def createKursi(self, **kw):    
        if request.jsonrequest:    
            if kw['name']:
                vals={
                    'name': kw['name'], 
                    'tipe' : kw['tipe'],
                    'stok' : kw['stok'],
                    'harga' : kw['harga'],
                }
                kursibaru = request.env['wedding.kursitamu'].create(vals)
                args = {'success': True, 'ID':kursibaru.id}
                return args