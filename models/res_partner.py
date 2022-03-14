from odoo import api, fields,models

class Partner(models.Model):
    _inherit = 'res.partner'
    
    #ofbool
    pegawai = fields.Boolean(string='Pegawai', default=False)
    pelanggan = fields.Boolean(string='Customer', default=False)