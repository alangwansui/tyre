# -*- coding: utf-8 -*-

from openerp import models, fields, api, _, tools


class color_theme(models.Model):
    _name = 'colors.customization.theme'

    def _get_properties(self):
        return [
            ('nav.navbar-inverse', 'background-color', self.navbar_color),
            ('nav.navbar-inverse', 'border-color', self.navbar_border_color),
            ('.navbar-inverse .navbar-nav > li > a', 'color', self.menu_font_color),
            ('.navbar-inverse .navbar-nav > .active > a,  .navbar-inverse .navbar-nav > .active > a:focus', 'color', self.navbar_active_item_font_color),
            ('.navbar-inverse .navbar-nav > li.active > a', 'background-color', self.menu_active_item_color),
            ('.navbar-inverse .navbar-nav > li > a:hover', 'color', self.navbar_hover_font_color),
            ('.navbar-inverse .navbar-nav > li > a:hover', 'background-color', self.navbar_hover_background_color),
            ('.oe_leftbar', 'background', self.left_bar_color),
            ('.nav-pills li > a', 'color', self.left_bar_font_color),
            ('.oe_secondary_menu_section', 'color', self.left_bar_category_font_color),

            ('.oe_secondary_menu_section > .oe_menu_leaf > .oe_menu_text','color',self.left_bar_menu_text),

            ('.nav-pills > li.active > a', 'background-color', self.left_bar_active_item_color),
            ('.nav-pills > li.active > a', 'color', self.left_bar_active_item_font_color),
            ('.nav-pills > li > a:hover', 'color', self.left_bar_hover_font_color),
            ('.nav-pills > li > a:hover', 'background-color', self.left_bar_hover_background_color),

            ('.openerp .oe-control-panel', 'background-color', self.header_table_color),
            ('.openerp .oe-control-panel', 'background-image', self.webkit_gradient),
            ('.openerp .oe-control-panel', 'background-image', self.linear_gradient),
            ('.openerp .oe-control-panel', 'background-image', self.moz_gradient),
            ('.openerp .oe-control-panel', 'background-image', self.ms_gradient),  
            ('.openerp .oe-control-panel', 'background-image', self.lin_gradient),
            ('.openerp .oe-control-panel', 'background-image', self.gradient_bot),

        ]

    def _build_rule(self, selector, prop, value):
        return "{s} {{ {p}: {v} !important;}}\n".format(s=selector, p=prop, v=value)

    @api.depends('navbar_color', 'navbar_border_color',
        'menu_font_color', 'left_bar_color',
        'menu_active_item_color','left_bar_menu_text',
        'navbar_hover_font_color','navbar_hover_background_color',
        'left_bar_font_color', 'left_bar_category_font_color',
        'left_bar_active_item_color', 'navbar_active_item_font_color',
        'left_bar_active_item_font_color',
        'left_bar_hover_font_color','left_bar_hover_background_color',
        'header_table_color','header_table_color_2',)
    def _get_css(self):
        result = ''
        for field in self._get_properties():
            result += self._build_rule(field[0], field[1], field[2])
        self.css = result

    name = fields.Char('Name',required=True,translate=True)
    css = fields.Char(compute='_get_css', store=True, string="CSS")
    
    navbar_color = fields.Char('Background Color')
    navbar_border_color = fields.Char('Border Color')
    navbar_active_item_font_color = fields.Char('Active Item Font Color')
    menu_font_color = fields.Char('Font Color')
    menu_active_item_color = fields.Char('Active Item Background Color')
    navbar_hover_font_color = fields.Char('Hover Font Color')
    navbar_hover_background_color = fields.Char('Hover Background Color')

    left_bar_color = fields.Char('Background Color')
    left_bar_menu_text = fields.Char('Individual Menu Color')

    left_bar_font_color = fields.Char('Sub Menu Color')
    left_bar_category_font_color = fields.Char('Main Menu Color')
    left_bar_active_item_font_color = fields.Char('Active Item Font Color')
    left_bar_active_item_color = fields.Char('Active Item Background Color')
    left_bar_hover_font_color = fields.Char('Hover Font Color')
    left_bar_hover_background_color = fields.Char('Hover Background Color')

    @api.one
    def get_header_gradient_webkit(self):
        if self.header_table_color and self.header_table_color_2:
            self.webkit_gradient = '-webkit-gradient(linear, left top, left bottom, from('+self.header_table_color+'), to('+self.header_table_color_2+'))'
            self.linear_gradient ='-webkit-linear-gradient(top, '+self.header_table_color+', '+self.header_table_color_2+')'
            self.moz_gradient = '-moz-linear-gradient(top,'+self.header_table_color+', '+self.header_table_color_2+')'
            self.ms_gradient = '-ms-linear-gradient(top,'+self.header_table_color+', '+self.header_table_color_2+')'
            self.lin_gradient = '-o-linear-gradient(top,'+self.header_table_color+', '+self.header_table_color_2+')'
            self.gradient_bot = 'linear-gradient(to bottom,'+self.header_table_color+', '+self.header_table_color_2+')'
        else:
            self.webkit_gradient = self.linear_gradient = self.moz_gradient = self.ms_gradient = self.lin_gradient = self.gradient_bot = False


    header_table_color = fields.Char('Header Section Background (Gradient)')
    header_table_color_2 = fields.Char('Header Section Background 2')
    webkit_gradient = fields.Char('Gradient',compute='get_header_gradient_webkit')
    linear_gradient = fields.Char('Gradient',compute='get_header_gradient_webkit')
    moz_gradient = fields.Char('Gradient',compute='get_header_gradient_webkit')
    ms_gradient = fields.Char('Gradient',compute='get_header_gradient_webkit')
    lin_gradient = fields.Char('Gradient',compute='get_header_gradient_webkit')
    gradient_bot =  fields.Char('Gradient',compute='get_header_gradient_webkit')


    @api.one
    def assign_to_all_users(self):
        for user in self.env['res.users'].search([]):
            user.company_color_theme = self

    users = fields.One2many('res.users','company_color_theme',string='Users',help='Only one theme may be specified to a user')

    @api.one
    def change_default_theme(self):
        if self.default_for_new_users:
            for theme in self.search([('id','!=',self.id)]):
                theme.default_for_new_users = False

    default_for_new_users = fields.Boolean(string='Default',inverse='change_default_theme',help='This theme would be applied to new users. There could be only one default theme')

    @api.one
    @api.depends('image')
    def _get_image(self):
        images =  tools.image_get_resized_images(self.image)
        self.image_small =  images.get('image_small')
        self.image_medium =  images.get('image_medium')


    image = fields.Binary(string='Favicon')
    image_medium = fields.Binary(compute='_get_image',store=True,string='Image Medium')
    image_small = fields.Binary(compute='_get_image',store=True,string='Image Small')

    @api.one
    @api.depends('image_small')
    def get_image_small_url(self):
        self.url_favicon = "web/binary/image?model=colors.customization.theme&id="+ str(self.id) +"&field=image_small"


    url_favicon = fields.Char(compute='get_image_small_url')

    footer_text = fields.Char(string='Footer', help='Leave it empty to delete a footer at all',translate=True)
    footer_url = fields.Char(string='URL',help='Use http or https to have an absolute url')
    footer_color = fields.Char(string='Color')

    remove_menu_preferences = fields.Boolean(string='Hide Preferences',help='From the user menu',default=False)
    remove_menu_account = fields.Boolean(string='Hide Account',help='From the user menu',default=True)
    remove_menu_help = fields.Boolean(string='Hide Support',help='From the user menu',default=True)
    remove_menu_about = fields.Boolean(string='Hide Deveoper Mode (About)',help='From the user menu',default=False)
    remove_menu_documentation = fields.Boolean(string='Hide Documentation',help='From the user menu',default=False)

    meta_title = fields.Char(string='Page Title',help='Instead of Odoo')

    _order = 'id' 



