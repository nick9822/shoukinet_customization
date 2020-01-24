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
                },
                {
                    "type": "doctype",
                    "name": "Bulk Enquiry",
                    "label": _("Bulk Enquiry"),
                },
                {
                    "type": "doctype",
                    "name": "Request Customer Support",
                    "label": _("Request Customer Support"),
                },
                {
                    "type": "doctype",
                    "name": "Sell Used Cisco",
                    "label": _("Sell Used Cisco"),
                },
                {
                    "type": "doctype",
                    "name": "Choice Of Partner",
                    "label": _("Choice Of Partner"),
                },
                {
                    "type": "doctype",
                    "name": "Request for Quote",
                    "label": _("Request for Quote"),
                }
            ]
        }
    ]