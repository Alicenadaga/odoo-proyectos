from odoo import models, fields


class TipoProducto(models.Model):
    _name = "pedidos.tipo.producto"
    _description = "Diferentes tipos de productos"

    name = fields.Char(required=True)
    productos_ids = fields.One2many("pedidos.producto", "tipo_id", string="Productos")
