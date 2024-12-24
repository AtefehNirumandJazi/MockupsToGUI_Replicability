
from besser.BUML.metamodel.gui import *
from besser.BUML.metamodel.structural import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="employee_component", description="Employee Management Interface")

# InputFields
searchNameField: InputField = InputField(name="Search Name", description="Search by employee name", fieldType="Search", validationRules="")
orderByField: InputField = InputField(name="Order By", description="Order employees", fieldType="Text", validationRules="")
nameOrderField: InputField = InputField(name="Name Order", description="Order by name", fieldType="Text", validationRules="")

# Buttons
addButton: Button = Button(name="Add Button", description="Add a new employee", label="+ Add", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)
viewButton: Button = Button(name="View Button", description="View employee details", label="View", buttonType=ButtonType.IconButton, actionType=ButtonActionType.View)
editButton: Button = Button(name="Edit Button", description="Edit employee details", label="Edit", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Edit)
deleteButton: Button = Button(name="Delete Button", description="Delete employee", label="Delete", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Delete)

# Employee DataSource
datasource_employee: ModelElement = ModelElement(name="Employee Data Source", dataSourceClass=Employee, fields=[Employee_name, Employee_email, Employee_salary])

# Employee List
employeeList: DataList = DataList(name="EmployeeList", description="List of employees", list_sources={datasource_employee})

# EmployeePage Screen definition
EmployeePageScreen: Screen = Screen(name="EmployeePageScreen", description="Manage employees",
                                    x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                                    view_elements={searchNameField, orderByField, nameOrderField, addButton, viewButton, editButton, deleteButton, employeeList})

# Module definition
EmployeeModule: Module = Module(name="employee_module", screens={EmployeePageScreen})

# Application definition
EmployeeApp: Application = Application(name="Employee Management App", package="com.example.employeemanagement", versionCode="1",
                                       versionName="1.0", description="An application for managing employees.",
                                       screenCompatibility=True, modules={EmployeeModule})

# Class and attributes
# This page is related to the Employee class in the structural model.
# Attributes of the Employee class: name, email, salary.
