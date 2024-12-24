
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="contact_management", description="Manage your contacts efficiently")

# Input Fields
nameInput: InputField = InputField(name="Name Input", description="Enter contact name", fieldType="Text", validationRules="")
emailInput: InputField = InputField(name="Email Input", description="Enter contact email", fieldType="Email", validationRules="")

# Form
contactForm: Form = Form(name="Contact Form", description="Form to add new contact", inputFields={nameInput, emailInput})

# Buttons
addContactButton: Button = Button(name="Add Contact Button", description="Add a new contact", label="Add new Contact", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)
exportButton: Button = Button(name="Export Button", description="Export contacts to Excel", label="Export to Excel", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Export)

# Search Field
searchInput: InputField = InputField(name="Search Input", description="Search for names", fieldType="Search", validationRules="")

# Data Source
contactDataSource: ModelElement = ModelElement(name="Contact Data Source", dataSourceClass=ContactList, fields={ContactList_contactName, ContactList_contactEmail})

# List
contactList: DataList = DataList(name="Contact List", description="List of contacts", list_sources={contactDataSource})

# Screen definition
contactScreen: Screen = Screen(name="Contact Management Screen", description="Screen to manage contacts",
                               x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={contactForm, addContactButton, exportButton, searchInput, contactList})

# Module definition
contactModule: Module = Module(name="Contact Module", screens={contactScreen})

# Application definition
contactApp: Application = Application(name="Contact Management App", package="com.example.contactmanagement", versionCode="1",
                                      versionName="1.0", description="An application to manage contacts", screenCompatibility=True, modules={contactModule})

# Class and Attributes
# This page is related to the class: ContactPage
# Attributes of this class: name, email

# Time taken to generate the structural model: 9.52 seconds

# Time taken to generate the GUI model: 148.24 seconds

# Total time taken: 157.76 seconds
