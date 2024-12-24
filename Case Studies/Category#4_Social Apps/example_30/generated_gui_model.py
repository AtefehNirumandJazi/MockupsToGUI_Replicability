
from besser.BUML.metamodel.gui import *

# Input Fields
nameField: InputField = InputField(name="Name", description="Enter your name", fieldType="Text", validationRules="")
contactField: InputField = InputField(name="Contact", description="Enter your contact number", fieldType="Tel", validationRules="")
emailField: InputField = InputField(name="Email", description="Enter your email address", fieldType="Email", validationRules="")

# Dropdown List
categoryList: List = List(name="Inquiry Category", description="Select Inquiry Category", list_sources=set())

# Text Area
detailsField: InputField = InputField(name="Inquiry Details", description="Enter inquiry details", fieldType="Text", validationRules="")

# Button
sendButton: Button = Button(name="Send Message", description="Send the inquiry message", label="Send Message", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Send)

# Form
inquiryForm: Form = Form(name="Inquiry Form", description="Form to submit inquiries", inputFields={nameField, contactField, emailField, detailsField, categoryList})

# Screen
inquiryScreen: Screen = Screen(name="Inquiry Screen", description="Screen for submitting inquiries", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={inquiryForm, sendButton})

# Class and Attributes
# This page is related to the "InquiryForm" class in the structural model.
# Attributes of this class based on the structural model:
# - name
# - category
# - contactNumber
# - details
# - emailAddress

# Time taken to generate the structural model: 7.76 seconds

# Time taken to generate the GUI model: 20.73 seconds

# Total time taken: 28.48 seconds
