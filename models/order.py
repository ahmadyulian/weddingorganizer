from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Order(models.Model):
    _name = 'wedding.order'
    _description = 'Deskripsi Order'

    #ofo2m
    orderpanggungdetail_ids = fields.One2many(
        comodel_name='wedding.orderpanggungdetail', 
        inverse_name='order_id', 
        string='Order Panggung')
    
    orderkursitamudetail_ids = fields.One2many(
        comodel_name='wedding.orderkursitamudetail', 
        inverse_name='orderkursi_id', 
        string='Order Kursi Tamu')
    
    #ofchar
    name = fields.Char(string='Kode Order', required=True)

    #oo_fields.DateTime
    tanggal_pesan = fields.Datetime('Tanggal Pemesanan',default=fields.Datetime.now())

    #oo_fields.Date
    tanggal_pengiriman = fields.Date(string='Tanggal Pengiriman', default=fields.Date.today())
    
    #ofm2o
    pemesan = fields.Many2one(
        comodel_name='res.partner', 
        string='Pemesan', 
        domain=[('is_customernya','=', True)],store=True)
    
    #ofint #oofcompute
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    @api.depends('orderpanggungdetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['wedding.orderpanggungdetail'].search([('order_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['wedding.orderkursitamudetail'].search([('orderkursi_id', '=', record.id)]).mapped('harga'))
            record.total = a + b
    
    #ofbool
    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', default=False)
    
class OrderPanggungDetail(models.Model):
    _name = 'wedding.orderpanggungdetail'
    _description = 'Deskripsi Order Panggung Detail'

    #ofm2o
    order_id = fields.Many2one(comodel_name='wedding.order', string='Order')
    panggung_id = fields.Many2one(comodel_name='wedding.panggung', string='Panggung')   
    
    #ofchar
    name = fields.Char(string='Name')

    #ofint #oofcompute
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan * record.qty

    #ofint
    qty = fields.Integer(string='Quantity')

    #ofint #oofcompute
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')
    @api.depends('panggung_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.panggung_id.harga
           
    @api.model
    def create(self,vals):
        record = super(OrderPanggungDetail, self).create(vals) 
        if record.qty:
            self.env['wedding.panggung'].search([('id','=',record.panggung_id.id)]).write({'stok':record.panggung_id.stok-record.qty})
            return record
        
class OrderKursiTamuDetail(models.Model):
    _name = 'wedding.orderkursitamudetail'
    _description = 'Deskripsi Kursi Tamu Detail'
    
    #ofm2o
    orderkursi_id = fields.Many2one(comodel_name='wedding.order', string='Order Kursi')
    kursitamu_id = fields.Many2one(
        comodel_name='wedding.kursitamu', 
        string='Kursi Tamu',
        domain=[('stok','>','100')])
    
    #ofchar
    name = fields.Char(string='Name')

    #ofint #oofcompute
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')
    @api.depends('kursitamu_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.kursitamu_id.harga
    
    #ofint
    qty = fields.Integer(string='Quantity')
    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            bahan = self.env['wedding.kursitamu'].search([('stok', '<',record.qty),('id', '=',record.id)])
            if bahan:
                raise ValidationError("Stok kursi yang dipilih tidak cukup")
    
    #ofint #oofcompute
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    @api.depends('harga_satuan','qty')
    def _compute_harga(self):
        for record in self:
               record.harga = record.harga_satuan * record.qty
    
    @api.model
    def create(self,vals):
        record = super(OrderKursiTamuDetail, self).create(vals) 
        if record.qty:
            self.env['wedding.kursitamu'].search([('id','=',record.kursitamu_id.id)]).write({'stok':record.kursitamu_id.stok-record.qty})
            return record