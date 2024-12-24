
# Import necessary classes from the GUI metamodel
from besser.BUML.metamodel.gui import *

# Define the ViewComponent
viewComponent: ViewComponent = ViewComponent(
    name="JustFourThings",
    description="Productivity app for the easily overwhelmed"
)

# Define InputFields
firstThingInput: InputField = InputField(
    name="First Thing",
    description="First task of the day",
    fieldType="Text",
    validationRules=""
)
secondThingInput: InputField = InputField(
    name="Second Thing",
    description="Second task of the day",
    fieldType="Text",
    validationRules=""
)
thirdThingInput: InputField = InputField(
    name="Third Thing",
    description="Third task of the day",
    fieldType="Text",
    validationRules=""
)
selfCareThingInput: InputField = InputField(
    name="Self-care Thing",
    description="Self-care task of the day",
    fieldType="Text",
    validationRules=""
)

# Define the Form
justFourThingsForm: Form = Form(
    name="JustFourThingsForm",
    description="Form to input four tasks",
    inputFields={firstThingInput, secondThingInput, thirdThingInput, selfCareThingInput}
)

# Define the Screen
justFourThingsScreen: Screen = Screen(
    name="JustFourThingsScreen",
    description="Screen for entering four tasks",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={justFourThingsForm}
)

# Define the Module
justFourThingsModule: Module = Module(
    name="JustFourThingsModule",
    screens={justFourThingsScreen}
)

# Define the Application
justFourThingsApp: Application = Application(
    name="JustFourThingsApp",
    package="com.example.justfourthings",
    versionCode="1",
    versionName="1.0",
    description="A productivity app for the easily overwhelmed",
    screenCompatibility=True,
    modules={justFourThingsModule}
)

# Class related to this page in the structural model
# Class: JustFourThingsPage
# Attributes: firstThing, secondThing, thirdThing, selfCareThing

# Time taken to generate the structural model: 7.77 seconds

# Time taken to generate the GUI model: 24.87 seconds

# Total time taken: 32.64 seconds
