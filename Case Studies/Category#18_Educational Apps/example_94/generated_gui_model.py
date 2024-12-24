
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="login_form", description="Login and Registration Form")

# InputFields for Login
registrationNumberField: InputField = InputField(name="Registration Number", description="Enter Registration", fieldType="Text", validationRules="")
passwordField: InputField = InputField(name="Password", description="Enter Password", fieldType="Password", validationRules="")
payrollNumberField: InputField = InputField(name="Payroll Number", description="Enter Payroll Number", fieldType="Text", validationRules="")
emailField: InputField = InputField(name="Email", description="Enter Email", fieldType="Email", validationRules="")
fullNameField: InputField = InputField(name="Full Name", description="Enter Full Name", fieldType="Text", validationRules="")
confirmPasswordField: InputField = InputField(name="Confirm Password", description="Enter Confirm Password", fieldType="Password", validationRules="")

# Buttons for Login
loginButton: Button = Button(name="Login Button", description="Login", label="Login", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login)
cancelButton: Button = Button(name="Cancel Button", description="Cancel", label="Cancel", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)
forgotPasswordButton: Button = Button(name="Forgot Password Button", description="Forgot Password", label="Forgot password?", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate)

# Buttons for Registration
registerButton: Button = Button(name="Register Button", description="Register", label="Register", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Checkboxes
rememberMeCheckbox: InputField = InputField(name="Remember Me", description="Remember me", fieldType="Boolean", validationRules="")
agreeTermsCheckbox: InputField = InputField(name="Agree Terms", description="I agree all statements in Terms of service", fieldType="Boolean", validationRules="")

# Form for Login
loginForm: Form = Form(name="Login Form", description="Form for user login", inputFields={registrationNumberField, passwordField, rememberMeCheckbox})

# Form for Registration
registrationForm: Form = Form(name="Registration Form", description="Form for user registration", inputFields={fullNameField, payrollNumberField, emailField, passwordField, confirmPasswordField, agreeTermsCheckbox})

# Screen definition
loginScreen: Screen = Screen(name="Login Screen", description="Screen for user login and registration", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={loginForm, registrationForm, loginButton, cancelButton, forgotPasswordButton, registerButton})

# Module definition
loginModule: Module = Module(name="Login Module", screens={loginScreen})

# Application definition
loginApp: Application = Application(name="Login Application", package="com.example.loginapp", versionCode="1", versionName="1.0", description="Application for user login and registration", screenCompatibility=True, modules={loginModule})

# Class and attributes
# This page is related to the class: LoginPage
# Attributes of this class based on the structural model:
# - agreeTerms: Boolean
# - confirmPassword: String
# - password: String
# - rememberMe: Boolean
# - registrationNumber: String
# - payrollNumber: String
# - email: String
# - fullName: String

# Time taken to generate the structural model: 13.42 seconds

# Time taken to generate the GUI model: 28.11 seconds

# Total time taken: 41.53 seconds
