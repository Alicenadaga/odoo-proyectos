from odoo import models, fields


class Producto(models.Model):
    _name = "pedidos.producto"
    _description = "Los pedidos que hacen del producto"

    name = fields.Char(required=True)
    precio = fields.Float(required=True)
    tipo_id = fields.Many2one("pedidos.tipo.producto", string="Tipo")
