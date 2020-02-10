import frappe, os
from frappe import _
from autofill_indiazipcode import methods

@frappe.whitelist()
def get_by_pincode(pincode):
	return methods.by_zipcode(pincode).to_json()