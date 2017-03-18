# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.web.models.ir_http import Http


class Http(Http):

    def webclient_rendering_context(self):
        result = super(Http, self).webclient_rendering_context()
        background = self.env['ir.config_parameter'].get_param(
            'maintenance_banner.background')
        content = self.env['ir.config_parameter'].get_param(
            'maintenance_banner.content')
        height = self.env['ir.config_parameter'].get_param(
            'maintenance_banner.height')
        show_banner = self.env['ir.config_parameter'].get_param(
            'maintenance_banner.show_banner')
        show_banner = str(show_banner).strip().lower()

        banner_data = {
            'background': background,
            'content': content,
            'height': height,
            'show_banner': 'yes' if show_banner == 'true' else show_banner,
        }
        result.update({'banner_data': banner_data})
        return result
