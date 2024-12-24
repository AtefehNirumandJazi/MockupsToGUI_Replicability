
from besser.BUML.metamodel.gui import *

# ViewComponent definitions
titleImage: Image = Image(name="Title Image")
titleText: ViewComponent = ViewComponent(name="Title Text", description="Animal Flashcards")

# InputField
guessInputField: InputField = InputField(
    name="Guess Input Field",
    description="Input field for guessing the Hmong word",
    fieldType="Text",
    validationRules=""
)

# Buttons
showCardButton: Button = Button(
    name="Show Card Button",
    description="Button to show a card",
    label="Show Card",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.View
)

submitButton: Button = Button(
    name="Submit Button",
    description="Button to submit the guess",
    label="Submit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.SubmitForm
)

resetScoreButton: Button = Button(
    name="Reset Score Button",
    description="Button to reset the score",
    label="Reset Score",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Reset
)

resetDeckButton: Button = Button(
    name="Reset Deck Button",
    description="Button to reset the deck",
    label="Reset Deck",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Reset
)

# Checkbox
autoAudioCheckbox: ViewComponent = ViewComponent(
    name="Auto-Audio Checkbox",
    description="Checkbox to enable or disable auto-audio"
)

# Current Score Display
currentScoreDisplay: ViewComponent = ViewComponent(
    name="Current Score Display",
    description="Display for the current score"
)

# Settings Container
settingsContainer: ViewContainer = ViewContainer(
    name="Settings Container",
    description="Container for settings elements",
    view_elements={resetScoreButton, resetDeckButton, autoAudioCheckbox}
)

# Screen definition
AnimalFlashcardsScreen: Screen = Screen(
    name="Animal Flashcards Screen",
    description="Screen for animal flashcards game",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={
        titleImage, titleText, guessInputField, showCardButton, submitButton, currentScoreDisplay, settingsContainer
    }
)

# Module definition
AnimalFlashcardsModule: Module = Module(
    name="Animal Flashcards Module",
    screens={AnimalFlashcardsScreen}
)

# Application definition
AnimalFlashcardsApp: Application = Application(
    name="Animal Flashcards Application",
    package="com.example.animalflashcards",
    versionCode="1",
    versionName="1.0",
    description="An application for learning Hmong words through animal flashcards.",
    screenCompatibility=True,
    modules={AnimalFlashcardsModule}
)

# Class and Attributes
# This page is related to the class: AnimalFlashcardsPage
# Attributes of this class:
# - currentScore
# - inputField
# - prompt
# - autoAudioEnabled
# - title

# Time taken to generate the structural model: 12.21 seconds

# Time taken to generate the GUI model: 30.41 seconds

# Total time taken: 42.62 seconds
