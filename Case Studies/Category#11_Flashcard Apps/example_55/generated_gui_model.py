
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="flashcard_component", description="Create Flashcard")

# Input fields for FlashcardPage
questionInput: InputField = InputField(name="Question Input", description="Enter the question", fieldType="Text", validationRules="")
answerInput: InputField = InputField(name="Answer Input", description="Enter the answer", fieldType="Text", validationRules="")

# Button for adding a flashcard
addCardButton: Button = Button(name="Add Card Button", description="Add a new flashcard", label="Add Card", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Form for creating a flashcard
flashcardForm: Form = Form(name="Flashcard Form", description="Form to create a flashcard", inputFields={questionInput, answerInput})

# Screen definition
FlashcardScreen: Screen = Screen(name="Create Flashcard Screen", description="Screen for creating a new flashcard",
                                 x_dpi="x_dpi", y_dpi="y_dpi", size="Large", view_elements={flashcardForm, addCardButton})

# Module definition
FlashcardModule: Module = Module(name="Flashcard Module", screens={FlashcardScreen})

# Application definition
FlashcardApp: Application = Application(name="Flashcard App", package="com.example.flashcardapp", versionCode="1",
                                        versionName="1.0", description="An app for creating and managing flashcards.",
                                        screenCompatibility=True, modules={FlashcardModule})

# Class and attributes
# This page is related to the FlashcardPage class in the structural model.
# Attributes of FlashcardPage class:
# - isAnswered: Boolean
# - answer: String
# - createdDate: DateTime
# - question: String
# - category: String
# - lastReviewed: DateTime
# - difficulty: Integer

# Time taken to generate the structural model: 9.91 seconds

# Time taken to generate the GUI model: 19.34 seconds

# Total time taken: 29.25 seconds
