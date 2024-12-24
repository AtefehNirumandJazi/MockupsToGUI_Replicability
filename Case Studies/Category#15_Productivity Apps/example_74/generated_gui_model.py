
from besser.BUML.metamodel.gui import *

# Input Fields
task_input = InputField(name="Task Input", description="Add a new task", fieldType="Text", validationRules="")
priority_input = InputField(name="Priority Input", description="Select priority", fieldType="Text", validationRules="")
deadline_input = InputField(name="Deadline Input", description="Select deadline", fieldType="Date", validationRules="")

# Buttons
add_task_button = Button(name="Add Task Button", description="Add Task", label="Add Task", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)
reset_tasks_button = Button(name="Reset Tasks Button", description="Reset Tasks", label="Reset Tasks", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)

# Form
todo_form = Form(name="To-Do Form", description="Form to add tasks", inputFields={task_input, priority_input, deadline_input})

# Screen
todo_screen = Screen(name="To-Do List Screen", description="Screen for managing to-do list", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={todo_form, add_task_button, reset_tasks_button})

# Module
todo_module = Module(name="To-Do Module", screens={todo_screen})

# Application
todo_app = Application(name="To-Do Application", package="com.example.todolist", versionCode="1", versionName="1.0", description="A simple to-do list application", screenCompatibility=True, modules={todo_module})

# Class and Attributes
# This page is related to the class: ToDoListPage
# Attributes of this class:
# - taskName: StringType
# - priorityLevel: StringType
# - dueDate: DateType

# Time taken to generate the structural model: 9.26 seconds

# Time taken to generate the GUI model: 48.38 seconds

# Total time taken: 57.64 seconds
