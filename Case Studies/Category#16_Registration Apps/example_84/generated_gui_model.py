
from besser.BUML.metamodel.gui import *

# Input Fields
name_input = InputField(name="Name", description="Enter your name", fieldType="Text", validationRules="")
gender_input = InputField(name="Gender", description="Select your gender", fieldType="Text", validationRules="")
age_input = InputField(name="Age", description="Enter your age", fieldType="Number", validationRules="")
attendance_input = InputField(name="Daily Attendance", description="Enter daily attendance", fieldType="Number", validationRules="")
phone_input = InputField(name="Phone Number", description="Enter your phone number", fieldType="Tel", validationRules="")
password_input = InputField(name="Password", description="Enter your password", fieldType="Password", validationRules="")

# Button
register_button = Button(name="Register Button", description="Register new user", label="Register", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Search Field
search_input = InputField(name="Search", description="Search", fieldType="Search", validationRules="")

# Form
registration_form = Form(name="Registration Form", description="Form for user registration", inputFields={name_input, gender_input, age_input, attendance_input, phone_input, password_input})

# Screen
center_registration_screen = Screen(name="Center Registration Screen", description="Screen for center registration", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={registration_form, register_button, search_input})

# Module
center_registration_module = Module(name="Center Registration Module", screens={center_registration_screen})

# Application
center_registration_app = Application(name="Center Registration App", package="com.example.centerregistration", versionCode="1", versionName="1.0", description="App for center registration", screenCompatibility=True, modules={center_registration_module})

# Class and Attributes
# This page is related to the class: CenterRegistrationPage
# Attributes of this class: age, name, userPassword, contactNumber, searchQuery, dailyAttendance, gender

# Time taken to generate the structural model: 5.94 seconds

# Time taken to generate the GUI model: 18.56 seconds

# Total time taken: 24.50 seconds
