
from besser.BUML.metamodel.gui import *

# Input fields for the FlashcardPage
questionInput: InputField = InputField(
    name="Question Input",
    description="Enter question here",
    fieldType="Text",
    validationRules=""
)

answerInput: InputField = InputField(
    name="Answer Input",
    description="Enter answer here",
    fieldType="Text",
    validationRules=""
)

# Button to add a new flashcard
addFlashcardButton: Button = Button(
    name="Add Flashcard Button",
    description="Add a new flashcard",
    label="Add Flashcard",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# File input for restoring backup
restoreBackupFileInput: InputField = InputField(
    name="Restore Backup File Input",
    description="Choose file",
    fieldType="File",
    validationRules=""
)

# Form for adding a new flashcard
addFlashcardForm: Form = Form(
    name="Add Flashcard Form",
    description="Form to add a new flashcard",
    inputFields={questionInput, answerInput}
)

# Screen for the FlashcardPage
flashcardScreen: Screen = Screen(
    name="Flashcard Screen",
    description="Screen for adding and restoring flashcards",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={addFlashcardForm, addFlashcardButton, restoreBackupFileInput}
)

# Module definition
flashcardModule: Module = Module(
    name="Flashcard Module",
    screens={flashcardScreen}
)

# Application definition
flashcardApp: Application = Application(
    name="Flashcard App",
    package="com.example.flashcardapp",
    versionCode="1",
    versionName="1.0",
    description="An app for creating and managing flashcards.",
    screenCompatibility=True,
    modules={flashcardModule}
)

# Class and attributes related to this page
# Class: FlashcardPage
# Attributes: question, answer, backupFilePath

# Time taken to generate the structural model: 13.60 seconds

# Time taken to generate the GUI model: 26.49 seconds

# Total time taken: 40.09 seconds
