const { useState } = owl.hooks;
const { xml } = owl.tags;
const {Component} = owl;


class MyComponent extends Component {
    setup() {
        this.state = useState({ value: 1 });
    }

    increment() {
        this.state.value++;
    }
}
MyComponent.template = 'testmodule.MyComponent';