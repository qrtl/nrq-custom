Besides installing this module, you need to add it to your addons, and load it as a server-wide module.

This can be done with the server_wide_modules parameter in /etc/odoo.conf or with the --load command-line parameter
Please put this module before the web module as core api method will be monkey patched.

server_wide_modules = "use_activity_log,web"
