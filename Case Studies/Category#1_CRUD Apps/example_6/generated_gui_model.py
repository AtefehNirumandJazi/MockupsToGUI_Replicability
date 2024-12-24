
# Import necessary classes from the GUI metamodel
from besser.BUML.metamodel.gui import *

# DataSource for UserManagementPage
user_data_source = ModelElement(
    name="User Data Source",
    dataSourceClass=UserManagementPage,
    fields=[
        UserManagementPage_name,
        UserManagementPage_country,
        UserManagementPage_salary,
        UserManagementPage_email
    ]
)

# InputField for search
search_input = InputField(
    name="Search Input",
    description="Search by name",
    fieldType="Search",
    validationRules=""
)

# Button for adding a new user
add_user_button = Button(
    name="Add User Button",
    description="Add a new user",
    label="Add more user",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# List for displaying users
user_list = DataList(
    name="User List",
    description="List of users",
    list_sources={user_data_source}
)

# Buttons for editing and deleting users
edit_button = Button(
    name="Edit Button",
    description="Edit user",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Edit
)

delete_button = Button(
    name="Delete Button",
    description="Delete user",
    label="Delete",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Delete
)

# Screen definition
user_management_screen = Screen(
    name="User Management Screen",
    description="Manage users",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={
        add_user_button,
        search_input,
        user_list,
        edit_button,
        delete_button
    }
)

# Module definition
user_management_module = Module(
    name="User Management Module",
    screens={user_management_screen}
)

# Application definition
user_management_app = Application(
    name="User Management App",
    package="com.example.usermanagement",
    versionCode="1",
    versionName="1.0",
    description="An application for managing users.",
    screenCompatibility=True,
    modules={user_management_module}
)

# Class and attributes related to this page
# Class: UserManagementPage
# Attributes: name, country, salary, email, totalSalary
