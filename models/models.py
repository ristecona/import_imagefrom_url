# -*- coding: utf-8 -*-
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urlparse import urlparse, parse_qsl, urlunparse, urljoin

except ImportError:
    from urllib.parse import urlparse, parse_qsl, urlunparse, urljoin
import urllib.request
import logging
import base64
import string

_logger = logging.getLogger(__name__)
from odoo import models, fields, api


class import_imagefrom_url(models.Model):
    _inherit = 'product.template'
    url_image = fields.Char("IMAGE URL: ", default='')

    @api.multi
    def write(self, vals):
        res = super(import_imagefrom_url, self).write(vals)
        if 'url_image' in vals and vals['url_image'] != '':
            temp_file, temp_header = urllib.request.urlretrieve(vals['url_image'])
            fo = open(temp_file, "rb")
            bindata = base64.b64encode(fo.read())
            self.image_medium = bindata
            return res
        return res


    @api.model
    def create(self, vals):
        product_templ = super(import_imagefrom_url, self).create(vals)
        if 'url_image' in vals and vals['url_image'] != '':
            temp_file, temp_header = urllib.request.urlretrieve(vals['url_image'])
            fo = open(temp_file, "rb")
            bindata = base64.b64encode(fo.read())
            self.image_medium = bindata
        return product_templ
