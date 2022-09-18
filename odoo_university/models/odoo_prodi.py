# -*- coding: utf-8 -*-
from odoo import  fields, models


class OdooProdi(models.Model):
    _name = 'odoo.prodi' # membuat Field

    name = fields.Char('Program Studi')
    code = fields.Char('Kode prodi')
    fakultas_id = fields.Many2one("odoo.fakultas","Fakultas")
    tag_ids = fields.Many2many("odoo.tag","rel_prodi_tag","prodi_id","tag_id","Panggilan")