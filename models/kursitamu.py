from odoo import api, fields, models

class KursiTamu(models.Model):
    _name = 'wedding.kursitamu'
    _description = 'Deskripsi Kursi Tamu dan Harganya'

    #ofchar
    name = fields.Char(string='Name')
    #ofsel
    tipe = fields.Selection(string='Tipe Kursi', selection=[('plastik','Plastik'), ('stainless','Stainless')])
    #ofint
    stok = fields.Integer(string='Stok Kursi')
    harga = fields.Integer(string='Harga Sewa per Unit')