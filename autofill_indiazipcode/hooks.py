# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "autofill_indiazipcode"
app_title = "Autofill Indiazipcode"
app_publisher = "iWEX Infomatics"
app_description = "Autofill India Zipcode"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "emails@iwex.in"
app_license = "MIT"

fixtures = [
	# "Territory",
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/autofill_indiazipcode/css/autofill_indiazipcode.css"
# app_include_js = "/assets/autofill_indiazipcode/js/autofill_indiazipcode.js"

# include js, css files in header of web template
# web_include_css = "/assets/autofill_indiazipcode/css/autofill_indiazipcode.css"
# web_include_js = "/assets/autofill_indiazipcode/js/autofill_indiazipcode.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Address" : "custom_scripts/address_custom.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "autofill_indiazipcode.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "autofill_indiazipcode.install.before_install"
# after_install = "autofill_indiazipcode.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "autofill_indiazipcode.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
	"Address": {
		"on_update": "autofill_indiazipcode.api.on_update_address",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"autofill_indiazipcode.tasks.all"
# 	],
# 	"daily": [
# 		"autofill_indiazipcode.tasks.daily"
# 	],
# 	"hourly": [
# 		"autofill_indiazipcode.tasks.hourly"
# 	],
# 	"weekly": [
# 		"autofill_indiazipcode.tasks.weekly"
# 	]
# 	"monthly": [
# 		"autofill_indiazipcode.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "autofill_indiazipcode.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "autofill_indiazipcode.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "autofill_indiazipcode.task.get_dashboard_data"
# }

