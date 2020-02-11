import frappe, os
from frappe import _
from autofill_indiazipcode import methods
from frappe.utils.nestedset import get_root_of

@frappe.whitelist()
def get_by_pincode(pincode):
	return methods.by_zipcode(pincode).to_json()

@frappe.whitelist()
def insert_territory(territory_name, parent_territory, is_group):
	if not frappe.db.exists("Territory", territory_name):
		territory = frappe.get_doc({
			"doctype": "Territory",
			"territory_name": territory_name,
			"parent_territory": parent_territory,
			"is_group": is_group
		})
		territory.flags.ignore_permissions = True
		territory.insert()
		return frappe.get_doc("Territory", territory_name)
	else:
		return frappe.get_doc("Territory", territory_name)


@frappe.whitelist()
def on_update_address(doc, method):
	root_territory = get_root_of("Territory")
	if doc.country:
		insert_territory(doc.country, root_territory, 1)
		if doc.state:
			insert_territory(doc.state, doc.country, 1)				
			if doc.county:
				insert_territory(doc.county, doc.state, 1)
				if doc.post_office:
					insert_territory(doc.post_office, doc.county, 0)