// /** @odoo-module **/
// const {xml, Component} = owl;
// import { standardFieldProps } from "@web/views/fields/standard_field_props";
// import {registry} from "@web/core/registry";
// export class CodeField extends Component {
//     setup() {
//         // This setup is useless here because we don't do anything
//         // But this is where you will use Hooks
//         super.setup();
//     }
// }

// CodeField.template = "testmodule.CodeField";
// CodeField.props = standardFieldProps;

// registry.category("fields").add("code2", CodeField);

odoo.define('website_sale.video_field_preview1', function (require) {
    "use strict";
    
    var AbstractField = require('web.AbstractField');
    var core = require('web.core');
    var fieldRegistry = require('web.field_registry');
    
    var QWeb = core.qweb;
    /**
    * Displays preview of the video showcasing product.
    */
    var FieldVideoPreview = AbstractField.extend({
    className: 'd-block o_field_video_preview',
    
    _render: function () {
    this.$el.html(QWeb.render('productVideo', {
    embedCode: this.value,
    }));
    },
    });
    
    fieldRegistry.add('video_preview', FieldVideoPreview);
    
    return FieldVideoPreview;
    
    });