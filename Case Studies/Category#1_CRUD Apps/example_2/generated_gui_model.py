Here's the Python code representing the GUI elements of the provided UI mock-up:

```python
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="user_management_component", description="User Management Interface")

# Button for adding a new user
addNewButton: Button = Button(
    name="Add New Button",
    description="Add a new user",
    label="Add New",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# DataSource for UserManagementPage
datasource_user: ModelElement = ModelElement(
    name="User Data Source",
    dataSourceClass=UserManagementPage,
    fields=[
        UserManagementPage_userId,
        UserManagementPage_userName,
        UserManagementPage_userFullName,
        UserManagementPage_userEmail
    ]
)

# User List definition
userList: DataList = DataList(
    name="UserList",
    description="List of users",
    list_sources={datasource_user}
)

# User Management Screen definition
UserManagementScreen: Screen = Screen(
    name="UserManagementScreen",
    description="Manage users with options to edit or delete",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={addNewButton, userList}
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
    description="An application for managing users.",
    screenCompatibility=True,
    modules={UserModule}
)
```