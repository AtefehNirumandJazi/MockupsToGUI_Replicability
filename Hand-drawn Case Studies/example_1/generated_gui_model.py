
from besser.BUML.metamodel.gui import *

# Input Fields
name_input = InputField(name="Name", description="Type in your Name", fieldType="Text")
email_input = InputField(name="Email Address", description="Type in your Email", fieldType="Email")
age_input = InputField(name="Age (optional)", description="Age", fieldType="Number")

# Dropdown for Pet Type
pet_type_dropdown = InputField(name="Select type of pet", description="Select an animal", fieldType="Text")

# Radio Buttons for Pet Gender
pet_gender_male = InputField(name="Pet Gender Male", description="Male", fieldType="Text")
pet_gender_female = InputField(name="Pet Gender Female", description="Female", fieldType="Text")

# Checkboxes for Pet Personality
pet_personality_relaxed = InputField(name="Pet Personality Relaxed", description="Relaxed", fieldType="Text")
pet_personality_playful = InputField(name="Pet Personality Playful", description="Playful", fieldType="Text")
pet_personality_loyal = InputField(name="Pet Personality Loyal", description="Loyal", fieldType="Text")
pet_personality_lazy = InputField(name="Pet Personality Lazy", description="Lazy", fieldType="Text")
pet_personality_hyper = InputField(name="Pet Personality Hyper", description="Hyper", fieldType="Text")
pet_personality_nice = InputField(name="Pet Personality Nice", description="Nice", fieldType="Text")
pet_personality_timid = InputField(name="Pet Personality Timid", description="Timid", fieldType="Text")
pet_personality_fierce = InputField(name="Pet Personality Fierce", description="Fierce", fieldType="Text")
pet_personality_silly = InputField(name="Pet Personality Silly", description="Silly", fieldType="Text")
pet_personality_independent = InputField(name="Pet Personality Independent", description="Independent", fieldType="Text")

# Text Area for Least Favorite Pet Comments
least_favorite_pet_comments = InputField(name="Least Favorite Pet Comments", description="Type in your comments here...", fieldType="Text")

# Submit Button
submit_button = Button(name="Submit", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton)

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
        pet_personality_independent, least_favorite_pet_comments
    }
)

# Screen
favorite_pet_survey_screen = Screen(
    name="Favorite Pet Survey Screen",
    description="Screen for Favorite Pet Survey",
    x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
    view_elements={favorite_pet_survey_form, submit_button}
)

# Class and Attributes
# This page is related to the class: FavoritePetSurvey
# Attributes of this class:
# - age
# - petType
# - petGender
# - email
# - name
# - petPersonality
# - leastFavoritePetComments

# Time taken to generate the structural model: 9.58 seconds

# Time taken to generate the GUI model: 36.42 seconds

# Total time taken: 45.99 seconds
