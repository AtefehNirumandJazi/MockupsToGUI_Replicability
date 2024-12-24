
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="contact_manager_component", description="Contact Manager Form")

# Input Fields
givenNameField: InputField = InputField(name="Given Name", description="Enter given name", fieldType="Text", validationRules="")
familyNameField: InputField = InputField(name="Family Name", description="Enter family name", fieldType="Text", validationRules="")
ageField: InputField = InputField(name="Age", description="Enter age", fieldType="Number", validationRules="")

# Button
addButton: Button = Button(name="Add to Contacts", description="Add contact to list", label="Add to contacts", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Form
contactForm: Form = Form(name="Contact Form", description="Form to add contact details", inputFields={givenNameField, familyNameField, ageField})

# Screen definition
ContactManagerScreen: Screen = Screen(name="Contact Manager Screen", description="Screen for managing contacts",
                                      x_dpi="x_dpi", y_dpi="y_dpi", size="Large", view_elements={contactForm, addButton})

# Module definition
ContactManagerModule: Module = Module(name="Contact Manager Module", screens={ContactManagerScreen})

# Application definition
ContactManagerApp: Application = Application(name="Contact Manager App", package="com.example.contactmanager", versionCode="1",
                                             versionName="1.0", description="An application to manage contacts",
                                             screenCompatibility=True, modules={ContactManagerModule})

# Class and attributes
# This page is related to the "ContactManager" class in the structural model.
# Attributes of the ContactManager class:
# - givenName
# - familyName
# - age
# - email
# - isActive
# - phoneNumber
# - createdAt
# - address
# - updatedAt
# - dateOfBirth

# Time taken to generate the structural model: 7.78 seconds

# Time taken to generate the GUI model: 19.04 seconds

# Total time taken: 26.82 seconds
