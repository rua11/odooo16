/** @odoo-module **/

import {registry} from '@web/core/registry';
import {url} from '@web/core/utils/urls';
import {BinaryField} from '@web/views/fields/binary/binary_field';

export class VideoField extends BinaryField {
    get url() {
        return url('/web/content', {
            model: this.props.record.resModel,
            id: this.props.record.resId,
            field: this.props.name,
        })
    }

}

VideoField.template = 'web_widget_video.VideoField';
BinaryField.defaultProps = {
    acceptedFileExtensions: 'video/*',
};

registry.category('fields').add('video', VideoField);