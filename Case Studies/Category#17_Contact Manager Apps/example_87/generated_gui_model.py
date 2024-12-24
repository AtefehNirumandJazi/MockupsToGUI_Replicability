
# Menu definition
menu = Menu(
    name="Main Menu",
    description="Navigation menu",
    menuItems={
        MenuItem(label="Show all Contacts"),
        MenuItem(label="Search"),
        MenuItem(label="Add New Contact")
    }
)

# Search Contacts Form
search_form = Form(
    name="Search Contacts",
    description="Form to search contacts",
    inputFields={
        InputField(
            name="contactName",
            description="Enter name of contact",
            fieldType="Text",
            validationRules=""
        )
    }
)

search_button = Button(
    name="Submit Search",
    description="Submit search form",
    label="Submit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Search
)

# Add a new contact Form
add_contact_form = Form(
    name="Add a new contact",
    description="Form to add a new contact",
    inputFields={
        InputField(
            name="name",
            description="Enter name",
            fieldType="Text",
            validationRules=""
        ),
        InputField(
            name="phoneNumber",
            description="Enter Phone Number",
            fieldType="Tel",
            validationRules=""
        ),
        InputField(
            name="email",
            description="Enter e-mail",
            fieldType="Email",
            validationRules=""
        )
    }
)

add_contact_button = Button(
    name="Submit New Contact",
    description="Submit new contact form",
    label="Submit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.SubmitForm
)

# Screen definition
contact_screen = Screen(
    name="Contact Management",
    description="Screen for managing contacts",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={menu, search_form, search_button, add_contact_form, add_contact_button}
)

# Class and attributes
# This page is related to the ContactPage class in the structural model.
# Attributes of the ContactPage class:
# - email
# - lastContacted
# - contactName
# - address
# - phoneNumber
# - birthDate
# - isFavorite

# Time taken to generate the structural model: 8.00 seconds

# Time taken to generate the GUI model: 37.67 seconds

# Total time taken: 45.67 seconds
