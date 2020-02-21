import frappe, os
from frappe import _
from autofill_indiazipcode import methods
from frappe.utils.nestedset import get_root_of
import json

@frappe.whitelist()
def get_by_pincode(pincode):
	result = {}
	zipcodes = frappe.get_all("India Zipcode", filters={"pincode":pincode}, fields=["*"])
	if not zipcodes:
		zipcodes_csv = methods.by_zipcode(pincode).to_json()
		if zipcodes_csv:
			docs = json.loads(zipcodes_csv)
			for officename in docs["pincode"]:
				if officename:
					doc = frappe.get_doc({
						"doctype": "India Zipcode",
						"officename": officename.replace(".O","O").replace("("," (") if officename else "",
						"pincode": docs["pincode"][officename],
						"officetype": docs["officeType"][officename].replace(".O","O") if docs["officeType"][officename] else "",
						"deliverystatus": docs["Deliverystatus"][officename],
						"divisionname": docs["divisionname"][officename],
						"regionname": docs["regionname"][officename],
						"circlename": docs["circlename"][officename],
						"taluk": docs["Taluk"][officename],
						"districtname": docs["Districtname"][officename],
						"statename": docs["statename"][officename].capitalize(),
						"telephone": docs["Telephone"][officename],
						"related_suboffice": docs["Related Suboffice"][officename].replace(".O","O") if docs["Related Suboffice"][officename] else "",
						"related_headoffice": docs["Related Headoffice"][officename].replace(".O","O") if docs["Related Headoffice"][officename] else "",
						"longitude": docs["longitude"][officename],
						"latitude": docs["latitude"][officename],
					})
					doc.flags.ignore_permissions = True
					doc.insert()
			frappe.db.commit()

		zipcodes = frappe.get_all("India Zipcode", filters={"pincode":pincode}, fields=["*"])
	
	if zipcodes:
		for d in zipcodes:
			result[d.officename] = d
	return result


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

	return True

@frappe.whitelist()
def on_update_address(doc, method):
	#save territory
	root_territory = get_root_of("Territory")
	if doc.country:
		insert_territory(doc.country, root_territory, 1)
		if doc.state:
			insert_territory(doc.state, doc.country, 1)				
			if doc.county:
				insert_territory(doc.county, doc.state, 1)
				if doc.post_office:
					insert_territory(doc.post_office, doc.county, 0)
	
	#save India Zipcode
	if doc.post_office and doc.postal_code and doc.county and doc.state:
		if not frappe.db.exists("India Zipcode", {"pincode":  doc.postal_code, "officename":  doc.post_office}):
			zipcode = frappe.get_doc({
				"doctype": "India Zipcode",
				"officename": doc.post_office,
				"pincode": doc.postal_code,
				"taluk": doc.taluk,
				"districtname": doc.county,
				"statename": doc.state,
			})
			zipcode.flags.ignore_permissions = True
			zipcode.insert()