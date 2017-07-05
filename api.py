import frappe
@frappe.whitelist()
def send_invitation_emails(meeting):
	meeting = frappe.get_doc("Meeting",meeting)
	meeting.check_permission("email")
	import pdb
	pdb.set_trace()

	if meeting.status =="Planned":
		frappe.sendmail(
			recipients=[d.attendee for d in meeting.attendee],
			sender= frappe.session.user,
			subject=meeting.title,
			message =meeting.invitation_message,			
			reference_doctype=meeting.doctype,
			reference_name= meeting.name,
			)

		meeting.status=="Invitation Sent"
		meeting.save()
		frappe.msgprint(_("Invitation has been sent"))
	else:
		frappe.msgprint(_("Meeting Status must be planned to send the emails"))



