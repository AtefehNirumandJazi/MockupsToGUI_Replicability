
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="todo_component", description="Modern To-Do App Interface")

# InputField for task entry
taskInputField: InputField = InputField(
    name="Task Input Field",
    description="Enter your task",
    fieldType="Text",
    validationRules=""
)

# Button for adding tasks
addButton: Button = Button(
    name="Add Task Button",
    description="Add a new task",
    label="Add",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Button for resetting tasks
resetButton: Button = Button(
    name="Reset Button",
    description="Reset all tasks",
    label="Reset",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Cancel
)

# Labels for task statistics
totalTasksLabel: ViewComponent = ViewComponent(
    name="Total Tasks Label",
    description="Displays total number of tasks"
)

tasksRemainingLabel: ViewComponent = ViewComponent(
    name="Tasks Remaining Label",
    description="Displays number of tasks remaining"
)

tasksCompletedLabel: ViewComponent = ViewComponent(
    name="Tasks Completed Label",
    description="Displays number of tasks completed"
)

# Screen definition
ToDoAppScreen: Screen = Screen(
    name="ToDoAppScreen",
    description="Screen for managing tasks in the To-Do App",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={
        taskInputField, addButton, resetButton,
        totalTasksLabel, tasksRemainingLabel, tasksCompletedLabel
    }
)

# Module definition
ToDoAppModule: Module = Module(
    name="ToDoAppModule",
    screens={ToDoAppScreen}
)

# Application definition
ToDoApp: Application = Application(
    name="Modern To-Do App",
    package="com.example.todoapp",
    versionCode="1",
    versionName="1.0",
    description="A modern to-do application for task management.",
    screenCompatibility=True,
    modules={ToDoAppModule}
)

# Class and attributes related to this page
# Class: ToDoApp
# Attributes: tasksCompleted, taskPriority, totalTasks, tasksRemaining, taskInput, isTaskCompleted, taskDueDate
