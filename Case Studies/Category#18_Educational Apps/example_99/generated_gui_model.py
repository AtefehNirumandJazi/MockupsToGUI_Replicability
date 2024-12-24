
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="Social Educational App", description="A social educational platform")

# InputFields for Login
usernameField: InputField = InputField(name="Username", description="Enter your username", fieldType="Text", validationRules="required")
passwordField: InputField = InputField(name="Password", description="Enter your password", fieldType="Password", validationRules="required")

# Form for Login
loginForm: Form = Form(name="Login Form", description="User login form", inputFields={usernameField, passwordField})

# Button for Login
loginButton: Button = Button(name="Login Button", description="Submit login form", label="Login", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login)

# InputField for Chat
chatField: InputField = InputField(name="Chat", description="Type your message here", fieldType="Text", validationRules="")

# Button for Send
sendButton: Button = Button(name="Send Button", description="Send chat message", label="Send", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Send)

# Menu for Navigation
navigationMenu: Menu = Menu(name="Navigation Menu", description="Main navigation menu", menuItems={
    MenuItem(label="Home"),
    MenuItem(label="Chat"),
    MenuItem(label="Videos"),
    MenuItem(label="Photos"),
    MenuItem(label="Messages"),
    MenuItem(label="Profile")
})

# Image for Background
backgroundImage: Image = Image(name="Background Image", description="Background image of children using laptops")

# Footer
footer: ViewComponent = ViewComponent(name="Footer", description="Footer with copyright and icons")

# Screen definition
socialEducationalAppScreen: Screen = Screen(
    name="Social Educational App Screen",
    description="Main screen for the social educational app",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Large",
    view_elements={loginForm, loginButton, chatField, sendButton, navigationMenu, backgroundImage, footer}
)

# Module definition
socialEducationalAppModule: Module = Module(name="Social Educational App Module", screens={socialEducationalAppScreen})

# Application definition
socialEducationalApp: Application = Application(
    name="Social Educational App",
    package="com.example.socialeducationalapp",
    versionCode="1",
    versionName="1.0",
    description="A social educational platform for students",
    screenCompatibility=True,
    modules={socialEducationalAppModule}
)

# Class and Attributes
# This page is related to the class: SocialEducationalApp
# Attributes of this class based on the structural model:
# - message: String
# - videos: Boolean
# - copyright: String
# - photos: Boolean
# - icons: String
# - password: String
# - home: Boolean
# - messages: Boolean
# - username: String
# - chat: Boolean
# - profile: Boolean

# Time taken to generate the structural model: 12.13 seconds

# Time taken to generate the GUI model: 29.85 seconds

# Total time taken: 41.97 seconds
