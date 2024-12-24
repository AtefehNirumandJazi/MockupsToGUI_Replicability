
from besser.BUML.metamodel.gui import *

# DataSource for UserProfilePage
userProfileDataSource: ModelElement = ModelElement(
    name="UserProfile Data Source",
    dataSourceClass=UserProfilePage,
    fields=[
        UserProfilePage_userId,
        UserProfilePage_userName,
        UserProfilePage_userFullName,
        UserProfilePage_userEmail
    ]
)

# List for displaying user profiles
userProfileList: DataList = DataList(
    name="UserProfileList",
    description="List of user profiles",
    list_sources={userProfileDataSource}
)

# Buttons for each user profile
editButton: Button = Button(
    name="Edit Button",
    description="Edit user profile",
    label="Edit",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Edit
)

deleteButton: Button = Button(
    name="Delete Button",
    description="Delete user profile",
    label="Delete",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Delete
)

# Add new user button
addNewButton: Button = Button(
    name="Add New Button",
    description="Add a new user profile",
    label="Add New",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Screen for displaying user profiles
userProfileScreen: Screen = Screen(
    name="UserProfileScreen",
    description="Screen for managing user profiles",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={userProfileList, editButton, deleteButton, addNewButton}
)

# Module containing the user profile screen
userProfileModule: Module = Module(
    name="UserProfileModule",
    screens={userProfileScreen}
)

# Application definition
userProfileApp: Application = Application(
    name="UserProfile Management App",
    package="com.example.userprofile",
    versionCode="1",
    versionName="1.0",
    description="An application for managing user profiles.",
    screenCompatibility=True,
    modules={userProfileModule}
)

# Class and attributes related to this page
# Class: UserProfilePage
# Attributes: userId, userName, userFullName, userEmail

# Time taken to generate the structural model: 10.93 seconds

# Time taken to generate the GUI model: 43.13 seconds

# Total time taken: 54.06 seconds
