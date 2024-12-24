
# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="FlashcardApp", description="Flashcard Application")

# Input Fields
questionInput: InputField = InputField(name="Question", description="Enter question here", fieldType="Text", validationRules="")
answerInput: InputField = InputField(name="Answer", description="Enter answer here", fieldType="Text", validationRules="")

# Form
flashcardForm: Form = Form(name="Add New Flashcard", description="Form to add a new flashcard", inputFields={questionInput, answerInput})

# Button
addFlashcardButton: Button = Button(name="Add Flashcard Button", description="Add Flashcard", label="Add Flashcard", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# File Input
restoreBackupFile: InputField = InputField(name="Restore Backup File", description="Choose file", fieldType="File", validationRules="")

# Restore Backup Form
restoreBackupForm: Form = Form(name="Restore Backup", description="Form to restore backup", inputFields={restoreBackupFile})

# Screen definition
flashcardScreen: Screen = Screen(name="Flashcard Screen", description="Screen for managing flashcards", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={flashcardForm, addFlashcardButton, restoreBackupForm})

# Module definition
flashcardModule: Module = Module(name="Flashcard Module", screens={flashcardScreen})

# Application definition
flashcardApp: Application = Application(name="Flashcard Application", package="com.example.flashcardapp", versionCode="1", versionName="1.0", description="An application to manage flashcards", screenCompatibility=True, modules={flashcardModule})

# Class and Attributes
# This page is related to the class: FlashcardApp
# Attributes of this class: question, answer

# Time taken to generate the structural model: 7.49 seconds

# Time taken to generate the GUI model: 22.32 seconds

# Total time taken: 29.82 seconds
