
from besser.BUML.metamodel.gui import *

# Input Fields
nameInput: InputField = InputField(name="Name Input", fieldType="Text", validationRules="required")
emailInput: InputField = InputField(name="Email Input", fieldType="Email", validationRules="required")

# Button
addContactButton: Button = Button(name="Add Contact Button", label="Add Contact", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Form
personalInfoForm: Form = Form(name="Personal Information Form", inputFields={nameInput, emailInput})

# Data Source
contactListDataSource: ModelElement = ModelElement(name="Contact List Data Source", dataSourceClass=ContactListPage, fields={ContactListPage_userName, ContactListPage_email})

# List
contactList: DataList = DataList(name="Contact List", list_sources={contactListDataSource})

# Buttons
emptyButton: Button = Button(name="Empty Button", label="Empty", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)
saveButton: Button = Button(name="Save Button", label="Save", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)
loadButton: Button = Button(name="Load Button", label="Load", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Load)

# Screen
contactManagerScreen: Screen = Screen(
    name="Contact Manager Screen",
    view_elements={personalInfoForm, addContactButton, contactList, emptyButton, saveButton, loadButton},
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Large"
)

# Module
contactManagerModule: Module = Module(name="Contact Manager Module", screens={contactManagerScreen})

# Application
contactManagerApp: Application = Application(
    name="Contact Manager",
    package="com.example.contactmanager",
    versionCode="1",
    versionName="3.0",
    description="A contact management application.",
    screenCompatibility=True,
    modules={contactManagerModule}
)

# Class and Attributes
# This page is related to the ContactManagerPage class.
# Attributes of this class based on the structural model:
# - name: StringType
# - email: StringType

# Time taken to generate the structural model: 11.00 seconds

# Time taken to generate the GUI model: 28.77 seconds

# Total time taken: 39.77 seconds
