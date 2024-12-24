
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="multi_factor_authentication", description="Multi Factor Authentication")

# Button1: Email
emailButton: Button = Button(
    name="Email Button",
    description="Authenticate via Email",
    label="EMAIL",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Select
)

# Button2: Text Message (SMS)
smsButton: Button = Button(
    name="SMS Button",
    description="Authenticate via SMS",
    label="TEXT MESSAGE (SMS)",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Select
)

# Button3: Authentication App
authAppButton: Button = Button(
    name="Auth App Button",
    description="Authenticate via App",
    label="AUTHENTICATION APP",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Select
)

# Multi Factor Authentication Screen definition
MultiFactorAuthScreen: Screen = Screen(
    name="MultiFactorAuthScreen",
    description="Please select how you would like to authenticate",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={emailButton, smsButton, authAppButton}
)

# Module definition
AuthModule: Module = Module(name="auth_module", screens={MultiFactorAuthScreen})

# Application definition
AuthApp: Application = Application(
    name="Authentication App",
    package="com.example.authapp",
    versionCode="1",
    versionName="1.0",
    description="An application for multi-factor authentication.",
    screenCompatibility=True,
    modules={AuthModule}
)

# Class and attributes related to this page
# Class: MultiFactorAuthenticationPage
# Attributes: isEnabled, method, lastUpdated, description

# Time taken to generate the structural model: 10.64 seconds

# Time taken to generate the GUI model: 19.26 seconds

# Total time taken: 29.90 seconds
