
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="employee_management_component", description="Manage Employees")

# Button: Delete
deleteButton: Button = Button(
    name="Delete Button",
    description="Delete selected employees",
    label="Delete",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Delete
)

# Button: Add New Employee
addNewEmployeeButton: Button = Button(
    name="Add New Employee Button",
    description="Add a new employee",
    label="Add New Employee",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Employee DataSource definition
datasource_employee: ModelElement = ModelElement(
    name="Employee Data Source",
    dataSourceClass=EmployeeManagementPage,
    fields=[
        EmployeeManagementPage_employeeName,
        EmployeeManagementPage_employeeEmail,
        EmployeeManagementPage_employeeAddress,
        EmployeeManagementPage_employeePhone
    ]
)

# Employee List definition
employeeList: DataList = DataList(
    name="EmployeeList",
    description="List of employees",
    list_sources={datasource_employee}
)

# Employee Management Screen definition
EmployeeManagementScreen: Screen = Screen(
    name="Employee Management Screen",
    description="Screen for managing employees",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={deleteButton, addNewEmployeeButton, employeeList}
)

# Module definition
EmployeeModule: Module = Module(
    name="employee_module",
    screens={EmployeeManagementScreen}
)

# Application definition
EmployeeApp: Application = Application(
    name="Employee Management App",
    package="com.example.employeemanagement",
    versionCode="1",
    versionName="1.0",
    description="An application for managing employees.",
    screenCompatibility=True,
    modules={EmployeeModule}
)

# Class and attributes related to this page
# Class: EmployeeManagementPage
# Attributes: employeeName, employeeEmail, employeeAddress, employeePhone
