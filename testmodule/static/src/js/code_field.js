/** @odoo-module **/
const {xml, Component} = owl;
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import {registry} from "@web/core/registry";
export class CodeField extends Component {
    setup() {
        // This setup is useless here because we don't do anything
        // But this is where you will use Hooks
        super.setup();
    }
}

CodeField.template = xml`<pre t-esc="props.value" class="bg-primary text-white p-3 rounded"/>`;
CodeField.props = standardFieldProps;

registry.category("fields").add("code2", CodeField);