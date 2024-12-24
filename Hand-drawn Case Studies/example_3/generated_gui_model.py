
from besser.BUML.metamodel.gui import *

# Input fields for the registration page
email_input = InputField(name="Email", description="Email input field", fieldType="Email", validationRules="required")
username_input = InputField(name="Username", description="Username input field", fieldType="Text", validationRules="required")
password_input = InputField(name="Password", description="Password input field", fieldType="Password", validationRules="required")

# Form containing the input fields
registration_form = Form(name="RegistrationForm", description="Basic registration form", inputFields={email_input, username_input, password_input})

# Screen containing the form
registration_screen = Screen(name="RegistrationScreen", description="Screen for user registration", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={registration_form})

# Adding header as per the mock-up
header = ViewElement(name="Header", description="Header for the registration page")

# Updating the screen to include the header
registration_screen.view_elements.add(header)

# Class and attributes based on the structural model
class_name = "RegistrationPage"
attributes = [
    "email",
    "dateOfBirth",
    "confirmPassword",
    "termsAccepted",
    "username",
    "registrationDate",
    "firstName",
    "lastName",
    "password"
]

# Time taken to generate the structural model: 9.33 seconds

# Time taken to generate the GUI model: 21.83 seconds

# Total time taken: 31.16 seconds
