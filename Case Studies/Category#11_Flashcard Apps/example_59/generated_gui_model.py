
from besser.BUML.metamodel.gui import *

# ViewComponent definitions
add_flashcard_button = Button(
    name="AddFlashcardButton",
    description="Button to add a new flashcard",
    label="Add Flashcard",
    buttonType=ButtonType.RaisedButton
)

import_flashcards_button = Button(
    name="ImportFlashcardsButton",
    description="Button to import flashcards",
    label="Import Flashcards",
    buttonType=ButtonType.RaisedButton
)

create_new_set_button = Button(
    name="CreateNewSetButton",
    description="Button to create a new flashcard set",
    label="Create New Set",
    buttonType=ButtonType.RaisedButton
)

import_set_button = Button(
    name="ImportSetButton",
    description="Button to import a flashcard set",
    label="Import Set",
    buttonType=ButtonType.RaisedButton
)

delete_set_button = Button(
    name="DeleteSetButton",
    description="Button to delete a flashcard set",
    label="Delete Set",
    buttonType=ButtonType.RaisedButton
)

export_set_button = Button(
    name="ExportSetButton",
    description="Button to export a flashcard set",
    label="Export Set",
    buttonType=ButtonType.RaisedButton
)

start_practice_button = Button(
    name="StartPracticeButton",
    description="Button to start practice mode",
    label="Start Practice",
    buttonType=ButtonType.RaisedButton
)

# InputField definitions
english_word_input = InputField(
    name="EnglishWordInput",
    description="Input field for English word",
    fieldType="Text"
)

spanish_translation_input = InputField(
    name="SpanishTranslationInput",
    description="Input field for Spanish translation",
    fieldType="Text"
)

bulk_import_textarea = InputField(
    name="BulkImportTextarea",
    description="Textarea for bulk import of flashcards",
    fieldType="Text"
)

new_set_name_input = InputField(
    name="NewSetNameInput",
    description="Input field for new set name",
    fieldType="Text"
)

file_input = InputField(
    name="FileInput",
    description="File input for importing sets",
    fieldType="File"
)

# Screen definition
flashcard_app_screen = Screen(
    name="FlashcardAppScreen",
    description="Screen for the Flashcard App",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={
        add_flashcard_button,
        import_flashcards_button,
        create_new_set_button,
        import_set_button,
        delete_set_button,
        export_set_button,
        start_practice_button,
        english_word_input,
        spanish_translation_input,
        bulk_import_textarea,
        new_set_name_input,
        file_input
    }
)

# Module definition
flashcard_module = Module(
    name="FlashcardModule",
    screens={flashcard_app_screen}
)

# Application definition
flashcard_app = Application(
    name="FlashcardApp",
    package="com.example.flashcardapp",
    versionCode="1",
    versionName="1.0",
    description="An application for managing flashcards",
    screenCompatibility=True,
    modules={flashcard_module}
)

# Class and Attributes
# This page is related to the class: AddNewFlashcard
# Attributes of this class based on the structural model:
# - englishWord
# - spanishTranslation

# Time taken to generate the structural model: 13.58 seconds

# Time taken to generate the GUI model: 29.95 seconds

# Total time taken: 43.52 seconds
