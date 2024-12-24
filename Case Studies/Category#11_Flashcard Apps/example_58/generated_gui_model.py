
# Import necessary classes from the GUI metamodel
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(
    name="project_ideas_page",
    description="The one-stop destination for project ideas."
)

# Button for getting random project ideas
getRandomIdeasButton: Button = Button(
    name="Get Random Ideas Button",
    description="Get random project ideas",
    label="Get random Project Idea",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

# Buttons for choosing a theme
workFromHomeButton: Button = Button(
    name="Work From Home Button",
    description="Choose Work From Home theme",
    label="Work From Home",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

farmingButton: Button = Button(
    name="Farming Button",
    description="Choose Farming theme",
    label="Farming",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

fitnessButton: Button = Button(
    name="Fitness Button",
    description="Choose Fitness theme",
    label="Fitness",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

natureButton: Button = Button(
    name="Nature Button",
    description="Choose Nature theme",
    label="Nature",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

educationButton: Button = Button(
    name="Education Button",
    description="Choose Education theme",
    label="Education",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

# Button for project ideas for job resume
jobResumeIdeasButton: Button = Button(
    name="Job Resume Ideas Button",
    description="Get project ideas for job resume",
    label="Get the Idea",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

# Button for project ideas using data structures and algorithms
dataStructuresIdeasButton: Button = Button(
    name="Data Structures Ideas Button",
    description="Get project ideas using data structures and algorithms",
    label="Get the Idea",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

# Input field for suggesting a feature
suggestFeatureInput: InputField = InputField(
    name="Suggest Feature Input",
    description="Input field for suggesting a feature",
    fieldType="Text",
    validationRules=""
)

# Label for visitor count
visitorCountLabel: ViewComponent = ViewComponent(
    name="Visitor Count Label",
    description="Label for displaying the total number of visitors"
)

# Screen definition
projectIdeasScreen: Screen = Screen(
    name="Project Ideas Screen",
    description="Screen for project ideas",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={
        getRandomIdeasButton,
        workFromHomeButton,
        farmingButton,
        fitnessButton,
        natureButton,
        educationButton,
        jobResumeIdeasButton,
        dataStructuresIdeasButton,
        suggestFeatureInput,
        visitorCountLabel
    }
)

# Module definition
projectIdeasModule: Module = Module(
    name="Project Ideas Module",
    screens={projectIdeasScreen}
)

# Application definition
projectIdeasApp: Application = Application(
    name="Project Ideas Application",
    package="com.example.projectideas",
    versionCode="1",
    versionName="1.0",
    description="Application for generating project ideas",
    screenCompatibility=True,
    modules={projectIdeasModule}
)

# Class and attributes related to this page
# Class: ProjectIdeasPage
# Attributes: projectDescription, isRandomIdeasButtonEnabled, pageTitle, isDataStructuresIdeasButtonEnabled, availableThemeOptions, visitorCount, userFeatureSuggestion, isJobResumeIdeasButtonEnabled

# Time taken to generate the structural model: 7.69 seconds

# Time taken to generate the GUI model: 53.83 seconds

# Total time taken: 61.53 seconds
