
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="habit_tracker_component", description="Habit Tracker UI")

# Input Fields
habitNameInput: InputField = InputField(name="habitNameInput", description="Enter new habit", fieldType="Text", validationRules="")
weeklyGoalInput: InputField = InputField(name="weeklyGoalInput", description="Weekly goal", fieldType="Number", validationRules="")

# Button
addHabitButton: Button = Button(name="addHabitButton", description="Add Habit", label="Add Habit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Dropdown
timePeriodDropdown: InputField = InputField(name="timePeriodDropdown", description="Select time period", fieldType="Text", validationRules="")

# Text
progressSummaryText: ViewComponent = ViewComponent(name="progressSummaryText", description="Progress Summary")
summaryText: ViewComponent = ViewComponent(name="summaryText", description="Summary")
noHabitsText: ViewComponent = ViewComponent(name="noHabitsText", description="No habits tracked yet.")

# Screen definition
HabitTrackerScreen: Screen = Screen(
    name="HabitTrackerScreen",
    description="Screen for tracking habits",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Small",
    view_elements={
        habitNameInput, weeklyGoalInput, addHabitButton, timePeriodDropdown,
        progressSummaryText, summaryText, noHabitsText
    }
)

# Time taken to generate the structural model: 9.06 seconds

# Time taken to generate the GUI model: 22.74 seconds

# Total time taken: 31.80 seconds
