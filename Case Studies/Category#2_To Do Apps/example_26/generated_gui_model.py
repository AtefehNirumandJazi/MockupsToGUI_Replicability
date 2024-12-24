
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="ToDoComponent", description="To-Do List Application")

# InputField for adding tasks
taskInputField: InputField = InputField(
    name="TaskInput",
    description="Input field for new tasks",
    fieldType="Text",
    validationRules=""
)

# Button for adding tasks
addButton: Button = Button(
    name="AddTaskButton",
    description="Button to add a new task",
    label="+",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add
)

# DataSource for tasks
taskDataSource: ModelElement = ModelElement(
    name="TaskDataSource",
    dataSourceClass=Task,
    fields=[Task_id, Task_description]
)

# List of tasks
taskList: DataList = DataList(
    name="TaskList",
    description="List of tasks",
    list_sources={taskDataSource}
)

# Screen definition
ToDoScreen: Screen = Screen(
    name="ToDoScreen",
    description="Screen for managing tasks",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={taskInputField, addButton, taskList}
)

# Module definition
ToDoModule: Module = Module(
    name="ToDoModule",
    screens={ToDoScreen}
)

# Application definition
ToDoApp: Application = Application(
    name="ToDoApp",
    package="com.example.todoapp",
    versionCode="1",
    versionName="1.0",
    description="A simple to-do list application",
    screenCompatibility=True,
    modules={ToDoModule}
)

# Class and attributes
# This page is related to the "Task" class in the structural model.
# Attributes of the "Task" class: id, description
