
# Input fields
given_name_input = InputField(name="Given Name Input", description="Input for given name", fieldType="Text")
family_name_input = InputField(name="Family Name Input", description="Input for family name", fieldType="Text")
age_input = InputField(name="Age Input", description="Input for age", fieldType="Number")

# Button
add_to_contacts_button = Button(name="Add to Contacts Button", description="Button to add contact", label="Add to Contacts", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Form
contact_form = Form(name="Contact Form", description="Form to add a new contact", inputFields={given_name_input, family_name_input, age_input})

# Screen
contact_manager_screen = Screen(name="Contact Manager Screen", description="Screen for managing contacts", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={contact_form, add_to_contacts_button})

# Class and attributes
class_name = "ContactManager"
attributes = ["givenName", "familyName", "age", "phoneNumber", "address", "isActive", "birthDate", "email"]

# Time taken to generate the structural model: 8.94 seconds

# Time taken to generate the GUI model: 29.75 seconds

# Total time taken: 38.69 seconds
