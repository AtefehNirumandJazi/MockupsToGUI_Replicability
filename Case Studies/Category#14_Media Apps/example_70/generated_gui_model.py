
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="survey_form_component", description="Survey Form for Social Media Influence")

# Input Fields
nameField: InputField = InputField(name="Name", description="Enter your name", fieldType="Text", validationRules="")
emailField: InputField = InputField(name="Email", description="Enter your email", fieldType="Email", validationRules="")
passwordField: InputField = InputField(name="Password", description="Password must contain numbers and letters", fieldType="Password", validationRules="")
numberField: InputField = InputField(name="Number", description="Enter your phone number", fieldType="Tel", validationRules="")

# Gender Radio Buttons
genderMale: InputField = InputField(name="GenderMale", description="Male", fieldType="Text", validationRules="")
genderFemale: InputField = InputField(name="GenderFemale", description="Female", fieldType="Text", validationRules="")

# Form definition
surveyForm: Form = Form(name="SurveyForm", description="Influence of social media on Gen Z", inputFields={nameField, emailField, passwordField, numberField, genderMale, genderFemale})

# Screen definition
surveyScreen: Screen = Screen(name="SurveyScreen", description="Survey Form Screen", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={surveyForm})

# Class and attributes
# This page is related to the class: SurveyForm
# Attributes of this class based on the structural model:
# - name
# - email
# - password
# - phoneNumber
# - gender

# Time taken to generate the structural model: 8.87 seconds

# Time taken to generate the GUI model: 21.34 seconds

# Total time taken: 30.21 seconds
