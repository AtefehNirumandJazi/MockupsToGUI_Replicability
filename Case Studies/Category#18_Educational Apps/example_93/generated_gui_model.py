
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="asaidiza_component", description="Asaidiza Educational App")

# Dropdown for selecting a scenario
scenarioDropdown: InputField = InputField(
    name="Scenario Dropdown",
    description="Select a Scenario",
    fieldType="Text",
    validationRules=""
)

# Dropdown for selecting a topic
topicDropdown: InputField = InputField(
    name="Topic Dropdown",
    description="Select a Topic",
    fieldType="Text",
    validationRules=""
)

# Start Quiz Button
startQuizButton: Button = Button(
    name="Start Quiz Button",
    description="Start the quiz",
    label="Start Quiz",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

# Exit Button
exitButton: Button = Button(
    name="Exit Button",
    description="Exit the application",
    label="Exit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Exit
)

# Asaidiza Screen definition
AsaidizaScreen: Screen = Screen(
    name="Asaidiza Screen",
    description="Asaidiza Educational App Screen",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={scenarioDropdown, topicDropdown, startQuizButton, exitButton}
)

# Module definition
AsaidizaModule: Module = Module(
    name="asaidiza_module",
    screens={AsaidizaScreen}
)

# Application definition
AsaidizaApp: Application = Application(
    name="Asaidiza",
    package="com.example.asaidiza",
    versionCode="1",
    versionName="1.0",
    description="An educational app for online safety and cybersecurity.",
    screenCompatibility=True,
    modules={AsaidizaModule}
)

# Class and attributes based on the structural model
# Class: AsaidizaPage
# Attributes: contactEmail, topic, contactName, scenario, contactAddress

# Time taken to generate the structural model: 11.32 seconds

# Time taken to generate the GUI model: 25.68 seconds

# Total time taken: 37.00 seconds
