odoo.define('testmodule.testmodule', function(require){
    'use strict'
    console.log('popup.js loaded');
    var FormController = require('web.FormController');
    console.log('1');
    var ExtendFormController = FormController.include({
    saveRecord: function() {
        console.log('saveRecord');
        var res = this._super.apply(this,arguments);
        // if (this.modelName == 'dog'){
        //     this.do_notify('Success, Record saved')
        //     self = this
        //     self._rpc({
        //         model: "testmodule",
        //         method: "search_read",
        //         fields: ["name", "number_of_vides"],
        //         context: self.context,
        //     }).then(function(result){
        //         console.log(result)
        //     })
        console.log('2');
        return res;

        }
    });
    console.log('3')
});
