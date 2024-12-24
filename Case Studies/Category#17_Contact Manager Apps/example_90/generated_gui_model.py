
from library import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="contact_component", description="Contact Management Interface")

# Input Fields
nameInput: InputField = InputField(name="Name Input", description="Enter contact name", fieldType="Text", validationRules="")
emailInput: InputField = InputField(name="Email Input", description="Enter contact email", fieldType="Email", validationRules="")

# Form
contactForm: Form = Form(name="Contact Form", description="Form to add new contact", inputFields={nameInput, emailInput})

# Button
addContactButton: Button = Button(name="Add Contact Button", description="Add new contact", label="Add new Contact", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# DataSource
datasource_contact: ModelElement = ModelElement(name="Contact Data Source", dataSourceClass=ContactList, fields=[ContactList_name, ContactList_email])

# List
contactList: DataList = DataList(name="Contact List", description="List of contacts", list_sources={datasource_contact})

# Buttons
emptyButton: Button = Button(name="Empty Button", description="Empty the list", label="Empty", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Delete)
saveButton: Button = Button(name="Save Button", description="Save the list", label="Save", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Save)
loadButton: Button = Button(name="Load Button", description="Load the list", label="Load", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Load)
sortButton: Button = Button(name="Sort Button", description="Sort the list", label="Sort", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Sort)

# Input Field for Search
searchInput: InputField = InputField(name="Search Input", description="Search the list", fieldType="Search", validationRules="")

# Screen definition
ContactScreen: Screen = Screen(name="Contact Management Screen", description="Screen for managing contacts",
                               x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                               view_elements={contactForm, addContactButton, contactList, emptyButton, saveButton, loadButton, sortButton, searchInput})

# Module definition
ContactModule: Module = Module(name="Contact Module", screens={ContactScreen})

# Application definition
ContactApp: Application = Application(name="Contact Management App", package="com.example.contactmanagement", versionCode="1",
                                      versionName="1.0", description="An application for managing contacts.",
                                      screenCompatibility=True, modules={ContactModule})

# Class and Attributes
# This page is related to the class: ContactList
# Attributes of this class: name, email

# Time taken to generate the structural model: 7.17 seconds

# Time taken to generate the GUI model: 30.22 seconds

# Total time taken: 37.38 seconds
