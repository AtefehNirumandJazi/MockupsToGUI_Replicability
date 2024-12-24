
from besser.BUML.metamodel.gui import *

# Input Fields for User Login
loginUsernameField: InputField = InputField(
    name="loginUsernameField",
    description="Username input for login",
    fieldType="Text",
    validationRules=""
)

loginPasswordField: InputField = InputField(
    name="loginPasswordField",
    description="Password input for login",
    fieldType="Password",
    validationRules=""
)

# Button for User Login
loginButton: Button = Button(
    name="loginButton",
    description="Button to login",
    label="login",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Login
)

# Form for User Login
userLoginForm: Form = Form(
    name="userLoginForm",
    description="Form for user login",
    inputFields={loginUsernameField, loginPasswordField}
)

# Input Fields for Register User
registerUsernameField: InputField = InputField(
    name="registerUsernameField",
    description="Username input for registration",
    fieldType="Text",
    validationRules=""
)

registerPasswordField: InputField = InputField(
    name="registerPasswordField",
    description="Password input for registration",
    fieldType="Password",
    validationRules=""
)

# Button for Register User
registerButton: Button = Button(
    name="registerButton",
    description="Button to register",
    label="register",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.SubmitForm
)

# Form for Register User
registerUserForm: Form = Form(
    name="registerUserForm",
    description="Form for user registration",
    inputFields={registerUsernameField, registerPasswordField}
)

# Screen definition
userAuthScreen: Screen = Screen(
    name="UserAuthenticationScreen",
    description="Screen for user login and registration",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={userLoginForm, loginButton, registerUserForm, registerButton}
)

# Class and attributes from the structural model
# Class: UserAuthenticationPage
# Attributes: registerUsername, loginPassword, loginUsername, registerPassword

# Time taken to generate the structural model: 4.91 seconds

# Time taken to generate the GUI model: 24.06 seconds

# Total time taken: 28.97 seconds
