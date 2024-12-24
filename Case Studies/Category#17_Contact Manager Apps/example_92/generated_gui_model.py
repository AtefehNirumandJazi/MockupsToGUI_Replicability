
from besser.BUML.metamodel.gui import *

# Input Fields
firstNameField = InputField(name="First Name", description="Enter first name", fieldType="Text")
lastNameField = InputField(name="Last Name", description="Enter last name", fieldType="Text")
phoneNumberField = InputField(name="Phone Number", description="Enter phone number", fieldType="Tel")

# Submit Button
submitButton = Button(name="Submit Contact", description="Submit contact information", label="Submit Contact", buttonType=ButtonType.TextButton, actionType=ButtonActionType.SubmitForm)

# Form
contactForm = Form(name="Contact Form", description="Form to add a new contact", inputFields={firstNameField, lastNameField, phoneNumberField})

# Data Source
contactDataSource = ModelElement(name="Contact Data Source", dataSourceClass=ContactManager, fields={ContactManager_firstName, ContactManager_lastName, ContactManager_phoneNumber})

# List
contactList = DataList(name="Contact List", description="List of contacts", list_sources={contactDataSource})

# Clear Table Button
clearTableButton = Button(name="Clear Table", description="Clear the contact table", label="Clear Table", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Delete)

# Screen
contactManagerScreen = Screen(name="Contact Manager", description="Manage contacts", x_dpi="x_dpi", y_dpi="y_dpi", size="Large", view_elements={contactForm, submitButton, contactList, clearTableButton})

# Module
contactModule = Module(name="Contact Module", screens={contactManagerScreen})

# Application
contactApp = Application(name="Contact Manager App", package="com.example.contactmanager", versionCode="1", versionName="1.0", description="An application to manage contacts", screenCompatibility=True, modules={contactModule})

# Class and Attributes
# This page is related to the ContactManager class.
# Attributes: firstName, lastName, phoneNumber, createdDate, emailAddress, lastUpdated, contactType, isFavorite

# Time taken to generate the structural model: 8.02 seconds

# Time taken to generate the GUI model: 76.04 seconds

# Total time taken: 84.06 seconds
