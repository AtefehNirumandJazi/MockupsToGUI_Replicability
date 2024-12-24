
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="register_component", description="User registration form")

# InputFields
emailInput: InputField = InputField(name="email_address", description="E-mail address", fieldType="Email", validationRules="required")
passwordInput: InputField = InputField(name="password", description="Set up a password", fieldType="Password", validationRules="required")
confirmPasswordInput: InputField = InputField(name="confirm_password", description="Confirm password", fieldType="Password", validationRules="required")
firstNameInput: InputField = InputField(name="first_name", description="First name", fieldType="Text", validationRules="required")
lastNameInput: InputField = InputField(name="last_name", description="Last name", fieldType="Text", validationRules="required")

# Checkboxes
subscribeCheckbox: InputField = InputField(name="subscribe_newsletter", description="Subscribe to our newsletter", fieldType="Boolean", validationRules="")
agreeTermsCheckbox: InputField = InputField(name="agree_terms", description="I agree with the Terms and conditions", fieldType="Boolean", validationRules="required")

# Button
createAccountButton: Button = Button(name="create_account", description="Create my account", label="Create my account", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Form
registerForm: Form = Form(name="register_form", description="Register", inputFields={emailInput, passwordInput, confirmPasswordInput, firstNameInput, lastNameInput, subscribeCheckbox, agreeTermsCheckbox})

# Screen definition
RegisterScreen: Screen = Screen(name="RegisterScreen", description="User registration screen", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={registerForm, createAccountButton})

# Module definition
RegisterModule: Module = Module(name="register_module", screens={RegisterScreen})

# Application definition
RegisterApp: Application = Application(name="RechargeApp", package="com.example.rechargeapp", versionCode="1", versionName="1.0", description="A social media app registration page", screenCompatibility=True, modules={RegisterModule})

# Class and attributes
# This page is related to the class: RegisterPage
# Attributes of this class: password, confirmPassword, agreeTerms, firstName, subscribeNewsletter, lastName, emailAddress

# Time taken to generate the structural model: 8.70 seconds

# Time taken to generate the GUI model: 25.24 seconds

# Total time taken: 33.94 seconds
