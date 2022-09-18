# -*- coding: utf-8 -*-
from odoo import  fields, models


class OdooFakultas(models.Model):
    _name = 'odoo.fakultas' # membuat Field
    _description = 'New Description'

    name = fields.Char('Nama Fakultas')
    code = fields.Char('Kode Fakultas')
    prodi_ids = fields.One2many("odoo.prodi","fakultas_id","Daftar Program Studi")
