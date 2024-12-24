
from besser.BUML.metamodel.gui import *

# Menu definition
sideMenu: Menu = Menu(
    name="Side Menu",
    description="Navigation menu",
    menuItems={
        MenuItem(label="Login"),
        MenuItem(label="Courses"),
        MenuItem(label="Purchase Course"),
        MenuItem(label="Profile"),
        MenuItem(label="Change Password")
    }
)

# Input fields for the login form
usernameField: InputField = InputField(
    name="Username Field",
    description="Input for username",
    fieldType="Text",
    validationRules="required"
)

passwordField: InputField = InputField(
    name="Password Field",
    description="Input for password",
    fieldType="Password",
    validationRules="required"
)

# Form definition
loginForm: Form = Form(
    name="Login Form",
    description="Form for user login",
    inputFields={usernameField, passwordField}
)

# Button definition
loginButton: Button = Button(
    name="Login Button",
    description="Button to submit login form",
    label="Login",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Login
)

# Screen definition
loginScreen: Screen = Screen(
    name="Login Screen",
    description="Screen for user login",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Large",
    view_elements={sideMenu, loginForm, loginButton}
)

# Module definition
loginModule: Module = Module(
    name="Login Module",
    screens={loginScreen}
)

# Application definition
loginApp: Application = Application(
    name="Login Application",
    package="com.example.loginapp",
    versionCode="1",
    versionName="1.0",
    description="Application for user login",
    screenCompatibility=True,
    modules={loginModule}
)

# Class and attributes
# This page is related to the class: LoginPage
# Attributes of this class based on the structural model:
# - username: StringType
# - password: StringType
# - loginTime: DateTimeType
# - rememberMe: BooleanType

# Time taken to generate the structural model: 8.07 seconds

# Time taken to generate the GUI model: 25.70 seconds

# Total time taken: 33.77 seconds
