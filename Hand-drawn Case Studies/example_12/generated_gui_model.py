
from library import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="library_system", description="Library System Interface")

# InputFields for LibraryPage
nameInput: InputField = InputField(name="Name", description="Book Name", fieldType="Text", validationRules="")
authorInput: InputField = InputField(name="Author", description="Book Author", fieldType="Text", validationRules="")
publisherInput: InputField = InputField(name="Publisher", description="Book Publisher", fieldType="Text", validationRules="")
pagesInput: InputField = InputField(name="Number of Pages", description="Page Count", fieldType="Number", validationRules="")
serialInput: InputField = InputField(name="Serial Number", description="Book Serial Number", fieldType="Number", validationRules="")

# Form for adding a book
addBookForm: Form = Form(name="AddBookForm", description="Form to add a new book", inputFields={nameInput, authorInput, publisherInput, pagesInput, serialInput})

# Add Button
addButton: Button = Button(name="AddButton", description="Add a new book", label="ADD", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# DataSource for LibraryPage
datasource_libraryPage: ModelElement = ModelElement(name="LibraryPage Data Source", dataSourceClass=LibraryPage, fields=[LibraryPage_bookName, LibraryPage_bookAuthor, LibraryPage_bookPublisher, LibraryPage_pageCount, LibraryPage_bookSerialNumber])

# List for displaying books
bookList: DataList = DataList(name="BookList", description="List of books", list_sources={datasource_libraryPage})

# LibraryPage Screen definition
LibraryPageScreen: Screen = Screen(name="LibraryPageScreen", description="Screen for managing library books",
                                   x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={addBookForm, addButton, bookList})

# Module definition
LibraryModule: Module = Module(name="LibraryModule", screens={LibraryPageScreen})

# Application definition
LibraryApp: Application = Application(name="Library Management App", package="com.example.librarymanagement", versionCode="1",
                                      versionName="1.0", description="An application for managing library books.",
                                      screenCompatibility=True, modules={LibraryModule})

# Class and attributes
# Class: LibraryPage
# Attributes: bookPublisher, pageCount, bookName, bookSerialNumber, bookAuthor

# Time taken to generate the structural model: 11.20 seconds

# Time taken to generate the GUI model: 24.00 seconds

# Total time taken: 35.20 seconds
