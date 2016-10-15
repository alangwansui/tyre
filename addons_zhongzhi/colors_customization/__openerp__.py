# -*- coding: utf-8 -*-
{
    'name': 'Customizable Interface',
    'version': '1.3',
    'category': 'Extra Tools',
    'summary': "Configure Odoo user interface and mails' styles. Remove branding and Odoo marketing spam in your database",
    'description': '''
Interface Customization
=======================
Individual users' interfaces and mail styles. Debranding. Replace Odoo bindings
-------------------------------------------------------------------------------
The app goal is to make your Odoo 9 interface (backend) customizable and to remove irritating branding. It allows configuring interface themes which let you:
* Apply your own styling and colors by each user individually
* Configure emails footer and links
* Replace branding of the Odoo interface and Odoo outgoing emails
Features
--------
* There may be an unlimited number of interface themes simultaneously
* Each theme is applied by each user individually. Thus, users may have different interface and user menu. If no theme is selected, default styling would be applied
* Let or forbid users to select existing interface themes through 'Preferences'. Anyway, a theme may be changed in a few clicks
* You may define a theme which would be default to all new users including portal users
* Themes may be added or changed only by user with the administrator rights.
Interface Styling
-----------------
* Define the top menu colors: background, border, font, active item font and background, hover font and background
* Define the left navigation panel colors: background, font, active item font and background, hover font and background
* Define the header section gradient colors for the background
* Redefine or fully remove the page title: e.g. "Inbox - Yourcompany" instead of "Inbox - Odoo"
* Replace the standard favicon by your own image
* Replace standard "Powered by Odoo" with your own footer or fully remove it. You may define footer's content, color and url.
User Menu
---------
You may configure user menu (top right corner) for each user individually:
* Hide or unhide the menu unit "Preferences"
* Hide or unhide the menu unit "About", including the Developer Mode functionality
* Hide or unhide the menu unit "My Odoo.com account"
* Hide or unhide the menu unit "Support"
* Hide or unhide the menu unit "Documentation"
Additional Features
-------------------
* Your Odoo doesn't call to Odoo.com and removes the message "Your Odoo is not supported" ("Your OpenERP is not supported")
* Instead of Odoo standard logo, empty image place holder is shown (in case there was no logo of a company)
* No reference to Odoo on a main page of login
* Redefine or replace email styles parts: "Sent by YourCompany using Odoo", "View in Odoo", "Follow"/"Unfollow" through Interface settings and the corresponding email template
    ''',
    'auto_install': False,
    'application':True,
    'price': '75.00',
    'currency': 'EUR',
    'author': 'IT Libertas',
    'website': 'http://itlibertas.com',
    'depends': [
        'base',
        'web',
        #'web_widget_color',
        'mail',
    ],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/include_css.xml',
        'views/colors_customization.xml',
        'views/res_company.xml',
        'views/interface_conf.xml',
        'views/no_knock_to_odoo.xml',
            ],
    'qweb': [
        'static/src/xml/*.xml',
            ],
    'js': [
            ],
    'demo': [

            ],
    'test': [

            ],
    'license': 'OEEL-1',
    'images': ['static/description/main.png'],
    'update_xml': [],
    'application':True,
    'installable': True,
    'private_category':False,
    'external_dependencies': {
    },

}
