
# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="employee_component", description="Employee Information Table")

# DataSource definition
datasource_employee: ModelElement = ModelElement(
    name="Employee Data Source",
    dataSourceClass=EmployeePage,
    fields=[
        EmployeePage_name,
        EmployeePage_status,
        EmployeePage_role,
        EmployeePage_manager,
        EmployeePage_department
    ]
)

# Employee List definition
employeeList: DataList = DataList(
    name="EmployeeList",
    description="List of employees with details",
    list_sources={datasource_employee}
)

# Employee Screen definition
EmployeeScreen: Screen = Screen(
    name="EmployeeScreen",
    description="Screen displaying employee details",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Large",
    view_elements={employeeList}
)

# Module definition
EmployeeModule: Module = Module(
    name="employee_module",
    screens={EmployeeScreen}
)

# Application definition
EmployeeApp: Application = Application(
    name="Employee Management",
    package="com.example.employeemanagement",
    versionCode="1",
    versionName="1.0",
    description="Application for managing employee details",
    screenCompatibility=True,
    modules={EmployeeModule}
)

# Class and Attributes
# This page is related to the EmployeePage class.
# Attributes of EmployeePage:
# - name
# - status
# - role
# - manager
# - department
