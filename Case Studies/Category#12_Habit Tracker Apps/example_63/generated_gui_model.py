
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="habit_tracker_component", description="Habit Tracker UI")

# Input Fields
habitNameInput: InputField = InputField(name="habitNameInput", description="Enter new habit", fieldType="Text", validationRules="")
weeklyGoalInput: InputField = InputField(name="weeklyGoalInput", description="Weekly goal", fieldType="Number", validationRules="")

# Button
addHabitButton: Button = Button(name="addHabitButton", description="Add Habit", label="Add Habit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Dropdown for Summary Type
summaryTypeDropdown: InputField = InputField(name="summaryTypeDropdown", description="Summary Type", fieldType="Text", validationRules="")

# Progress Summary
progressSummaryList: List = List(name="progressSummaryList", description="Progress Summary", list_sources=set())

# Screen definition
HabitTrackerScreen: Screen = Screen(
    name="HabitTrackerScreen",
    description="Screen for tracking habits",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Small",
    view_elements={habitNameInput, weeklyGoalInput, addHabitButton, summaryTypeDropdown, progressSummaryList}
)

# Module definition
HabitTrackerModule: Module = Module(name="HabitTrackerModule", screens={HabitTrackerScreen})

# Application definition
HabitTrackerApp: Application = Application(
    name="HabitTrackerApp",
    package="com.example.habittracker",
    versionCode="1",
    versionName="1.0",
    description="An application for tracking habits",
    screenCompatibility=True,
    modules={HabitTrackerModule}
)

# Class and Attributes
# This page is related to the class: HabitTrackerPage
# Attributes of this class based on the structural model:
# - habitName: String
# - progressSummary: String
# - weeklyGoal: Integer
# - summaryType: String

# Time taken to generate the structural model: 7.99 seconds

# Time taken to generate the GUI model: 32.42 seconds

# Total time taken: 40.41 seconds
