
from besser.BUML.metamodel.gui import *

# Input fields for User Login
login_username_field = InputField(
    name="loginUsernameField",
    description="Username input for login",
    fieldType="Text",
    validationRules="",
    placeholder="What's your name?"
)

login_password_field = InputField(
    name="loginPasswordField",
    description="Password input for login",
    fieldType="Password",
    validationRules="",
    placeholder="Password..."
)

# Button for User Login
login_button = Button(
    name="loginButton",
    description="Button to log in",
    label="Login",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Login
)

# Input fields for Register User
register_username_field = InputField(
    name="registerUsernameField",
    description="Username input for registration",
    fieldType="Text",
    validationRules="",
    placeholder="Choose your username"
)

register_password_field = InputField(
    name="registerPasswordField",
    description="Password input for registration",
    fieldType="Password",
    validationRules="",
    placeholder="Password..."
)

# Button for Register User
register_button = Button(
    name="registerButton",
    description="Button to register",
    label="Register",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.SubmitForm
)

# Form for User Login
user_login_form = Form(
    name="userLoginForm",
    description="Form for user login",
    inputFields={login_username_field, login_password_field}
)

# Form for Register User
register_user_form = Form(
    name="registerUserForm",
    description="Form for user registration",
    inputFields={register_username_field, register_password_field}
)

# Screen definition
user_authentication_screen = Screen(
    name="UserAuthenticationScreen",
    description="Screen for user login and registration",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={user_login_form, login_button, register_user_form, register_button}
)

# Class and attributes based on the structural model
# Class: UserAuthenticationPage
# Attributes: loginUsername, loginPassword, registerUsername, registerPassword

# Time taken to generate the structural model: 7.55 seconds

# Time taken to generate the GUI model: 26.49 seconds

# Total time taken: 34.04 seconds
