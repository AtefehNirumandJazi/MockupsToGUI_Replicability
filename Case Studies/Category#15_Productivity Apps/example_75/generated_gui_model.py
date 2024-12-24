
from besser.BUML.metamodel.gui import *

# Input Fields
task_input = InputField(name="Task Input", description="Enter task name", fieldType="Text", validationRules="")
category_input = InputField(name="Category Input", description="Select category", fieldType="Text", validationRules="")
priority_input = InputField(name="Priority Input", description="Select priority", fieldType="Text", validationRules="")
due_date_input = InputField(name="Due Date Input", description="Enter due date", fieldType="Date", validationRules="")

# Button
add_task_button = Button(name="Add Task Button", description="Add a new task", label="Add Task", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Form
task_form = Form(name="Task Form", description="Form to add a new task", inputFields={task_input, category_input, priority_input, due_date_input})

# Screen
task_screen = Screen(name="Task Screen", description="Screen to add a new task", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={task_form, add_task_button})

# Module
task_module = Module(name="Task Module", screens={task_screen})

# Application
task_app = Application(name="Artist Productivity App", package="com.example.artistproductivity", versionCode="1", versionName="1.0", description="App to manage artist tasks", screenCompatibility=True, modules={task_module})

# Class and Attributes
# This page is related to the TaskPage class in the structural model.
# Attributes of TaskPage class:
# - taskName
# - category
# - priority
# - dueDate

# Time taken to generate the structural model: 10.24 seconds

# Time taken to generate the GUI model: 24.05 seconds

# Total time taken: 34.29 seconds
