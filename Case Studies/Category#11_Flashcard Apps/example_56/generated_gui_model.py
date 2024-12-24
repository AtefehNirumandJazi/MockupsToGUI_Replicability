
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="flashcard_app_component", description="Flashcard App Interface")

# Input Fields
questionInput: InputField = InputField(name="question_input", description="Enter question", fieldType="Text", validationRules="")
answerInput: InputField = InputField(name="answer_input", description="Enter answer", fieldType="Text", validationRules="")
bulkInput: InputField = InputField(name="bulk_input", description="Enter term and definition pairs separated by a semicolon (e.g., term1: definition1; term2: definition2;)", fieldType="Text", validationRules="")

# Buttons
addCardButton: Button = Button(name="add_card_button", description="Add Card", label="Add Card", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)
addBulkButton: Button = Button(name="add_bulk_button", description="Add Cards in Bulk", label="Add Cards in Bulk", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)
nextCardButton: Button = Button(name="next_card_button", description="Next Card", label="Next Card", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Next)

# Screen definition
FlashcardAppScreen: Screen = Screen(
    name="FlashcardAppScreen",
    description="Flashcard App Interface",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={questionInput, answerInput, bulkInput, addCardButton, addBulkButton, nextCardButton}
)

# Module definition
FlashcardAppModule: Module = Module(name="flashcard_app_module", screens={FlashcardAppScreen})

# Application definition
FlashcardApp: Application = Application(
    name="Flashcard App",
    package="com.example.flashcardapp",
    versionCode="1",
    versionName="1.0",
    description="A simple flashcard application.",
    screenCompatibility=True,
    modules={FlashcardAppModule}
)

# Class and attributes
# This page is related to the class: FlashcardApp
# Attributes of this class based on the structural model:
# - message
# - answer
# - question
# - bulkInput

# Time taken to generate the structural model: 9.46 seconds

# Time taken to generate the GUI model: 25.68 seconds

# Total time taken: 35.15 seconds
