odoo.define('testmodule.testmoule', function (require) {
    "use strict";
var AbstractField = require('web.AbstractField');
var core = require("web.core");
var registry = require("web.field_registry");

var UrlImage = AbstractField.extend({
// className: "o_field_image",
template: "FieldImageURL",
// placeholder: "/web/static/src/img/placeholder.png",
supportedFieldType: ['binary'],

url: function(){
    return this.value ? this.value: "";
},

url_not_thumbnail: function(){
    return this.value ? this.value.replaceAll('/thumbnail', ''):"";
},

_render:function(){
    this._super(arguments);
    var self = this;
    var $img = this.$("img:first");
},
});
registry.add('gm_image_href', UrlImage)
});