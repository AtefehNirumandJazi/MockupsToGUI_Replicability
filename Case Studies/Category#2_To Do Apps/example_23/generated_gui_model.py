
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="ToDoAppComponent", description="To Do App Interface")

# InputField for adding tasks
taskInputField: InputField = InputField(
    name="Task Input Field",
    description="Field to add new tasks",
    fieldType="Text",
    validationRules="required"
)

# Button for adding tasks
addTaskButton: Button = Button(
    name="Add Task Button",
    description="Button to add a new task",
    label="Add",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add
)

# Screen definition
ToDoAppScreen: Screen = Screen(
    name="ToDoAppScreen",
    description="Screen for managing to-do tasks",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={taskInputField, addTaskButton}
)

# Module definition
ToDoAppModule: Module = Module(
    name="ToDoAppModule",
    screens={ToDoAppScreen}
)

# Application definition
ToDoApp: Application = Application(
    name="ToDoApp",
    package="com.example.todoapp",
    versionCode="1",
    versionName="1.0",
    description="A simple to-do list application",
    screenCompatibility=True,
    modules={ToDoAppModule}
)

# Class and attributes
# This page is related to the class: ToDoAppPage
# Attributes of this class:
# - taskDescription: String
# - taskInputField: String
# - isCompleted: Boolean
# - creationTime: DateTime
# - pageTitle: String
# - dueDate: Date
