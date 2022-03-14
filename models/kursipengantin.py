from odoo import api, fields, models

class KursiPengantin(models.Model):
    _name = 'wedding.kursipengantin'
    _description = 'Daftar Kursi Pengantin Pelaminan'

    #ofchar
    name = fields.Char(string='Name')
    #ofchar
    deskripsi = fields.Char(string='Deskripsi Kursi Pengantin')
    #ofint
    harga = fields.Integer(string='Harga Sewa')