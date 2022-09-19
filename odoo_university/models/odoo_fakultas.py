# -*- coding: utf-8 -*-
from dataclasses import field
from xml.sax.handler import feature_external_ges
from odoo import  fields, models


class OdooFakultas(models.Model):
    _name = 'odoo.fakultas' # membuat Field
    _description = 'New Description'

    name = fields.Char('Nama Fakultas')
    code = fields.Char('Kode Fakultas')
    mahasiswa_ids = fields.One2many('odoo.mahasiswa', 'fak_id','Nama Mahasiswa')
    prodi_ids = fields.One2many("odoo.prodi","fakultas_id","Daftar Program Studi")
