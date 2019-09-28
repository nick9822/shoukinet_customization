# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "shoukinet_customization"
app_title = "Shoukinet Customization"
app_publisher = "GoElite"
app_description = "Customzitaion for Shoukinet"
app_icon = "octicon octicon-settings"
app_color = "grey"
app_email = "contact@goelite.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/shoukinet_customization/css/shoukinet_customization.css"
# app_include_js = "/assets/shoukinet_customization/js/shoukinet_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/shoukinet_customization/css/shoukinet_customization.css"
# web_include_js = "/assets/shoukinet_customization/js/shoukinet_customization.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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
# get_website_user_home_page = "shoukinet_customization.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "shoukinet_customization.install.before_install"
# after_install = "shoukinet_customization.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "shoukinet_customization.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"shoukinet_customization.tasks.all"
# 	],
# 	"daily": [
# 		"shoukinet_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"shoukinet_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"shoukinet_customization.tasks.weekly"
# 	]
# 	"monthly": [
# 		"shoukinet_customization.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "shoukinet_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "shoukinet_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "shoukinet_customization.task.get_dashboard_data"
# }

