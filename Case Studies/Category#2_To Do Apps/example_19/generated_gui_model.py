
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="task_component", description="Task Management Interface")

# Input Fields
taskInputField: InputField = InputField(name="Task Input", description="What Do You Need To-Do?", fieldType="Text", validationRules="")
searchInputField: InputField = InputField(name="Search Input", description="Search My Tasks", fieldType="Search", validationRules="")

# Buttons
addButton: Button = Button(name="Add Button", description="Add a new task", label="Add", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)
searchButton: Button = Button(name="Search Button", description="Search tasks", label="Search My Tasks", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Search)
clearCompletedButton: Button = Button(name="Clear Completed Button", description="Clear completed tasks", label="Clear 2 Completed Task(s)", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)
checkAllButton: Button = Button(name="Check All Button", description="Check all tasks", label="Check All Completed", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Confirm)
uncheckAllButton: Button = Button(name="Uncheck All Button", description="Uncheck all tasks", label="Uncheck All Completed", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)
deleteAllButton: Button = Button(name="Delete All Button", description="Delete all tasks", label="Delete All Tasks", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)

# Task List
taskDataSource: ModelElement = ModelElement(name="Task Data Source", dataSourceClass=Task, fields=[Task_title, Task_isCompleted])
taskList: DataList = DataList(name="Task List", description="List of tasks", list_sources={taskDataSource})

# Screen definition
taskScreen: Screen = Screen(name="Task Screen", description="Screen for managing tasks",
                            x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                            view_elements={taskInputField, searchInputField, addButton, searchButton, clearCompletedButton, checkAllButton, uncheckAllButton, deleteAllButton, taskList})

# Module definition
taskModule: Module = Module(name="Task Module", screens={taskScreen})

# Application definition
taskApp: Application = Application(name="Task Management App", package="com.example.taskmanagement", versionCode="1",
                                   versionName="1.0", description="An application for managing tasks",
                                   screenCompatibility=True, modules={taskModule})

# Class and Attributes
# This page is related to the "Task" class in the structural model.
# Attributes of the "Task" class: title, isCompleted
