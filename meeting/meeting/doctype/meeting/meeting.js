 // Copyright (c) 2017, NC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Meeting',{
	send_email:function(frm)
	{
		// alert("Hii")
		if(frm.doc.status==="Planned")
		{
			frappe.call
			({
				method:"meeting.api.send_invitation_emails",
				args:
				{
					meeting : frm.doc.name
				},
			});
		}
	},

});


frappe.ui.form.on('Meeting Attendee', 
{
	// console.log("Go");
	attendee: function(frm,cdt,cdn) 
	{
		var attendee = locals[cdt][cdn];
		
		if (attendee.attendee)
		{
			frappe.call({
				method:"meeting.meeting.doctype.meeting.meeting.get_full_name",
				args:{
					attendee: attendee.attendee
					},
			callback :function(r) 
			{
				frappe.model.set_value(cdt,cdn,"name1",r.message);
				// refresh_field('name1')
			}	
					});
		}
		else{
			frappe.model.set_value(cdt,cdn,"name1",null);
			}

	}

})


