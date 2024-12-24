
from besser.BUML.metamodel.gui import *

# Input Fields
usernameField: InputField = InputField(
    name="Username Field",
    description="Input field for username",
    fieldType="Text",
    validationRules="required"
)

passwordField: InputField = InputField(
    name="Password Field",
    description="Input field for password",
    fieldType="Password",
    validationRules="required"
)

# Button
signInButton: Button = Button(
    name="Sign In Button",
    description="Button to sign in",
    label="SIGN IN",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Login
)

# Form
signInForm: Form = Form(
    name="Sign In Form",
    description="Form for user sign in",
    inputFields={usernameField, passwordField}
)

# Menu Items
forgotPasswordItem: MenuItem = MenuItem(label="Forgot password?")
changePasswordItem: MenuItem = MenuItem(label="Change my password")
needHelpItem: MenuItem = MenuItem(label="I need help.")

# Menu
helpMenu: Menu = Menu(
    name="Help Menu",
    description="Menu for help options",
    menuItems={forgotPasswordItem, changePasswordItem, needHelpItem}
)

# Screen
signInScreen: Screen = Screen(
    name="Sign In Screen",
    description="Screen for user sign in",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={signInForm, signInButton, helpMenu}
)

# Module
signInModule: Module = Module(
    name="Sign In Module",
    screens={signInScreen}
)

# Application
signInApp: Application = Application(
    name="Sign In Application",
    package="com.example.signin",
    versionCode="1",
    versionName="1.0",
    description="Application for user sign in",
    screenCompatibility=True,
    modules={signInModule}
)

# Class and Attributes
# This page is related to the class: SignInPage
# Attributes of this class:
# - loginAttempts: IntegerType
# - username: StringType
# - password: StringType
# - rememberMe: BooleanType
# - lastLogin: DateTimeType

# Time taken to generate the structural model: 9.06 seconds

# Time taken to generate the GUI model: 33.07 seconds

# Total time taken: 42.13 seconds
