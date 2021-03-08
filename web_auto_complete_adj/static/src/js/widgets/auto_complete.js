odoo.define("web_auto_complete_adj.AutoComplete", function(require) {
    "use strict";

    var AutoComplete = require("web.AutoComplete");

    // QTL Edit
    // Apply "[FIX] web: update search view menu on click IME suggestion menu"
    // Ref: https://github.com/odoo/odoo/commit/6610b5d8fffe567b2dd7e4f45815eb4643defe83
    return AutoComplete.include({
        start: function() {
            var self = this;
            this.$input.on("compositionend", function() {
                self._isInputComposing = false;
            });
            this.$input.on("compositionstart", function() {
                self._isInputComposing = true;
            });
            this.$input.on("keyup", function(ev) {
                if (ev.which === $.ui.keyCode.RIGHT && !self._isInputComposing) {
                    self.searching = true;
                    ev.preventDefault();
                    return;
                }
                if (ev.which === $.ui.keyCode.ENTER && !self._isInputComposing) {
                    if (self.search_string.length) {
                        self.select_item(ev);
                    }
                    return;
                }
                self._updateSearch();
            });
            this.$input.on("input", function(ev) {
                if (ev.originalEvent.inputType === "insertCompositionText") {
                    // Click inside keyboard IME suggestions menu
                    self._updateSearch();
                }
            });
            this.$input.on("keypress", function(ev) {
                self.search_string += String.fromCharCode(ev.which);
                if (self.search_string.length) {
                    self.searching = true;
                    var search_string = self.search_string;
                    self.initiate_search(search_string);
                } else {
                    self.close();
                }
            });
            this.$input.on("keydown", function(ev) {
                if (self._isInputComposing) {
                    return;
                }
                switch (ev.which) {
                    case $.ui.keyCode.ENTER:
                    // TAB and direction keys are handled at KeyDown because KeyUp
                    // is not guaranteed to fire.
                    // See e.g. https://github.com/aef-/jquery.masterblaster/issues/13
                    case $.ui.keyCode.TAB:
                        if (self.search_string.length) {
                            self.select_item(ev);
                        }
                        break;
                    case $.ui.keyCode.DOWN:
                        self.move("down");
                        self.searching = false;
                        ev.preventDefault();
                        break;
                    case $.ui.keyCode.UP:
                        self.move("up");
                        self.searching = false;
                        ev.preventDefault();
                        break;
                    case $.ui.keyCode.RIGHT:
                        self.searching = false;
                        var current = self.current_result;
                        if (current && current.expand && !current.expanded) {
                            self.expand();
                            self.searching = true;
                        }
                        ev.preventDefault();
                        break;
                    case $.ui.keyCode.ESCAPE:
                        self.close();
                        self.searching = false;
                        break;
                }
            });
        },
        /**
         * Update search dropdown menu based on new input content.
         *
         * @private
         */
        _updateSearch: function() {
            var search_string = this.get_search_string();
            if (this.search_string !== search_string) {
                if (search_string.length) {
                    this.search_string = search_string;
                    this.initiate_search(search_string);
                } else {
                    this.close();
                }
            }
        },
    });
});
