
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(
    name="JustFourThingsComponent", 
    description="Productivity App for the Easily Overwhelmed"
)

# InputFields
firstThingInput: InputField = InputField(
    name="FirstThingInput", 
    description="First Thing", 
    fieldType="Text", 
    validationRules=""
)
secondThingInput: InputField = InputField(
    name="SecondThingInput", 
    description="Second Thing", 
    fieldType="Text", 
    validationRules=""
)
thirdThingInput: InputField = InputField(
    name="ThirdThingInput", 
    description="Third Thing", 
    fieldType="Text", 
    validationRules=""
)
selfCareThingInput: InputField = InputField(
    name="SelfCareThingInput", 
    description="Self-Care Thing", 
    fieldType="Text", 
    validationRules=""
)

# Form definition
justFourThingsForm: Form = Form(
    name="JustFourThingsForm", 
    description="Today I will...", 
    inputFields={
        firstThingInput, 
        secondThingInput, 
        thirdThingInput, 
        selfCareThingInput
    }
)

# Screen definition
justFourThingsScreen: Screen = Screen(
    name="JustFourThingsScreen", 
    description="Just Four Things", 
    x_dpi="x_dpi", 
    y_dpi="y_dpi", 
    size="Medium", 
    view_elements={justFourThingsForm}
)

# Module definition
justFourThingsModule: Module = Module(
    name="JustFourThingsModule", 
    screens={justFourThingsScreen}
)

# Application definition
justFourThingsApp: Application = Application(
    name="JustFourThingsApp", 
    package="com.example.justfourthings", 
    versionCode="1", 
    versionName="1.0", 
    description="Productivity App for the Easily Overwhelmed", 
    screenCompatibility=True, 
    modules={justFourThingsModule}
)

# Class and attributes
# This page is related to the class: JustFourThingsPage
# Attributes of this class:
# - firstThing
# - secondThing
# - thirdThing
# - selfCareThing

# Time taken to generate the structural model: 9.17 seconds

# Time taken to generate the GUI model: 23.51 seconds

# Total time taken: 32.68 seconds
