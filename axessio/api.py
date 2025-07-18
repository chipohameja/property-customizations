import frappe
from frappe import _

@frappe.whitelist()
def get_rendered_template(doc, reference, message):
    """
    Renders a template with the given document and reference.
    :param doc: The doctype of the document to be rendered.
    :param reference: The reference ID of the document.
    :param message: The template message to be rendered.
    :return: A dictionary containing the rendered message and document details."""
    if doc and reference:
        try:
            doc_record = frappe.get_doc(doc, reference)

            context = {
                "doc": doc_record.as_dict()
            }
            
            rendered_message = frappe.render_template(message, context)

            response = {
                "message": rendered_message,
                "doctype": doc,
                "reference": reference
            }

            return response

        except frappe.DoesNotExistError:
            response = (_("Document {0} with reference {1} does not exist.").format(doc, reference))
            return response
        except Exception as e:
            response = (_("An error occurred while rendering the template: {0}").format(str(e)))
            return response
