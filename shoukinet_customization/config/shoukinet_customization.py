from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
        {
            "label": _("Document"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Export Emails",
                    "label": _("Export Emails"),
                }
            ]
        }
    ]