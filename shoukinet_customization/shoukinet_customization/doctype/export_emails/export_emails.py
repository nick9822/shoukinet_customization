# -*- coding: utf-8 -*-
# Copyright (c) 2019, GoElite and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import re, csv, os
from frappe.model.document import Document
from frappe.utils.csvutils import UnicodeWriter
from frappe.utils import cstr, formatdate, format_datetime, parse_json, cint

@frappe.whitelist()
def export_emails_to_csv(doc):
	exporter = ExportEmailsCls(doc)
	exporter.export_emails_to_csv()

class ExportEmails(Document):
	pass	

class ExportEmailsCls(Document):
	def __init__(self, doc):
		self.doc = parse_json(doc)
	
	def export_emails_to_csv(self):
		switcher = { "Lead": self.export_leads, "Customer": self.export_customers, "Supplier": self.export_suppliers }
		func = switcher.get(self.doc.export_from, self.invalid_export)
		return func()
	
	def invalid_export(self):
		frappe.throw("Invalid Document! Please contact Adminstrator")

	def export_leads(self):
		self.writer = UnicodeWriter()
		lead_list = frappe.get_list("Lead", fields=["name", "lead_name", "company_name", "email_id"])
		self.writer.writerow(["name", "company_name", "email"])
		for e in lead_list:
			if e.email_id:
				self.writer.writerow([e.lead_name, e.company_name, e.email_id])
		self.build_response_as_csv()
	
	def export_customers(self):
		self.writer = UnicodeWriter()
		group = self.doc.customer_group or "All Customer Groups"
		customer_list = frappe.db.sql("""
						select
							customer.customer_name,
							contact.first_name,
							contact.last_name,
							contact.email_id
						from
							`tabCustomer` customer,
							`tabContact` contact,
							`tabDynamic Link` contact_dyn_link
						where
							customer.customer_group = '{0}'
							and contact_dyn_link.parent = contact.name
							and contact_dyn_link.link_doctype = "Customer"
							and contact_dyn_link.link_name = customer.name
					""".format(group), as_dict=True)
		self.writer.writerow(["name", "company_name", "email"])
		for e in customer_list:
			if e.email_id:
				self.writer.writerow(["{0} {1}".format(e.first_name, e.last_name) if e.last_name else e.first_name, e.customer_name, e.email_id])
		self.build_response_as_csv()
	
	def export_suppliers(self):
		self.writer = UnicodeWriter()
		group = self.doc.supplier_group or "All Supplier Groups"
		supplier_list = frappe.db.sql("""
						select
							supplier.supplier_name,
							contact.first_name,
							contact.last_name,
							contact.email_id
						from
							`tabSupplier` supplier,
							`tabContact` contact,
							`tabDynamic Link` contact_dyn_link
						where
							supplier.supplier_group = '{0}'
							and contact_dyn_link.parent = contact.name
							and contact_dyn_link.link_doctype = "Supplier"
							and contact_dyn_link.link_name = supplier.name
					""".format(group), as_dict=True)
		self.writer.writerow(["name", "company_name", "email"])
		for e in supplier_list:
			if e.email_id:
				self.writer.writerow(["{0} {1}".format(e.first_name, e.last_name) if e.last_name else e.first_name, e.supplier_name, e.email_id])
		self.build_response_as_csv()

	def build_response_as_excel(self):
		filename = frappe.generate_hash("", 10)
		with open(filename, 'wb') as f:
			f.write(cstr(self.writer.getvalue()).encode('utf-8'))
		f = open(filename)
		reader = csv.reader(f)

		from frappe.utils.xlsxutils import make_xlsx
		xlsx_file = make_xlsx(reader, 'Data Export')

		f.close()
		os.remove(filename)

		# write out response as a xlsx type
		frappe.response['filename'] = self.doc.export_from + '.xlsx'
		frappe.response['filecontent'] = xlsx_file.getvalue()
		frappe.response['type'] = 'binary'
	
	def build_response_as_csv(self):
		frappe.response['result'] = cstr(self.writer.getvalue())
		frappe.response['type'] = 'csv'
		frappe.response['doctype'] = self.doc.export_from