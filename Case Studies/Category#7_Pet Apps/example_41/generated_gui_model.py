
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="pet_sitter_form", description="Pet Sitter Form")

# Input Fields
petNameField: InputField = InputField(name="Pet Name", description="Enter the pet's name", fieldType="Text", validationRules="")
petTypeField: InputField = InputField(name="Pet Type", description="Select the pet type", fieldType="Text", validationRules="")

# Radio Buttons for Pet Gender
maleRadioButton: InputField = InputField(name="Male", description="Select if pet is male", fieldType="Text", validationRules="")
femaleRadioButton: InputField = InputField(name="Female", description="Select if pet is female", fieldType="Text", validationRules="")
unknownRadioButton: InputField = InputField(name="Unknown", description="Select if pet gender is unknown", fieldType="Text", validationRules="")

# Text Area for Special Care Instructions
specialCareInstructionsField: InputField = InputField(name="Special Care Instructions", description="Enter special care instructions", fieldType="Text", validationRules="")

# Buttons
submitButton: Button = Button(name="Submit", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)
testingButton: Button = Button(name="Testing", description="Click to display saved data", label="TESTING: click to display saved data", buttonType=ButtonType.TextButton, actionType=ButtonActionType.ShowList)

# Form definition
petSitterForm: Form = Form(name="Pet Sitter Form", description="Form to enter pet details", inputFields={petNameField, petTypeField, specialCareInstructionsField, maleRadioButton, femaleRadioButton, unknownRadioButton})

# Screen definition
petSitterScreen: Screen = Screen(name="Pet Sitter Screen", description="Screen for pet sitter form", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={petSitterForm, submitButton, testingButton})

# Module definition
petSitterModule: Module = Module(name="Pet Sitter Module", screens={petSitterScreen})

# Application definition
petSitterApp: Application = Application(name="Pet Sitter Application", package="com.example.petsitter", versionCode="1", versionName="1.0", description="Application for pet sitting services", screenCompatibility=True, modules={petSitterModule})

# Class and Attributes
# This page is related to the class: PetSitterPage
# Attributes of this class:
# - petGender
# - duration
# - ownerContact
# - isVaccinated
# - petName
# - petAge
# - bookingDate
# - petType
# - petWeight
# - bookingTime
# - specialCareInstructions
# - ownerName

# Time taken to generate the structural model: 10.05 seconds

# Time taken to generate the GUI model: 46.34 seconds

# Total time taken: 56.38 seconds
