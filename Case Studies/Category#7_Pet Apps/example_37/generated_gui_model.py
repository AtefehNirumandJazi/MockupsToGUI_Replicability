
from besser.BUML.metamodel.gui import *

# Input Fields
name_input = InputField(name="Name", description="Type in Your Name", fieldType="Text")
email_input = InputField(name="Email Address", description="Type in Your Email", fieldType="Email")
age_input = InputField(name="Age (Optional)", description="Age", fieldType="Number")

# Dropdown for Pet Type
pet_type_dropdown = InputField(name="Select type of Pet", description="Select an animal", fieldType="Text")

# Radio Buttons for Pet Gender
pet_gender_male = InputField(name="Pet Gender Male", description="Male", fieldType="Text")
pet_gender_female = InputField(name="Pet Gender Female", description="Female", fieldType="Text")

# Checkboxes for Pet Personality
pet_personality_relaxed = InputField(name="Relaxed", description="Relaxed", fieldType="Text")
pet_personality_playful = InputField(name="Playful", description="Playful", fieldType="Text")
pet_personality_loyal = InputField(name="Loyal", description="Loyal", fieldType="Text")
pet_personality_lazy = InputField(name="Lazy", description="Lazy", fieldType="Text")
pet_personality_hyper = InputField(name="Hyper", description="Hyper", fieldType="Text")
pet_personality_nice = InputField(name="Nice", description="Nice", fieldType="Text")
pet_personality_timid = InputField(name="Timid", description="Timid", fieldType="Text")
pet_personality_fierce = InputField(name="Fierce", description="Fierce", fieldType="Text")
pet_personality_silly = InputField(name="Silly", description="Silly", fieldType="Text")
pet_personality_independent = InputField(name="Independent", description="Independent", fieldType="Text")

# Text Area for Comments
comments_input = InputField(name="Comments", description="Type in Your Comments here...", fieldType="Text")

# Submit Button
submit_button = Button(name="Submit", description="Submit the survey", label="Submit", buttonType=ButtonType.RaisedButton)

# Form
favorite_pet_survey_form = Form(
    name="Favorite Pet Survey Form",
    description="Survey Form for Favorite Pet",
    inputFields={
        name_input, email_input, age_input, pet_type_dropdown,
        pet_gender_male, pet_gender_female,
        pet_personality_relaxed, pet_personality_playful, pet_personality_loyal,
        pet_personality_lazy, pet_personality_hyper, pet_personality_nice,
        pet_personality_timid, pet_personality_fierce, pet_personality_silly,
        pet_personality_independent, comments_input
    }
)

# Screen
favorite_pet_survey_screen = Screen(
    name="Favorite Pet Survey Screen",
    description="Screen for Favorite Pet Survey",
    x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
    view_elements={favorite_pet_survey_form, submit_button}
)

# Module
favorite_pet_survey_module = Module(
    name="Favorite Pet Survey Module",
    screens={favorite_pet_survey_screen}
)

# Application
favorite_pet_survey_app = Application(
    name="Favorite Pet Survey App",
    package="com.example.favoritepetsurvey",
    versionCode="1",
    versionName="1.0",
    description="An application to survey favorite pets.",
    screenCompatibility=True,
    modules={favorite_pet_survey_module}
)

# Class and Attributes
# This page is related to the class: FavoritePetSurvey
# Attributes of this class:
# - petPersonality
# - emailAddress
# - age
# - comments
# - petType
# - petGender
# - name

# Time taken to generate the structural model: 10.06 seconds

# Time taken to generate the GUI model: 38.24 seconds

# Total time taken: 48.29 seconds
