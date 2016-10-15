odoo.define('colors_customization.menu', function (require) {
"use strict";
var core = require('web.core');
var Dialog = require('web.Dialog');
var framework = require('web.framework');
var Model = require('web.DataModel');
var session = require('web.session');
var Widget = require('web.Widget');
var UserMenu = require('web.UserMenu');
var WebClient = require('web.WebClient');
var _t = core._t;
var QWeb = core.qweb;
var utils = require('web.utils');

    UserMenu.include({
        do_update: function () {
            var res = this._super.apply(this, arguments);
            
            var self = this;
            var fct = function() {
                var $avatar = self.$el.find('.oe_topbar_avatar');
                $avatar.attr('src', $avatar.data('default-src'));
                if (!session.uid)
                    return;
                var func = new Model("res.users").get_func("read");

                var Users = new Model('res.users');
                Users.query(['name'])
                    .filter([['id','=',self.session.uid]])
                    .first().then(function(user) {
                               var Themes =  new Model('colors.customization.theme');
                               Themes.query(['name','remove_menu_account','remove_menu_preferences','remove_menu_about','remove_menu_help','remove_menu_documentation'])
                                    .filter([['users','=',user.id]])
                                    .first().then(function(theme) {
                                        if (theme) {
                                            var $account_menu = self.$el.find("a[data-menu]");
                                            $account_menu.each(function(index,menu_obj){
                                                if (menu_obj.getAttribute('data-menu') == 'account'){
                                                    if(theme.remove_menu_account){
                                                        menu_obj.remove();
                                                    };
                                                };
                                                if (menu_obj.getAttribute('data-menu') == 'settings'){
                                                    if(theme.remove_menu_preferences){
                                                        menu_obj.remove();
                                                    };
                                                };                                            
                                                if (menu_obj.getAttribute('data-menu') == 'about'){
                                                    if(theme.remove_menu_about){
                                                        menu_obj.remove();
                                                    };
                                                }; 
                                                if (menu_obj.getAttribute('data-menu') == 'support'){
                                                    if(theme.remove_menu_help){
                                                        menu_obj.remove();
                                                    };
                                                };                                          
                                                if (menu_obj.getAttribute('data-menu') == 'documentation'){
                                                    if(theme.remove_menu_documentation){
                                                        menu_obj.remove();
                                                    };
                                                };    

                                            });
                                        };
                                    });
                            });

                return self.alive(func(self.session.uid, ["name", "company_id"])).then(function(res) {
                    var topbar_name = res.name;
                    if(session.debug)
                        topbar_name = _.str.sprintf("%s (%s)", topbar_name, session.db);
                    if(res.company_id[0] > 1)
                        topbar_name = _.str.sprintf("%s (%s)", topbar_name, res.company_id[1]);
                    self.$el.find('.oe_topbar_name').text(topbar_name);
                    if (!session.debug) {
                        topbar_name = _.str.sprintf("%s (%s)", topbar_name, session.db);
                    }
                    var avatar_src = self.session.url('/web/binary/image', {model:'res.users', field: 'image_small', id: self.session.uid});
                    $avatar.attr('src', avatar_src);

                    openerp.web.bus.trigger('resize');  // Re-trigger the reflow logic
                });
            };

            this.update_promise = this.update_promise.then(fct, fct);
        },    
    });


    WebClient.include({
        init: function(parent, client_options) {
            this._super(parent);
            if (client_options) {
                _.extend(this.client_options, client_options);
            }
            this._current_state = null;
            this.menu_dm = new utils.DropMisordered();
            this.action_mutex = new utils.Mutex();
            this.set('title_part', {"zopenerp": ""});


            var self = this;

            openerp.session.rpc("/web/session/get_session_info", {}).then(function(result) {
                if (result.uid) {
                        var Users = new Model('res.users');
                        Users.query(['name'])
                            .filter([['id','=',result.uid]])
                            .first().then(function(user) {
                                       var Themes =  new Model('colors.customization.theme');                               
                                       Themes.query(['name','meta_title'])
                                            .filter([['users','=',user.id]])
                                            .first().then(function(theme) {
                                                if (theme) {
                                                    if(theme.meta_title){
                                                       self.set('title_part', {"zopenerp": theme.meta_title});
                                                    };

                                                };
                                            });
                            });
                }
            
            }); 



        }, 

    

    }); 
});