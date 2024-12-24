
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="user_page_component", description="User Page with CRUD operations")

# Buttons
undoButton: Button = Button(name="Undo Button", description="Undo last action", label="Undo", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)
redoButton: Button = Button(name="Redo Button", description="Redo last undone action", label="Redo", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Confirm)
addButton: Button = Button(name="Add Button", description="Add a new user", label="ADD", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)
deleteButton: Button = Button(name="Delete Button", description="Delete selected users", label="Delete", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)

# Search InputField
searchField: InputField = InputField(name="Search Field", description="Search users", fieldType="Search", validationRules="")

# User DataSource
datasource_user: ModelElement = ModelElement(name="User Data Source", dataSourceClass=UserPage, fields=[
    UserPage_userId, UserPage_userName, UserPage_userGender, UserPage_userBirthday, UserPage_userPhone, UserPage_userCreatedTime
])

# User List
userList: DataList = DataList(name="UserList", description="List of users", list_sources={datasource_user})

# User Page Screen definition
UserPageScreen: Screen = Screen(name="UserPageScreen", description="Screen for managing users",
                                x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                                view_elements={undoButton, redoButton, addButton, deleteButton, searchField, userList})

# Module definition
UserModule: Module = Module(name="UserModule", screens={UserPageScreen})

# Application definition
UserApp: Application = Application(name="User Management App", package="com.example.usermanagement", versionCode="1",
                                   versionName="1.0", description="Application for managing users with CRUD operations.",
                                   screenCompatibility=True, modules={UserModule})

# Class and attributes
# This page is related to the class: UserPage
# Attributes of this class: userId, userName, userGender, userBirthday, userPhone, userCreatedTime
