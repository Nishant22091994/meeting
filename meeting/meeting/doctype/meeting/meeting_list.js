frappe.listview_settings['Meeting'] = {

	get_indicator: function(doc) {
		return[__(doc.status),{
			"Planned":"orange",
			"Invitation Sent":"blue",
			"In porgress":"darygrey",
			"Completed":"green",
			"Cancelled":"red",
		}[doc.status], "status,=," + doc.status];
	}
};
