
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="SaidizaPageComponent", description="Saidiza Page Interface")

# Dropdown for selecting a scenario
scenarioDropdown: InputField = InputField(
    name="ScenarioDropdown",
    description="Select a Scenario",
    fieldType="Text",
    validationRules=""
)

# Dropdown for selecting a topic
topicDropdown: InputField = InputField(
    name="TopicDropdown",
    description="Select a Topic",
    fieldType="Text",
    validationRules=""
)

# Start Quiz Button
startQuizButton: Button = Button(
    name="StartQuizButton",
    description="Start the quiz",
    label="Start Quiz",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

# Exit Button
exitButton: Button = Button(
    name="ExitButton",
    description="Exit the application",
    label="Exit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Exit
)

# Saidiza Page Screen definition
SaidizaPageScreen: Screen = Screen(
    name="SaidizaPageScreen",
    description="Welcome to Saidiza, an educational app designed to teach children about online safety and cybersecurity.",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={scenarioDropdown, topicDropdown, startQuizButton, exitButton}
)

# Module definition
SaidizaModule: Module = Module(
    name="SaidizaModule",
    screens={SaidizaPageScreen}
)

# Application definition
SaidizaApp: Application = Application(
    name="SaidizaApp",
    package="com.example.saidiza",
    versionCode="1",
    versionName="1.0",
    description="Saidiza educational app for online safety and cybersecurity.",
    screenCompatibility=True,
    modules={SaidizaModule}
)

# Class and attributes related to this page
# Class: SaidizaPage
# Attributes: page_load_time, user_id, last_accessed, topic, is_active, scenario

# Time taken to generate the structural model: 9.71 seconds

# Time taken to generate the GUI model: 32.90 seconds

# Total time taken: 42.62 seconds
