from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

sitemap = 1

def get_context(context):
	context.itm_grps = frappe.get_list("Item Group", fields=["name", "image", "route"], limit_page_length=9, order_by='weightage desc')
	context.title = "Shouki Electronics LLC - Cisco Channel Partner & Zycoo UAE Distributor"
	out = {
		"parents": [
			{ "name": _("Home"), "route": "/" }
		],
		"title" : "Shouki Electronics LLC - Cisco Channel Partner & Zycoo UAE Distributor"
	}

	return out