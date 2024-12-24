
from besser.BUML.metamodel.gui import *
from library import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="registration_component", description="User Registration Form")

# Input Fields
firstNameField: InputField = InputField(name="First Name", description="User's first name", fieldType="Text", validationRules="required")
lastNameField: InputField = InputField(name="Last Name", description="User's last name", fieldType="Text", validationRules="required")
emailField: InputField = InputField(name="Your Email", description="User's email address", fieldType="Email", validationRules="required")
phoneField: InputField = InputField(name="Your Phone", description="User's phone number", fieldType="Tel", validationRules="required")
passwordField: InputField = InputField(name="Password", description="User's password", fieldType="Password", validationRules="required")
confirmPasswordField: InputField = InputField(name="Confirm Password", description="Confirm user's password", fieldType="Password", validationRules="required")
securityQuestionField: InputField = InputField(name="Security Question", description="User's security question", fieldType="Text", validationRules="required")
securityAnswerField: InputField = InputField(name="Enter Your Answer", description="Answer to security question", fieldType="Text", validationRules="required")
genderField: InputField = InputField(name="Gender", description="User's gender", fieldType="Text", validationRules="required")

# Form
registrationForm: Form = Form(name="Registration Form", description="Form for user registration", inputFields={
    firstNameField, lastNameField, emailField, phoneField, passwordField, confirmPasswordField, securityQuestionField, securityAnswerField, genderField
})

# Buttons
registerButton: Button = Button(name="Register Button", description="Button to submit registration", label="Register", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)
loginButton: Button = Button(name="Login Button", description="Button to navigate to login", label="Login", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate)

# Screen definition
RegistrationScreen: Screen = Screen(name="Registration Screen", description="Screen for user registration",
                                    x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={registrationForm, registerButton, loginButton})

# Module definition
RegistrationModule: Module = Module(name="registration_module", screens={RegistrationScreen})

# Application definition
RegistrationApp: Application = Application(name="User Registration App", package="com.example.registration", versionCode="1",
                                           versionName="1.0", description="An application for user registration",
                                           screenCompatibility=True, modules={RegistrationModule})

# Class and attributes
# This page is related to the class: RegistrationPage
# Attributes of this class based on the structural model:
# - firstName
# - lastName
# - email
# - phone
# - password
# - confirmPassword
# - securityQuestion
# - securityAnswer
# - gender

# Time taken to generate the structural model: 10.76 seconds

# Time taken to generate the GUI model: 33.89 seconds

# Total time taken: 44.65 seconds
