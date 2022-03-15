from odoo import api, fields,models

class Partner(models.Model):
    #inherit dengan modul res.partner
    _inherit = 'res.partner'
    
    #ofbool
    is_pegawainya = fields.Boolean(string='Pegawai', default=False)
    is_customernya = fields.Boolean(string='Customer', default=False)