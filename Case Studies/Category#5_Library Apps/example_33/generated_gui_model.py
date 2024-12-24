
from library import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="library_system_component", description="Library System Interface")

# Input Fields
nameInput: InputField = InputField(name="Name Input", description="Input for book name", fieldType="Text", validationRules="")
authorInput: InputField = InputField(name="Author Input", description="Input for author name", fieldType="Text", validationRules="")
publisherInput: InputField = InputField(name="Publisher Input", description="Input for publisher name", fieldType="Text", validationRules="")
pageCountInput: InputField = InputField(name="Page Count Input", description="Input for number of pages", fieldType="Number", validationRules="")
serialNumberInput: InputField = InputField(name="Serial Number Input", description="Input for serial number", fieldType="Text", validationRules="")

# Form
libraryForm: Form = Form(name="Library Form", description="Form to add a new book", inputFields={nameInput, authorInput, publisherInput, pageCountInput, serialNumberInput})

# Add Button
addButton: Button = Button(name="Add Button", description="Button to add a new book", label="ADD", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Data Source
datasource_library: ModelElement = ModelElement(name="Library Data Source", dataSourceClass=LibraryPage, fields={LibraryPage_bookName, LibraryPage_bookAuthor, LibraryPage_bookPublisher, LibraryPage_pageCount, LibraryPage_bookSerialNumber})

# Library List
libraryList: DataList = DataList(name="Library List", description="List of books in the library", list_sources={datasource_library})

# Library Screen
LibraryScreen: Screen = Screen(name="Library Screen", description="Screen for managing library books", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={libraryForm, addButton, libraryList})

# Module definition
LibraryModule: Module = Module(name="Library Module", screens={LibraryScreen})

# Application definition
LibraryApp: Application = Application(name="Library Management App", package="com.example.librarymanagement", versionCode="1", versionName="1.0", description="An application for managing library books.", screenCompatibility=True, modules={LibraryModule})

# Class and Attributes
# This page is related to the class: LibraryPage
# Attributes of this class: bookAuthor, bookPublisher, bookName, pageCount, bookSerialNumber

# Time taken to generate the structural model: 10.13 seconds

# Time taken to generate the GUI model: 33.75 seconds

# Total time taken: 43.89 seconds
