
# Import necessary classes from the GUI metamodel
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="user_registration_component", description="User Registration Page")

# InputFields for Member Login Section
memberLoginUsername: InputField = InputField(name="member_login_username", description="Username", fieldType="Text", validationRules="")
memberLoginPassword: InputField = InputField(name="member_login_password", description="Password", fieldType="Password", validationRules="")

# Form for Member Login Section
memberLoginForm: Form = Form(name="member_login_form", description="Members Login Form", inputFields={memberLoginUsername, memberLoginPassword})

# Button for Member Login Section
loginButton: Button = Button(name="login_button", description="Login Button", label="Login", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login)

# InputFields for Registration Section
registrationUsername: InputField = InputField(name="registration_username", description="Username", fieldType="Text", validationRules="")
registrationPassword: InputField = InputField(name="registration_password", description="Password", fieldType="Password", validationRules="")

# Form for Registration Section
registrationForm: Form = Form(name="registration_form", description="Registration Form", inputFields={registrationUsername, registrationPassword})

# Button for Registration Section
registerButton: Button = Button(name="register_button", description="Register Button", label="Register", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Screen definition
userRegistrationScreen: Screen = Screen(name="UserRegistrationScreen", description="User Registration and Login Screen",
                                        x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                                        view_elements={memberLoginForm, loginButton, registrationForm, registerButton})

# Module definition
userRegistrationModule: Module = Module(name="user_registration_module", screens={userRegistrationScreen})

# Application definition
userRegistrationApp: Application = Application(name="UserRegistrationApp", package="com.example.userregistration", versionCode="1",
                                               versionName="1.0", description="An application for user registration and login.",
                                               screenCompatibility=True, modules={userRegistrationModule})

# Class and attributes based on the structural model
# Class: UserRegistrationPage
# Attributes: username, password

# Time taken to generate the structural model: 6.48 seconds

# Time taken to generate the GUI model: 18.32 seconds

# Total time taken: 24.80 seconds
