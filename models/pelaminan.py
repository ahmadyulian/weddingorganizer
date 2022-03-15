from odoo import api, fields, models

class Pelaminan(models.Model):
    _name = 'wedding.pelaminan'
    _description = 'Daftar Tip'

    #ofchar
    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi Pelaminan')

    #ofint
    harga = fields.Integer(string='Harga Sewa')