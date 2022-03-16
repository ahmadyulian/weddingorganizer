from odoo import api, fields, models

class KursiTamu(models.Model):
    _name = 'wedding.kursitamu'
    _description = 'Data tentang kursi tamu dan harganya'

    #ofchar
    name = fields.Char(string='Name')
    
    #ofsel
    tipe = fields.Selection(string='Tipe Kursi', 
    selection=[('plastik','Plastik'), ('besi','Besi'), ('stainless','Stainless')])
    
    #ofint
    stok = fields.Integer(string='Stok Kursi')
    harga = fields.Integer(string='Harga Sewa per Unit')