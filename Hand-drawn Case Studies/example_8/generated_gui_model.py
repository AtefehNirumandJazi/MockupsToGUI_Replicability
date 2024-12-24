
from besser.BUML.metamodel.gui import *

# Input Fields
nameInput: InputField = InputField(
    name="Name Input",
    description="Enter Your Name",
    fieldType="Text",
    validationRules=""
)

emailInput: InputField = InputField(
    name="Email Input",
    description="Enter Your Email",
    fieldType="Email",
    validationRules=""
)

ageInput: InputField = InputField(
    name="Age Input",
    description="Age (optional)",
    fieldType="Number",
    validationRules=""
)

currentRoleInput: InputField = InputField(
    name="Current Role Input",
    description="Select Current Role",
    fieldType="Text",
    validationRules=""
)

# Radio Buttons for Payment Options
paymentOption1: InputField = InputField(
    name="Payment Option 1",
    description="R100,50",
    fieldType="Text",
    validationRules=""
)

paymentOption2: InputField = InputField(
    name="Payment Option 2",
    description="R399,50",
    fieldType="Text",
    validationRules=""
)

paymentOption3: InputField = InputField(
    name="Payment Option 3",
    description="R499,50",
    fieldType="Text",
    validationRules=""
)

# Form
surveyForm: Form = Form(
    name="Learns Online Survey Form",
    description="Thank you for taking the time to help us improve our platform.",
    inputFields={nameInput, emailInput, ageInput, currentRoleInput, paymentOption1, paymentOption2, paymentOption3}
)

# Screen
surveyScreen: Screen = Screen(
    name="Survey Screen",
    description="Survey Form Screen",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={surveyForm}
)

# Class and Attributes
# This page is related to the class: SurveyForm
# Attributes of this class based on the structural model:
# - age
# - email
# - paymentOption
# - name
# - currentRole

# Time taken to generate the structural model: 8.91 seconds

# Time taken to generate the GUI model: 24.14 seconds

# Total time taken: 33.05 seconds
