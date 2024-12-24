
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="login_component", description="Login Page")

# Input Fields
usernameField: InputField = InputField(name="Username", description="Enter your username", fieldType="Text", validationRules="")
passwordField: InputField = InputField(name="Password", description="Enter your password", fieldType="Password", validationRules="")

# Buttons
loginButton: Button = Button(name="Login Button", description="Login to the application", label="Login", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login)
createAccountButton: Button = Button(name="Create Account Button", description="Create a new account", label="Create Account", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate)
deleteAccountButton: Button = Button(name="Delete Account Button", description="Delete an existing account", label="Delete Account", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)

# Form definition
loginForm: Form = Form(name="Login Form", description="Form for user login", inputFields={usernameField, passwordField})

# Screen definition
LoginScreen: Screen = Screen(name="Login Screen", description="Screen for user login", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={loginForm, loginButton, createAccountButton, deleteAccountButton})

# Module definition
LoginModule: Module = Module(name="Login Module", screens={LoginScreen})

# Application definition
LoginApp: Application = Application(name="Login Application", package="com.example.loginapp", versionCode="1", versionName="1.0", description="An application for user login", screenCompatibility=True, modules={LoginModule})

# Class and attributes
# This page is related to the class: LoginPage
# Attributes of this class based on the structural model:
# - loginStatus: BooleanType
# - username: StringType
# - password: StringType
# - lastLoginAttempt: DateTimeType
# - errorMessage: StringType

# Time taken to generate the structural model: 6.58 seconds

# Time taken to generate the GUI model: 30.43 seconds

# Total time taken: 37.02 seconds
