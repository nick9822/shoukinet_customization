from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

sitemap = 1

def get_context(context):
	out = {
		"parents": [
			{ "name": _("Home"), "route": "/" }
		]
	}

	return out