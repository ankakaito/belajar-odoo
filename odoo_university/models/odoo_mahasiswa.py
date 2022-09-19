# -*- coding: utf-8 -*-
from odoo import  fields, models


class OdooMahasiswa(models.Model):
    _name = 'odoo.mahasiswa'

    nim = fields.Char('Nim Mahasiswa')
    name = fields.Char('Nama Mahasiswa')
    kelas  = fields.Char('Kelas')
    semester = fields.Char('semester')
    prodi_id = fields.Many2one("odoo.prodi","Program Studi")
    fak_id = fields.Many2one('odoo.fakultas','Fakultas')