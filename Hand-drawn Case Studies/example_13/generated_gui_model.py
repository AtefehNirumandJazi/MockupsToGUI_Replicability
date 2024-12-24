
# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="sign_in_component", description="Sign In Page")

# Input Fields
usernameField: InputField = InputField(name="username", description="Username input", fieldType="Text", validationRules="")
passwordField: InputField = InputField(name="password", description="Password input", fieldType="Password", validationRules="")

# Button
signInButton: Button = Button(name="sign_in_button", description="Sign In button", label="SIGN IN", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login)

# Menu
forgotPasswordItem: MenuItem = MenuItem(label="Forgot Password?")
changePasswordItem: MenuItem = MenuItem(label="Change my Password")
helpItem: MenuItem = MenuItem(label="I need help")
menu: Menu = Menu(name="options_menu", description="Options menu", menuItems={forgotPasswordItem, changePasswordItem, helpItem})

# Screen definition
SignInScreen: Screen = Screen(name="SignInScreen", description="Screen for user sign in",
                              x_dpi="x_dpi", y_dpi="y_dpi", size="Small",
                              view_elements={usernameField, passwordField, signInButton, menu})

# Module definition
SignInModule: Module = Module(name="sign_in_module", screens={SignInScreen})

# Application definition
SignInApp: Application = Application(name="SignInApp", package="com.example.signinapp", versionCode="1",
                                     versionName="1.0", description="Application for user sign in",
                                     screenCompatibility=True, modules={SignInModule})

# Class and Attributes
# This page is related to the class: SignInPage
# Attributes of this class: signInButton, errorMessage, rememberMe, password, username

# Time taken to generate the structural model: 9.08 seconds

# Time taken to generate the GUI model: 23.01 seconds

# Total time taken: 32.09 seconds
