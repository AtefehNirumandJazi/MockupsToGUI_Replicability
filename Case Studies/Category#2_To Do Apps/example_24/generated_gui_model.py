
from besser.BUML.metamodel.gui import *

# InputField for adding a new item
addItemInput: InputField = InputField(
    name="addItemInput",
    description="Input field to add a new item",
    fieldType="Text",
    validationRules=""
)

# Button to add a new item
addButton: Button = Button(
    name="addButton",
    description="Button to add a new item",
    label="Add",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Add
)

# DataSource for Todo items
todoDataSource: ModelElement = ModelElement(
    name="TodoDataSource",
    dataSourceClass=TodoItem,
    fields=[TodoItem_title, TodoItem_isCompleted]
)

# List for Todo items
todoList: DataList = DataList(
    name="TodoList",
    description="List of todo items",
    list_sources={todoDataSource}
)

# Button to edit a todo item
editButton: Button = Button(
    name="editButton",
    description="Button to edit a todo item",
    label="Edit",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.OpenForm
)

# Button to delete a todo item
deleteButton: Button = Button(
    name="deleteButton",
    description="Button to delete a todo item",
    label="Delete",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Delete
)

# Screen for the Todo application
todoScreen: Screen = Screen(
    name="TodoScreen",
    description="Screen for managing todo items",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Small",
    view_elements={addItemInput, addButton, todoList, editButton, deleteButton}
)

# Module for the Todo application
todoModule: Module = Module(
    name="TodoModule",
    screens={todoScreen}
)

# Application definition
todoApp: Application = Application(
    name="Todo Application",
    package="com.example.todoapp",
    versionCode="1",
    versionName="1.0",
    description="A simple todo application",
    screenCompatibility=True,
    modules={todoModule}
)
