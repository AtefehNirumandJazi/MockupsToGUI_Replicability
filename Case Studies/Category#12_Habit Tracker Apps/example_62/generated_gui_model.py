
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="HabitsTrackerComponent", description="Forming Habits Tracker")

# Button1: Mark Complete
markCompleteButton: Button = Button(
    name="MarkCompleteButton",
    description="Mark the habit as complete",
    label="Mark Complete",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Confirm
)

# Button2: View Progress
viewProgressButton: Button = Button(
    name="ViewProgressButton",
    description="View the progress of the habit",
    label="View Progress",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.View
)

# InputField: Enter new habit
newHabitInputField: InputField = InputField(
    name="NewHabitInputField",
    description="Input field for entering a new habit",
    fieldType="Text",
    validationRules=""
)

# Button3: Add Habit
addHabitButton: Button = Button(
    name="AddHabitButton",
    description="Add a new habit",
    label="Add Habit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Screen definition
HabitsTrackerScreen: Screen = Screen(
    name="HabitsTrackerScreen",
    description="Screen for tracking habits",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={markCompleteButton, viewProgressButton, newHabitInputField, addHabitButton}
)

# Module definition
HabitsTrackerModule: Module = Module(
    name="HabitsTrackerModule",
    screens={HabitsTrackerScreen}
)

# Application definition
HabitsTrackerApp: Application = Application(
    name="Forming Habits Tracker",
    package="com.example.habitstracker",
    versionCode="1",
    versionName="1.0",
    description="An application for tracking and managing habits.",
    screenCompatibility=True,
    modules={HabitsTrackerModule}
)

# Class and attributes
# This page is related to the class: HabitsTrackerPage
# Attributes of this class:
# - habitCompletionTime
# - habitDuration
# - habitStartDate
# - habitDescription
# - habitEndDate
# - newHabitInput
# - isHabitActive
# - habitFrequency

# Time taken to generate the structural model: 9.58 seconds

# Time taken to generate the GUI model: 26.14 seconds

# Total time taken: 35.72 seconds
