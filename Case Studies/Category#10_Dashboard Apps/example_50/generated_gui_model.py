
# Import necessary classes from the GUI metamodel
from besser.BUML.metamodel.gui import *

# Input fields
projectTitleField = InputField(
    name="Project Title",
    description="Project title input",
    fieldType="Text",
    validationRules=""
)

descriptionField = InputField(
    name="Description",
    description="Description input",
    fieldType="Text",
    validationRules=""
)

localhostLinkField = InputField(
    name="Localhost Link",
    description="Localhost link input",
    fieldType="Text",
    validationRules=""
)

skyNetTaskLinkField = InputField(
    name="SkyNet Task Link",
    description="SkyNet task link input",
    fieldType="URL",
    validationRules=""
)

# Button
addButton = Button(
    name="Add Project Button",
    description="Button to add project",
    label="ADD PROJECT",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.SubmitForm
)

# Form
projectForm = Form(
    name="Project Form",
    description="Form for project details",
    inputFields={projectTitleField, descriptionField, localhostLinkField, skyNetTaskLinkField}
)

# Screen
projectScreen = Screen(
    name="Project Screen",
    description="Screen for project details",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={projectForm, addButton}
)

# Class and attributes based on the structural model
# Class: ProjectPage
# Attributes: projectTitle, description, localhostLink, skyNetTaskLink

# Time taken to generate the structural model: 6.43 seconds

# Time taken to generate the GUI model: 18.77 seconds

# Total time taken: 25.20 seconds
