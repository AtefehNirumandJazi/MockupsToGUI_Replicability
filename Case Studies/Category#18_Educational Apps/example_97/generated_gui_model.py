
from besser.BUML.metamodel.gui import *

# Input Fields
name_input = InputField(name="Name", description="Enter your name", fieldType="Text", validationRules="")
email_input = InputField(name="Email", description="Enter your Email", fieldType="Email", validationRules="")
age_input = InputField(name="Age", description="Age (optional)", fieldType="Number", validationRules="")

# Dropdown for current role
current_role_dropdown = InputField(name="Current Role", description="Select current role", fieldType="Text", validationRules="")

# Radio Buttons for education investment amount
investment_options = [
    InputField(name="R10,50", description="R10,50", fieldType="Radio", validationRules=""),
    InputField(name="R39,50", description="R39,50", fieldType="Radio", validationRules=""),
    InputField(name="R49,50", description="R49,50", fieldType="Radio", validationRules="")
]

# Form
survey_form = Form(
    name="Learners Online Survey Form",
    description="Thank you for taking the time to help us improve our platform",
    inputFields={name_input, email_input, age_input, current_role_dropdown, *investment_options}
)

# Screen
survey_screen = Screen(
    name="Survey Screen",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={survey_form}
)

# Module
survey_module = Module(
    name="Survey Module",
    screens={survey_screen}
)

# Application
survey_app = Application(
    name="Survey Application",
    package="com.example.surveyapp",
    versionCode="1",
    versionName="1.0",
    description="A survey application for learners",
    screenCompatibility=True,
    modules={survey_module}
)

# Class and Attributes
# This page is related to the SurveyForm class in the structural model.
# Attributes of SurveyForm class:
# - emailAddress
# - currentOccupation
# - fullName
# - age
# - educationInvestmentAmount

# Time taken to generate the structural model: 10.22 seconds

# Time taken to generate the GUI model: 24.14 seconds

# Total time taken: 34.36 seconds
