
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="user_component", description="User Management Interface")

# Button for adding a new user
addButton: Button = Button(
    name="Add User Button",
    description="Add a new user",
    label="Add",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Input field for searching users
searchInput: InputField = InputField(
    name="Search Input",
    description="Search users by id, name, email",
    fieldType="Search",
    validationRules=""
)

# User data source definition
datasource_user: ModelElement = ModelElement(
    name="User Data Source",
    dataSourceClass=UserPage,
    fields=[
        UserPage_id, UserPage_name, UserPage_username,
        UserPage_email, UserPage_address, UserPage_website,
        UserPage_company
    ]
)

# User list definition
userList: DataList = DataList(
    name="UserList",
    description="List of users",
    list_sources={datasource_user}
)

# Edit and delete buttons for each user
editButton: Button = Button(
    name="Edit User Button",
    description="Edit user details",
    label="edit",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Edit
)

deleteButton: Button = Button(
    name="Delete User Button",
    description="Delete user",
    label="delete",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Delete
)

# User management screen definition
UserManagementScreen: Screen = Screen(
    name="User Management Screen",
    description="Manage users with CRUD operations",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="LargeScreen",
    view_elements={addButton, searchInput, userList, editButton, deleteButton}
)

# Module definition
UserModule: Module = Module(
    name="user_module",
    screens={UserManagementScreen}
)

# Application definition
UserApp: Application = Application(
    name="User Management App",
    package="com.example.usermanagement",
    versionCode="1",
    versionName="1.0",
    description="An application for managing users",
    screenCompatibility=True,
    modules={UserModule}
)

# Time taken to generate the structural model: 7.32 seconds

# Time taken to generate the GUI model: 26.76 seconds

# Total time taken: 34.08 seconds
