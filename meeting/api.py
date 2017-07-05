import frappe
from frappe import _
from frappe.utils import add_days,nowdate

@frappe.whitelist()
def send_invitation_emails(meeting):
	meeting = frappe.get_doc("Meeting",meeting)
	meeting.check_permission("email") 

	if meeting.status =="Planned":
		frappe.sendmail(
			recipients=[d.attendee for d in meeting.attendee],
			sender= frappe.session.user,
			subject=meeting.title,
			message =meeting.invitation_message,			
			reference_doctype=meeting.doctype,
			reference_name= meeting.name,
			# as_bulk =True
			)

		meeting.status=="Invitation Sent"
		meeting.save()
		frappe.msgprint(_("Invitation has been sent"))
	else:
		frappe.msgprint(_("Meeting Status must be planned to send the emails"))


@frappe.whitelist()
def get_meetings(start,end):
	if not frappe.has_permission("Meeting","read"):
		raise frappe.PermissionError

	data = frappe.db.sql(""" select 
		timestamp(date,from_time) as start,
		timestamp(date,totime) as end,
		name,
		title,
		status,
		0 as all_day
		from `tabMeeting`
		where `date` between %(start)s and %(end)s""",
		{
		'start':start,
		'end':end
		},as_dict=True)
	print "checking datda--------", data
	return data

def make_orientation_meeting(doc,method):
	import pdb
	pdb.set_trace()

	meeting_doc = frappe.new_doc("Meeting")
	# meeting_doc.doctype="Meeting"
	meeting_doc.title="Orientation for {0}".format(doc.first_name)
	meeting_doc.append("agenda_section",{
		"description":"Orientation day "
	})
	meeting_doc.date=add_days(nowdate(),1)
	meeting_doc.from_time="09:00"
	meeting_doc.to_time="09:00"
	meeting_doc.status="Planned"
	meeting_doc.attendee=[]
	
	meeting_doc.save()
		
	# meeting_doc.flags.ignore_permission = True

	# meeting.insert()

	frappe.msgprint(_("Orientation Meeting created"))
