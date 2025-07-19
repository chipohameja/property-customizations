import frappe
from erpnext_germany.erpnext_germany.doctype.business_letter.business_letter import BusinessLetter

class CustomBusinessLetter(BusinessLetter):
	def get_context(self):
		address = frappe.get_doc("Address", self.address) if self.address else None
		contact = frappe.get_doc("Contact", self.contact) if self.contact else None
		reference = frappe.get_doc(self.link_document_type, self.link_name) if self.link_name else None

		return {
			"address": address,
			"contact": contact,
			"reference": reference,
			"doc": self
		}