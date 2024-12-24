
from besser.BUML.metamodel.gui import *

# Input Fields
questionInput: InputField = InputField(
    name="questionInput",
    description="Enter question",
    fieldType="Text",
    validationRules=""
)

answerInput: InputField = InputField(
    name="answerInput",
    description="Enter answer",
    fieldType="Text",
    validationRules=""
)

# Buttons
createFlashcardButton: Button = Button(
    name="createFlashcardButton",
    description="Create Flashcard",
    label="Create Flashcard",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

startGameButton: Button = Button(
    name="startGameButton",
    description="Start Game",
    label="Start Game",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

# Form
flashcardForm: Form = Form(
    name="flashcardForm",
    description="Create Flashcard",
    inputFields={questionInput, answerInput}
)

# List
flashcardsList: List = List(
    name="flashcardsList",
    description="Flashcards",
    list_sources=set()
)

# Screen
flashcardScreen: Screen = Screen(
    name="FlashcardScreen",
    description="Flashcard Management",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={flashcardForm, createFlashcardButton, startGameButton, flashcardsList}
)

# Class and Attributes
# This page is related to the Flashcard class in the structural model.
# Attributes of the Flashcard class:
# - question
# - answer

# Time taken to generate the structural model: 17.97 seconds

# Time taken to generate the GUI model: 18.93 seconds

# Total time taken: 36.90 seconds
