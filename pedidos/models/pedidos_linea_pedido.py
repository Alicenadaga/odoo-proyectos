from odoo import fields, models, api


class LineaPedido(models.Model):
    _name = "pedidos.linea.pedido"
    _description = "Una linea de pedidos"

    pedido_id = fields.Many2one(
        "pedidos.pedido", string="Pedido", required=True, ondelete="cascade"
    )
    producto_id = fields.Many2one("pedidos.producto", string="Producto", required=True)
    cantidad = fields.Integer(default=1)
    precio_unitario = fields.Float()
    subtotal = fields.Float(compute="_compute_subtotal")

    @api.depends("cantidad", "precio_unitario")
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.cantidad * record.precio_unitario

    _sql_constraints = [
        (
            "check_cantidad",
            "CHECK(cantidad>0)",
            "La cantidad debe ser estrictamente positiva",
        ),
    ]
