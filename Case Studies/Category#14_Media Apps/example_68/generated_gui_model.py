
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="registration_component", description="Registration Page")

# Input Fields
emailField: InputField = InputField(name="Email", description="Email input field", fieldType="Email", validationRules="required")
usernameField: InputField = InputField(name="Username", description="Username input field", fieldType="Text", validationRules="required")
passwordField: InputField = InputField(name="Password", description="Password input field", fieldType="Password", validationRules="required")

# Form definition
registrationForm: Form = Form(name="RegistrationForm", description="Form for user registration", inputFields={emailField, usernameField, passwordField})

# Header
header: ViewComponent = ViewComponent(name="Header", description="Header with title and subtitle")

# Screen definition
registrationScreen: Screen = Screen(name="RegistrationScreen", description="Screen for user registration",
                                    x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={header, registrationForm})

# Module definition
registrationModule: Module = Module(name="RegistrationModule", screens={registrationScreen})

# Application definition
registrationApp: Application = Application(name="RegistrationApp", package="com.example.registration", versionCode="1",
                                           versionName="1.0", description="A simple registration application",
                                           screenCompatibility=True, modules={registrationModule})

# Class and attributes
# This page is related to the class: RegistrationPage
# Attributes of this class based on the structural model:
# - isEmailVerified: Boolean
# - password: String
# - registrationDate: DateTime
# - email: String
# - username: String

# Time taken to generate the structural model: 10.27 seconds

# Time taken to generate the GUI model: 19.69 seconds

# Total time taken: 29.95 seconds
