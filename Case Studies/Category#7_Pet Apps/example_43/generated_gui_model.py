
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="cat_survey_form", description="Cats survey form")

# Input Fields
nameField: InputField = InputField(name="Name", description="Your name", fieldType="Text", validationRules="")
emailField: InputField = InputField(name="Email", description="Your email", fieldType="Email", validationRules="")
numberOfCatsField: InputField = InputField(name="How many cats do you have", description="Optional", fieldType="Number", validationRules="")
communicationPhraseField: InputField = InputField(name="Choose the phrase that you most often use when communicating with a cat", description="Select current role", fieldType="Text", validationRules="")
catFactField: InputField = InputField(name="Any short fact about your cat(s)?", description="", fieldType="Text", validationRules="")

# Checkboxes for coat colors
coatColorsList: List = List(name="What colors are present in the coat of your pet?", list_sources={
    "Cream", "Brown", "Grey", "White", "Black", "Orange"
})

# Radio buttons for washing with shampoo
washWithShampooList: List = List(name="Do you wash your cat with shampoo?", list_sources={
    "Yes, often", "Not often", "No, my kittle doesn't like this"
})

# Submit Button
submitButton: Button = Button(name="Submit", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Form definition
catSurveyForm: Form = Form(name="CatSurveyForm", description="Cats survey form", inputFields={
    nameField, emailField, numberOfCatsField, communicationPhraseField, catFactField
})

# Screen definition
catSurveyScreen: Screen = Screen(name="CatSurveyScreen", description="Screen for cat survey form",
                                 x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={
                                     catSurveyForm, coatColorsList, washWithShampooList, submitButton
                                 })

# Module definition
catSurveyModule: Module = Module(name="CatSurveyModule", screens={catSurveyScreen})

# Application definition
catSurveyApp: Application = Application(name="CatSurveyApp", package="com.example.catsurvey", versionCode="1",
                                        versionName="1.0", description="An app for cat surveys",
                                        screenCompatibility=True, modules={catSurveyModule})

# Class and Attributes
# This page is related to the class: CatSurveyForm
# Attributes of this class based on the structural model:
# - coatColors: String
# - numberOfCats: Integer
# - washWithShampoo: Boolean
# - communicationPhrase: String
# - catFact: String
# - name: String
# - email: String

# Time taken to generate the structural model: 9.47 seconds

# Time taken to generate the GUI model: 31.55 seconds

# Total time taken: 41.02 seconds
