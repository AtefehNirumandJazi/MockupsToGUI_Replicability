
# Input Fields
usernameField = InputField(name="Username Field", description="Enter Username", fieldType="Text", validationRules="")
passwordField = InputField(name="Password Field", description="Enter Password", fieldType="Password", validationRules="")
reenterPasswordField = InputField(name="Re-enter Password Field", description="Re-enter Password", fieldType="Password", validationRules="")

# Radio Buttons for Operating System
osRadioButton = Form(name="OS Radio Button", description="Phone Operating System", inputFields=set([
    InputField(name="Android", description="Android", fieldType="Text", validationRules=""),
    InputField(name="iOS", description="iOS", fieldType="Text", validationRules=""),
    InputField(name="Windows", description="Windows", fieldType="Text", validationRules="")
]))

# Dropdown for Phone Model
phoneModelDropdown = List(name="Phone Model Dropdown", description="Select Phone Model", list_sources=set())

# Form
registrationForm = Form(name="Registration Form", description="Registration App", inputFields=set([
    usernameField, passwordField, reenterPasswordField
]))

# Screen
registrationScreen = Screen(name="Registration Screen", description="Phone Cloud Registration App",
                            x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                            view_elements=set([registrationForm, osRadioButton, phoneModelDropdown]))

# Module
registrationModule = Module(name="Registration Module", screens=set([registrationScreen]))

# Application
registrationApp = Application(name="Phone Cloud App", package="com.example.phonecloud", versionCode="1",
                              versionName="1.0", description="Phone Cloud Registration Application",
                              screenCompatibility=True, modules=set([registrationModule]))

# Class and Attributes
# This page is related to the class: RegistrationPage
# Attributes of this class based on the structural model:
# - operatingSystem
# - password
# - phoneModel
# - username
# - reenterPassword

# Time taken to generate the structural model: 6.38 seconds

# Time taken to generate the GUI model: 28.81 seconds

# Total time taken: 35.20 seconds
