
# Import necessary classes from the GUI metamodel
from besser.BUML.metamodel.gui import *

# Define the ViewComponent
viewComponent: ViewComponent = ViewComponent(
    name="Educational App",
    description="Select a topic to see the content."
)

# Define InputFields for EducationalAppPage
gradeInput: InputField = InputField(
    name="Select Grade",
    description="Select Grade",
    fieldType="Text",
    validationRules=""
)
subjectInput: InputField = InputField(
    name="Select Subject",
    description="Select Subject",
    fieldType="Text",
    validationRules=""
)
unitInput: InputField = InputField(
    name="Select Unit",
    description="Select Unit",
    fieldType="Text",
    validationRules=""
)
topicInput: InputField = InputField(
    name="Select Topic",
    description="Select Topic",
    fieldType="Text",
    validationRules=""
)

# Define the Form
educationalForm: Form = Form(
    name="Educational Form",
    description="Form to select educational parameters",
    inputFields={gradeInput, subjectInput, unitInput, topicInput}
)

# Define the Screen
EducationalAppScreen: Screen = Screen(
    name="Educational App Screen",
    description="Screen for selecting educational parameters",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={educationalForm}
)

# Define the Module
EducationalModule: Module = Module(
    name="Educational Module",
    screens={EducationalAppScreen}
)

# Define the Application
EducationalApp: Application = Application(
    name="Educational App",
    package="com.example.educationalapp",
    versionCode="1",
    versionName="1.0",
    description="An app for selecting educational topics.",
    screenCompatibility=True,
    modules={EducationalModule}
)

# Class related to this page in the structural model
# Class: EducationalAppPage
# Attributes: topic, subject, grade, unit

# Time taken to generate the structural model: 8.28 seconds

# Time taken to generate the GUI model: 32.36 seconds

# Total time taken: 40.63 seconds
