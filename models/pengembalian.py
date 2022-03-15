from odoo import api, fields, models

class Pengembalian(models.Model):
    _name = 'wedding.pengembalian'
    _description = 'Pengembalian Barang Sewa'

    #oofcompute
    name = fields.Char(compute='_compute_nama_penyewa', string='Nama Penyewa')
    
    @api.depends('order_id')
    def _compute_nama_penyewa(self):
        for record in self:
            record.name = self.env['wedding.order'].search([('id', '=', record.order_id.id)]).mapped('pemesan').name
    
    #ofm20
    order_id = fields.Many2one(comodel_name='wedding.order', string='No. Order')
    
    #oo_fields.Date
    tanggal_pengembalian = fields.Date(string='', default=fields.Date.today())
    
    #ofint #oofcompute
    tagihan = fields.Integer(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total            
   
    @api.model
    def create(self,vals):
        record = super(Pengembalian, self).create(vals) 
        if record.tanggal_pengembalian:
            self.env['wedding.order'].search([('id','=',record.order_id.id)]).write({'sudah_kembali':True})
            return record

    def unlink(self):
        for wiku in self:
            self.env['wedding.order'].search([('id','=',wiku.order_id.id)]).write({'sudah_kembali':False})
        record = super(Pengembalian, self).unlink()