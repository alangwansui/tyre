Requirements and exceptions
===========================
* Before installing the app uninstall the modules which modify Odoo web templates: e.g. remove some branding or styling. Potential contradiction may appear
* In some Odoo versions this app's installation may lead to Odoo users' group bug (users form are not opened or menus are broken). In that case just update the 'base' module
* The module depends on web and mail modules. Besides, it it depends on the module web_widget_color to use color picker options (the feature woule be available as soon as merge request by OCA would be accepted)
* Find themes under the menu unit Settings > Interface > Themes