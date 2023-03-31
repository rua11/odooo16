odoo.define('muk_preview_markdown.PreviewContentVideo', function (require) {
    "use strict";
    
    var core = require('web.core');
    var ajax = require('web.ajax');
    var utils = require('web.utils');
    var session = require('web.session');
    
    var registry = require('muk_preview.registry');
    
    var AbstractPreviewContent = require('muk_preview.AbstractPreviewContent');
    
    var QWeb = core.qweb;
    var _t = core._t;
    
    var PreviewContentVideo = AbstractPreviewContent.extend({
        template: "muk_preview.PreviewContentVideo",    
        mimetypeMap: {
            '.mp4': 'video/mp4', '.webm': 'video/webm', '.ogg': 'video/ogg',
            'mp4': 'video/mp4', 'webm': 'video/webm', 'ogg': 'video/ogg',
        },
        init: function(parent, url, mimetype, filename) {
            this._super.apply(this, arguments);
            if(this.mimetype === 'application/octet-stream') {
                var extension = this.filename.split('.').pop();
                this.mimetype = this.mimetypeMap[extension];
            }
        },
        downloadable: true,
        printable: false,
    });
    
    _.each(['.mp4', '.webm', '.ogg'], function(extension) {
        registry.add(extension, PreviewContentVideo);
    });
    _.each(['mp4', 'webm', 'ogg'], function(extension) {
        registry.add(extension, PreviewContentVideo);
    });
    _.each(['video/mp4', '	video/webm', 'video/ogg'], function(mimetype) {
        registry.add(mimetype, PreviewContentVideo);
    });
    
    return PreviewContentVideo;
    
    });
    