
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="registration_form_component", description="User Registration Form")

# Input Fields
firstNameField: InputField = InputField(name="first_name", description="Enter Your First Name", fieldType="Text")
lastNameField: InputField = InputField(name="last_name", description="Enter Your Last Name", fieldType="Text")
emailField: InputField = InputField(name="email", description="Enter Your Email", fieldType="Email")
passwordField: InputField = InputField(name="password", description="Create a New Password", fieldType="Password")
ageField: InputField = InputField(name="age", description="Input your age (years)", fieldType="Number")
bioField: InputField = InputField(name="bio", description="Provide a bio", fieldType="Text")

# Radio Buttons
personalAccountButton: Button = Button(name="personal_account", description="Personal Account", label="Personal Account", buttonType=ButtonType.RadioButton)
businessAccountButton: Button = Button(name="business_account", description="Business Account", label="Business Account", buttonType=ButtonType.RadioButton)

# Checkbox
termsCheckbox: Button = Button(name="terms_conditions", description="I accept the terms and conditions", label="I accept the terms and conditions", buttonType=ButtonType.Checkbox)

# File Upload
profilePictureField: InputField = InputField(name="profile_picture", description="Upload a profile picture", fieldType="File")

# Dropdown
referralSourceField: InputField = InputField(name="referral_source", description="How did you hear about us?", fieldType="Text")

# Submit Button
submitButton: Button = Button(name="submit", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Form definition
registrationForm: Form = Form(name="registration_form", description="Registration Form", inputFields={firstNameField, lastNameField, emailField, passwordField, ageField, bioField, profilePictureField, referralSourceField})

# Screen definition
registrationScreen: Screen = Screen(name="RegistrationScreen", description="User Registration Screen", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={registrationForm, personalAccountButton, businessAccountButton, termsCheckbox, submitButton})

# Module definition
registrationModule: Module = Module(name="registration_module", screens={registrationScreen})

# Application definition
registrationApp: Application = Application(name="RegistrationApp", package="com.example.registration", versionCode="1", versionName="1.0", description="User Registration Application", screenCompatibility=True, modules={registrationModule})

# Class and attributes
# This page is related to the class: RegistrationForm
# Attributes of this class based on the structural model:
# - firstName
# - lastName
# - email
# - password
# - age
# - bio
# - accountType
# - termsAccepted
# - profilePicture
# - referralSource

# Time taken to generate the structural model: 7.38 seconds

# Time taken to generate the GUI model: 39.25 seconds

# Total time taken: 46.63 seconds
