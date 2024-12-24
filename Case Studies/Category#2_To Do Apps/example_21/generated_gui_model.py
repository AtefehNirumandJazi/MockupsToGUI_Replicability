
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="todo_app_component", description="To-Do App Interface")

# InputField for adding a new task
addTaskInput: InputField = InputField(name="Add New Task", description="Input field for adding a new task", fieldType="Text", validationRules="")

# Button for adding a task
addTaskButton: Button = Button(name="Add Task Button", description="Button to add a new task", label="Add Task", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Incomplete Tasks List
incompleteTasksList: DataList = DataList(name="Incomplete Tasks List", description="List of incomplete tasks", list_sources=set())

# Completed Tasks List with delete button
completedTasksList: DataList = DataList(name="Completed Tasks List", description="List of completed tasks", list_sources=set())
deleteTaskButton: Button = Button(name="Delete Task Button", description="Button to delete a completed task", label="Delete", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Delete)

# Screen definition
ToDoAppScreen: Screen = Screen(name="ToDoAppScreen", description="Screen for managing tasks in the To-Do App",
                               x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                               view_elements={addTaskInput, addTaskButton, incompleteTasksList, completedTasksList, deleteTaskButton})

# Module definition
ToDoAppModule: Module = Module(name="ToDoAppModule", screens={ToDoAppScreen})

# Application definition
ToDoApp: Application = Application(name="To-Do App", package="com.example.todoapp", versionCode="1",
                                   versionName="1.0", description="A simple to-do application for managing tasks.",
                                   screenCompatibility=True, modules={ToDoAppModule})

# Class and attributes
# This page is related to the "Task" class in the structural model.
# Attributes of the "Task" class: dueDate, name, priority, isComplete

# Time taken to generate the structural model: 7.88 seconds

# Time taken to generate the GUI model: 25.37 seconds

# Total time taken: 33.25 seconds
