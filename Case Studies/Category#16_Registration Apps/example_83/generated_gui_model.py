
from besser.BUML.metamodel.gui import *

# Input fields
name_input = InputField(name="Name Input", description="Enter your name", fieldType="Text")
email_input = InputField(name="Email Input", description="Enter your email", fieldType="Email")
password_input = InputField(name="Password Input", description="Enter your password", fieldType="Password")

# Form
sign_up_form = Form(name="Sign Up Form", description="User sign up form", inputFields={name_input, email_input, password_input})

# Buttons
submit_button = Button(name="Submit Button", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton)
more_info_button = Button(name="More Info Button", description="Get more information", label="More Info", buttonType=ButtonType.TextButton)

# Screen
sign_up_screen = Screen(name="Sign Up Screen", description="Screen for user sign up", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={sign_up_form, submit_button, more_info_button})

# Class and attributes
class_name = "SignUpPage"
attributes = ["email", "confirmPassword", "signUpDate", "password", "name", "acceptTerms"]

# Time taken to generate the structural model: 5.35 seconds

# Time taken to generate the GUI model: 13.51 seconds

# Total time taken: 18.86 seconds
