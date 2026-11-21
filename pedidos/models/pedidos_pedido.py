from odoo import fields, models


class Pedido(models.Model):
    _name = "pedidos.pedido"
    _description = "un pedido"

    name = fields.Char(required=True)
    description = fields.Text()
    fecha_encargo = fields.Date()
    fecha_entrega = fields.Date()
    direccion_entrega = fields.Char()
    prioridad = fields.Selection(
        selection=[("baja", "Baja"), ("media", "Media"), ("alta", "Alta")],
    )
    metodo_pago = fields.Selection(
        selection=[("paypal", "paypal"), ("tropipay", "tropipay"), ("usdt", "usdt")],
    )
    estado = fields.Selection(
        selection=[
            ("borrador", "borrador"),
            ("confirmado", "confirmado"),
            ("entregado", "entregado"),
            ("cancelado", "cancelado"),
        ],
        required=True,
        copy=False,
        default="borrador",
    )
    cliente_id = fields.Many2one("res.partner", string="Clientes", required=True)
