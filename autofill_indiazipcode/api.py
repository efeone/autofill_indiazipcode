import frappe, os
from frappe import _
from autofill_indiazipcode import methods

@frappe.whitelist()
def get_by_zipcode(zipcode):
	return methods.by_zipcode(zipcode).to_json()