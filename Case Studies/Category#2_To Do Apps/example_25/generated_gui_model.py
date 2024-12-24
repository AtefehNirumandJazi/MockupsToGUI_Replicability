
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="ToDoComponent", description="To-Do List Management")

# Menu definition
categoryMenu: Menu = Menu(name="CategoryMenu", description="Choose the name of your To-Do!")
categoryMenu.menuItems = {
    MenuItem(label="Errands"),
    MenuItem(label="Movies"),
    MenuItem(label="Groceries"),
    MenuItem(label="TV Shows")
}

# InputField definition
itemNameInput: InputField = InputField(name="ItemNameInput", description="Enter the name of the item", fieldType="Text")

# Button definition
addItemButton: Button = Button(name="AddItemButton", description="Add a new item to the list", label="+ Add Item", buttonType=ButtonType.RaisedButton)

# Form definition
toDoForm: Form = Form(name="ToDoForm", description="Form to add a new to-do item")
toDoForm.inputFields = {itemNameInput}

# Screen definition
toDoScreen: Screen = Screen(name="ToDoScreen", description="Screen for managing to-do items", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium")
toDoScreen.view_elements = {categoryMenu, toDoForm, addItemButton}

# Module definition
toDoModule: Module = Module(name="ToDoModule", screens={toDoScreen})

# Application definition
toDoApp: Application = Application(name="ToDoApp", package="com.example.todoapp", versionCode="1", versionName="1.0", description="A simple to-do list application", screenCompatibility=True, modules={toDoModule})

# Class and attributes
# This page is related to the class: ToDoPage
# Attributes of this class based on the structural model:
# - itemName: StringType
# - updatedAt: DateTimeType
# - priority: IntegerType
# - dueDate: DateType
# - createdAt: DateTimeType
# - isCompleted: BooleanType
# - category: StringType
