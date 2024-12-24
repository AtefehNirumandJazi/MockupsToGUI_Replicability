
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="pet_survey_component", description="Pet Survey Form")

# Input Fields
nameField: InputField = InputField(name="Name", description="Enter your name", fieldType="Text", validationRules="")
emailField: InputField = InputField(name="Email", description="Enter your email", fieldType="Email", validationRules="")
numberOfPetsField: InputField = InputField(name="Number of Pets", description="Number of pets (optional)", fieldType="Number", validationRules="")
experienceLevelField: InputField = InputField(name="Experience Level", description="Select current experience level", fieldType="Text", validationRules="")

# Radio Buttons
interestedInAdoptingYes: InputField = InputField(name="Interested in Adopting Yes", description="Yes", fieldType="Boolean", validationRules="")
interestedInAdoptingNotSure: InputField = InputField(name="Interested in Adopting Not Sure", description="Not sure", fieldType="Boolean", validationRules="")
interestedInAdoptingNo: InputField = InputField(name="Interested in Adopting No", description="No", fieldType="Boolean", validationRules="")

# Checkboxes
petTypesDog: InputField = InputField(name="Pet Type Dog", description="Dog", fieldType="Boolean", validationRules="")
petTypesCat: InputField = InputField(name="Pet Type Cat", description="Cat", fieldType="Boolean", validationRules="")
petTypesFish: InputField = InputField(name="Pet Type Fish", description="Fish", fieldType="Boolean", validationRules="")
petTypesFerret: InputField = InputField(name="Pet Type Ferret", description="Ferret", fieldType="Boolean", validationRules="")
petTypesSnake: InputField = InputField(name="Pet Type Snake", description="Snake", fieldType="Boolean", validationRules="")
petTypesOther: InputField = InputField(name="Pet Type Other", description="Other", fieldType="Boolean", validationRules="")

# Text Area
favoriteThingField: InputField = InputField(name="Favorite Thing", description="Tell us your favorite thing about having a pet", fieldType="Text", validationRules="")

# Form
petSurveyForm: Form = Form(name="Pet Survey Form", description="Pet Survey Form", inputFields={
    nameField, emailField, numberOfPetsField, experienceLevelField,
    interestedInAdoptingYes, interestedInAdoptingNotSure, interestedInAdoptingNo,
    petTypesDog, petTypesCat, petTypesFish, petTypesFerret, petTypesSnake, petTypesOther,
    favoriteThingField
})

# Button
submitButton: Button = Button(name="Submit Button", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Screen definition
PetSurveyScreen: Screen = Screen(name="Pet Survey Screen", description="Pet Survey Screen",
                                 x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                                 view_elements={petSurveyForm, submitButton})

# Module definition
PetSurveyModule: Module = Module(name="Pet Survey Module", screens={PetSurveyScreen})

# Application definition
PetSurveyApp: Application = Application(name="Pet Survey Application", package="com.example.petsurvey", versionCode="1",
                                        versionName="1.0", description="An application for conducting pet surveys.",
                                        screenCompatibility=True, modules={PetSurveyModule})

# Class and Attributes
# This page is related to the class: PetSurveyPage
# Attributes of this class based on the structural model:
# - name
# - petTypes
# - experienceLevel
# - favoriteThing
# - numberOfPets
# - email
# - interestedInAdopting

# Time taken to generate the structural model: 9.08 seconds

# Time taken to generate the GUI model: 41.75 seconds

# Total time taken: 50.84 seconds
