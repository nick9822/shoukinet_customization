// Copyright (c) 2019, GoElite and contributors
// For license information, please see license.txt

frappe.ui.form.on('Export Emails', {
	export: function(frm) {
		open_url_post('/api/method/shoukinet_customization.shoukinet_customization.doctype.export_emails.export_emails.export_emails_to_csv', {doc: frm.doc});
		// frappe.call({
		// 	method: "export_emails_to_csv",
		// 	doc: frm.doc,
		// 	callback: function(r) {
		// 		console.log(r);
		// 		console.log(frappe.response());
		// 		console.log("Export Started");
		// 	}
		// });
	}
});
