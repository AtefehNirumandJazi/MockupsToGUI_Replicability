
from besser.BUML.metamodel.gui import *

# Input Fields
name_input = InputField(name="Name", description="Enter your name", fieldType="Text", validationRules="")
email_input = InputField(name="Email", description="Enter your email", fieldType="Email", validationRules="")
age_input = InputField(name="Age", description="Age (optional)", fieldType="Number", validationRules="")

# Dropdown for favorite cat type
favorite_cat_type_dropdown = InputField(name="Favorite Cat Type", description="Select your favorite cat type", fieldType="Text", validationRules="")

# Radio buttons for number of cats owned
number_of_cats_owned_radio = InputField(name="Number of Cats Owned", description="How many cats have you owned?", fieldType="Text", validationRules="")

# Checkboxes for favorite cat features
favorite_cat_feature_checkboxes = InputField(name="Favorite Cat Feature", description="What's your favorite thing about cats?", fieldType="Text", validationRules="")

# Text area for additional comments
additional_comments_textarea = InputField(name="Additional Comments", description="Anything else you love about cats?", fieldType="Text", validationRules="")

# Submit button
submit_button = Button(name="Submit", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Form
cat_lovers_survey_form = Form(name="Cat Lovers Survey Form", description="How much do you love cats?", inputFields={
    name_input, email_input, age_input, favorite_cat_type_dropdown, number_of_cats_owned_radio, favorite_cat_feature_checkboxes, additional_comments_textarea
})

# Screen
cat_lovers_survey_screen = Screen(name="Cat Lovers Survey Screen", description="Cat Lovers Survey Form Screen", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={
    cat_lovers_survey_form, submit_button
})

# Class and Attributes
# This page is related to the class: CatLoversSurveyForm
# Attributes of this class based on the structural model:
# - name
# - email
# - age
# - favoriteCatType
# - numberOfCatsOwned
# - favoriteCatFeature
# - additionalComments

# Time taken to generate the structural model: 9.88 seconds

# Time taken to generate the GUI model: 29.61 seconds

# Total time taken: 39.49 seconds
