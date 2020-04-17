/* Copyright 2018 Quartile Limited
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl). */

odoo.define("web_responsive_disable_search.web_responsive", function(require) {
  "use strict";

  var web_responsive = require("web_responsive");

  web_responsive.AppDrawer.include({
    redirectKeyPresses: function(e) {
      if (!this.isOpen) {
        // Drawer isn't open; Ignore.
        return;
      }

      // Trigger navigation to pseudo-focused link
      // & fake a click (in case of anchor link).
      if (e.key === "Enter") {
        window.location.href = $(".web-responsive-focus").attr("href");
        this.handleClickZones();
        return;
      }

      // Ignore any other modifier keys.
      if (this.MODIFIERS.indexOf(e.key) !== -1) {
        return;
      }

      // Event is already targeting the search input.
      // Perform search, then stop processing.
      if (e.target === this.$searchInput[0]) {
        this.searchMenus();
        return;
      }

      // Prevent default event,
      // redirect it to the search input,
      // and search.
      //Commented below code for disable auto search
      // feature on keypress

      /*e.preventDefault();
            this.$searchInput.trigger({
                type: e.type,
                key: e.key,
                keyCode: e.keyCode,
                which: e.which,
            });
            this.searchMenus(); */
    }
  });
});
