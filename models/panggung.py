from odoo import api, fields, models

class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'New Description'

    #ofchar
    name = fields.Char(string='Name', required=True)

    #ofm2o
    pelaminan_id = fields.Many2one(comodel_name='wedding.pelaminan', 
                                string='Tipe Pelaminan', 
                                required=True)   
    kursipengantin_id = fields.Many2one(comodel_name='wedding.kursipengantin', 
                                        string='Kursi Pengantin', 
                                        required=True)
    
    #ofsel
    bunga = fields.Selection(string='Tipe Bunga', selection=[('bunga mati', 'Bunga Dead'), ('bunga hidup', 'Bunga Life')])    
    
    #ofchar
    accesories = fields.Char(string='Aksesoris Pelaminan')
    
    #ofint #oofcompute
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    @api.depends('pelaminan_id','kursipengantin_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan_id.harga + record.kursipengantin_id.harga
    
    stok = fields.Integer(string='Stock Paket Panggung')
    
    deskripsi_pelaminan = fields.Char(compute='_compute_deskripsi_pelaminan', string='Deskripsi Pelaminan')
    @api.depends('pelaminan_id')
    def _compute_deskripsi_pelaminan(self):
        for record in self:
            record.deskripsi_pelaminan = record.pelaminan_id.deskripsi
    
    deskripsi_kursipengantin = fields.Char(compute='_compute_deskripsi_kursipengantin', string='Deskripsi Kursi Pengantin')
    @api.depends('kursipengantin_id')
    def _compute_deskripsi_kursipengantin(self):
        for record in self:
            record.deskripsi_kursipengantin = record.kursipengantin_id.deskripsi