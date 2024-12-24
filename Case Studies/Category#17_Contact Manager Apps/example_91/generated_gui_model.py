
from besser.BUML.metamodel.gui import *

# Input fields for the Contact Manager form
given_name_field = InputField(
    name="Given Name",
    description="Input field for given name",
    fieldType="Text",
    validationRules=""
)

family_name_field = InputField(
    name="Family Name",
    description="Input field for family name",
    fieldType="Text",
    validationRules=""
)

phone_number_field = InputField(
    name="Phone Number",
    description="Input field for phone number",
    fieldType="Tel",
    validationRules=""
)

# Form for adding a contact
contact_form = Form(
    name="Contact Form",
    description="Form to add a new contact",
    inputFields={given_name_field, family_name_field, phone_number_field}
)

# Button to add a contact
add_contact_button = Button(
    name="Add Contact Button",
    description="Button to add a new contact",
    label="Add Contact",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.SubmitForm
)

# Button to show the contact list
show_list_button = Button(
    name="Show List Button",
    description="Button to show the contact list",
    label="Show List",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.ShowList
)

# Screen for the Contact Manager
contact_manager_screen = Screen(
    name="Contact Manager Screen",
    description="Screen for managing contacts",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={contact_form, add_contact_button, show_list_button}
)

# Module containing the Contact Manager screen
contact_manager_module = Module(
    name="Contact Manager Module",
    screens={contact_manager_screen}
)

# Application definition
contact_manager_app = Application(
    name="Contact Manager App",
    package="com.example.contactmanager",
    versionCode="1",
    versionName="1.0",
    description="An application to manage contacts",
    screenCompatibility=True,
    modules={contact_manager_module}
)

# Class and attributes based on the structural model
# Class: ContactManager
# Attributes: createdDate, phoneNumber, givenName, emailAddress, lastUpdated, familyName, contactType, isFavorite

# Time taken to generate the structural model: 8.93 seconds

# Time taken to generate the GUI model: 29.73 seconds

# Total time taken: 38.66 seconds
