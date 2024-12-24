
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="task_component", description="Task Management Interface")

# InputField for adding tasks
taskInputField: InputField = InputField(name="taskInput", description="Input field for new tasks", fieldType="Text")

# Search InputField
searchTaskField: InputField = InputField(name="searchTask", description="Search field for tasks", fieldType="Search")

# Buttons
deleteCompletedButton: Button = Button(name="deleteCompletedButton", description="Delete completed tasks", label="Delete 2 Completed", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)
markAllCompletedButton: Button = Button(name="markAllCompletedButton", description="Mark all tasks as completed", label="Mark All Completed", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Confirm)
unmarkAllCompletedButton: Button = Button(name="unmarkAllCompletedButton", description="Unmark all tasks as completed", label="Unmark All Completed", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)
deleteAllButton: Button = Button(name="deleteAllButton", description="Delete all tasks", label="Delete All", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)
clearLocalStorageButton: Button = Button(name="clearLocalStorageButton", description="Clear local storage", label="Clear My Local Storage", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)

# Task List
taskDataSource: ModelElement = ModelElement(name="Task Data Source", dataSourceClass=Task, fields=[Task_name, Task_isDone])
taskList: DataList = DataList(name="taskList", description="List of tasks", list_sources={taskDataSource})

# Task Screen definition
TaskScreen: Screen = Screen(name="TaskScreen", description="Screen for managing tasks",
                            x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                            view_elements={taskInputField, searchTaskField, deleteCompletedButton, markAllCompletedButton, unmarkAllCompletedButton, deleteAllButton, clearLocalStorageButton, taskList})

# Module definition
TaskModule: Module = Module(name="task_module", screens={TaskScreen})

# Application definition
TaskApp: Application = Application(name="Task Management App", package="com.example.taskmanagement", versionCode="1",
                                   versionName="1.0", description="An application for managing tasks.",
                                   screenCompatibility=True, modules={TaskModule})

# Class and Attributes
# This page is related to the Task class in the structural model.
# Attributes of the Task class: name, isDone
