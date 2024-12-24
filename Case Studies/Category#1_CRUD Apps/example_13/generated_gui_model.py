
from library import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="application_component", description="Application Page")

# DataSource definition
datasource_application: ModelElement = ModelElement(
    name="Application Data Source",
    dataSourceClass=ApplicationPage,
    fields=[
        ApplicationPage_index,
        ApplicationPage_lastName,
        ApplicationPage_firstName,
        ApplicationPage_age,
        ApplicationPage_jobTitle,
        ApplicationPage_homeAddress
    ]
)

# DataList definition
applicationList: DataList = DataList(
    name="ApplicationList",
    description="List of application entries",
    list_sources={datasource_application}
)

# InputFields for Form
lastNameField: InputField = InputField(
    name="Last Name",
    description="Input for last name",
    fieldType="Text",
    validationRules=""
)

firstNameField: InputField = InputField(
    name="First Name",
    description="Input for first name",
    fieldType="Text",
    validationRules=""
)

ageField: InputField = InputField(
    name="Age",
    description="Input for age",
    fieldType="Number",
    validationRules=""
)

jobField: InputField = InputField(
    name="Job",
    description="Input for job",
    fieldType="Text",
    validationRules=""
)

addressField: InputField = InputField(
    name="Address",
    description="Input for address",
    fieldType="Text",
    validationRules=""
)

# Form definition
applicationForm: Form = Form(
    name="ApplicationForm",
    description="Form to add new application entry",
    inputFields={lastNameField, firstNameField, ageField, jobField, addressField}
)

# Button for adding new entry
addButton: Button = Button(
    name="Add Button",
    description="Button to add new entry",
    label="+",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add
)

# Screen definition
ApplicationScreen: Screen = Screen(
    name="ApplicationScreen",
    description="Screen displaying application data",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Large",
    view_elements={applicationList, applicationForm, addButton}
)

# Module definition
ApplicationModule: Module = Module(
    name="ApplicationModule",
    screens={ApplicationScreen}
)

# Application definition
ApplicationApp: Application = Application(
    name="Application",
    package="com.example.application",
    versionCode="1",
    versionName="1.0",
    description="Application for managing entries",
    screenCompatibility=True,
    modules={ApplicationModule}
)

# Class and attributes
# Class: ApplicationPage
# Attributes: index, lastName, firstName, age, jobTitle, homeAddress

# Time taken to generate the structural model: 8.04 seconds

# Time taken to generate the GUI model: 29.97 seconds

# Total time taken: 38.01 seconds
