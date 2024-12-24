
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="do_it_component", description="Task Management Interface")

# InputField
taskInputField: InputField = InputField(
    name="task_input",
    description="Enter a task",
    fieldType="Text",
    validationRules=""
)

# Button
addTaskButton: Button = Button(
    name="add_task_button",
    description="Add a task",
    label="Add Task",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Form
taskForm: Form = Form(
    name="task_form",
    description="Form to add tasks",
    inputFields={taskInputField}
)

# Screen definition
ToDoAppScreen: Screen = Screen(
    name="ToDoAppScreen",
    description="Screen for managing tasks",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Small",
    view_elements={taskForm, addTaskButton}
)

# Module definition
ToDoAppModule: Module = Module(
    name="ToDoAppModule",
    screens={ToDoAppScreen}
)

# Application definition
ToDoApp: Application = Application(
    name="ToDo Application",
    package="com.example.todoapp",
    versionCode="1",
    versionName="1.0",
    description="A simple to-do application",
    screenCompatibility=True,
    modules={ToDoAppModule}
)

# Class and attributes
# This page is related to the class: ToDoAppPage
# Attributes of this class:
# - taskInput: StringType
# - isAddTaskButtonEnabled: BooleanType

# Time taken to generate the structural model: 5.64 seconds

# Time taken to generate the GUI model: 22.22 seconds

# Total time taken: 27.86 seconds
