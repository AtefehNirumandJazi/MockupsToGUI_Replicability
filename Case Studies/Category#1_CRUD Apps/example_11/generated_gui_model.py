
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="my_component", description="Task Management Interface")

# DataSource definition
datasource_task: ModelElement = ModelElement(
    name="Task Data Source",
    dataSourceClass=ToDoTaskPage,
    fields=[ToDoTaskPage_taskName, ToDoTaskPage_taskPriority, ToDoTaskPage_taskStatus, ToDoTaskPage_taskDeadline]
)

# Task List definition
taskList: DataList = DataList(
    name="TaskList",
    description="A list of tasks with details",
    list_sources={datasource_task}
)

# Search InputField
searchField: InputField = InputField(
    name="SearchField",
    description="Search tasks",
    fieldType="Search",
    validationRules=""
)

# Button definitions
searchButton: Button = Button(
    name="SearchButton",
    description="Search tasks",
    label="",
    buttonType=ButtonType.IconButton,
    actionType=ButtonActionType.Search
)

filterButton: Button = Button(
    name="FilterButton",
    description="Filter tasks",
    label="",
    buttonType=ButtonType.IconButton,
    actionType=ButtonActionType.Filter
)

# Task Screen definition
TaskScreen: Screen = Screen(
    name="TaskScreen",
    description="Screen displaying tasks with options to search and filter",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="LargeScreen",
    view_elements={taskList, searchField, searchButton, filterButton}
)

# Module definition
TaskModule: Module = Module(
    name="TaskModule",
    screens={TaskScreen}
)

# Application definition
TaskApp: Application = Application(
    name="Task Management App",
    package="com.example.taskmanagement",
    versionCode="1",
    versionName="1.0",
    description="An application for managing tasks",
    screenCompatibility=True,
    modules={TaskModule}
)

# Class and attributes
# This page is related to the class: ToDoTaskPage
# Attributes of this class: taskName, taskPriority, taskStatus, taskDeadline

# Time taken to generate the structural model: 5.61 seconds

# Time taken to generate the GUI model: 22.43 seconds

# Total time taken: 28.04 seconds
