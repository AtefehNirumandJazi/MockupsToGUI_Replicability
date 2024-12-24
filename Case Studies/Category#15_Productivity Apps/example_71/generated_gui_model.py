
# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="productivity_app_component", description="Productivity App Interface")

# Input Fields
taskInputField: InputField = InputField(name="taskInput", description="Enter task", fieldType="Text", validationRules="")
priorityInputField: InputField = InputField(name="priorityInput", description="Select priority", fieldType="Text", validationRules="")
reminderInputField: InputField = InputField(name="reminderInput", description="Notify me when this task is due", fieldType="Boolean", validationRules="")

# Buttons
addButton: Button = Button(name="addButton", description="Add task", label="Add", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)
deleteButton: Button = Button(name="deleteButton", description="Delete task", label="Delete", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)
deleteAllButton: Button = Button(name="deleteAllButton", description="Delete all tasks", label="Delete all tasks", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)
saveButton: Button = Button(name="saveButton", description="Save settings", label="Save", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

# Lists
taskList: List = List(name="taskList", description="List of tasks", list_sources=set())

# Forms
taskForm: Form = Form(name="taskForm", description="Form to add tasks", inputFields={taskInputField, priorityInputField, reminderInputField})
settingsForm: Form = Form(name="settingsForm", description="Settings form", inputFields={priorityInputField, reminderInputField})

# Screens
taskScreen: Screen = Screen(name="taskScreen", description="Screen for managing tasks", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={taskForm, addButton, taskList, deleteAllButton, deleteButton})
settingsScreen: Screen = Screen(name="settingsScreen", description="Screen for settings", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={settingsForm, saveButton})

# Module definition
productivityModule: Module = Module(name="productivityModule", screens={taskScreen, settingsScreen})

# Application definition
productivityApp: Application = Application(name="ProductivityApp", package="com.example.productivityapp", versionCode="1", versionName="1.0", description="A productivity application for managing tasks.", screenCompatibility=True, modules={productivityModule})

# Class and Attributes
# This page is related to the "Task" class in the structural model.
# Attributes of the "Task" class:
# - taskName (StringType)
# - priorityLevel (StringType)
# - hasReminder (BooleanType)

# Time taken to generate the structural model: 13.59 seconds

# Time taken to generate the GUI model: 33.32 seconds

# Total time taken: 46.90 seconds
