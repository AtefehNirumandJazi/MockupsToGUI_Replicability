
from besser.BUML.metamodel.gui import *

# Input fields
project_title_input = InputField(
    name="Project Title",
    description="Project title input field",
    fieldType="Text",
    validationRules=""
)

description_input = InputField(
    name="Description",
    description="Description input field",
    fieldType="Text",
    validationRules=""
)

localhost_link_input = InputField(
    name="Localhost Link",
    description="Localhost link input field",
    fieldType="Text",
    validationRules=""
)

skynet_task_link_input = InputField(
    name="Skynet Task Link",
    description="Skynet task link input field",
    fieldType="URL",
    validationRules=""
)

# Button
add_project_button = Button(
    name="Add Project Button",
    description="Button to add a project",
    label="ADD PROJECT",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Form
project_form = Form(
    name="Project Form",
    description="Form to add a new project",
    inputFields={project_title_input, description_input, localhost_link_input, skynet_task_link_input}
)

# Screen
project_screen = Screen(
    name="Project Screen",
    description="Screen for adding a new project",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={project_form, add_project_button}
)

# Class and attributes
# This page is related to the "ProjectPage" class in the structural model.
# Attributes of this class:
# - projectTitle
# - description
# - localhostLink
# - skynetTaskLink

# Time taken to generate the structural model: 8.81 seconds

# Time taken to generate the GUI model: 21.12 seconds

# Total time taken: 29.93 seconds
