Here's the Python code representing the GUI elements of the provided UI mock-up:

```python
from besser.BUML.metamodel.gui import *
from besser.BUML.metamodel.structural import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="customer_management_component", description="Customer Management Interface")

# Button: Add another customer
addCustomerButton: Button = Button(
    name="AddCustomerButton",
    description="Add another customer",
    label="Add another customer",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# InputField: Search
searchInputField: InputField = InputField(
    name="SearchInputField",
    description="Search customers",
    fieldType="Search",
    validationRules=""
)

# DataSource: Customer Table
datasource_customer: ModelElement = ModelElement(
    name="Customer Data Source",
    dataSourceClass=CustomerManagement,
    fields=[
        CustomerManagement_name,
        CustomerManagement_gender,
        CustomerManagement_country,
        CustomerManagement_phoneNumber
    ]
)

# List: Customer Table
customerTable: DataList = DataList(
    name="CustomerTable",
    description="Table displaying customer information",
    list_sources={datasource_customer}
)

# Screen: Customer Management
CustomerManagementScreen: Screen = Screen(
    name="CustomerManagementScreen",
    description="Screen for managing customers",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="LargeScreen",
    view_elements={addCustomerButton, searchInputField, customerTable}
)

# Module definition
CustomerModule: Module = Module(
    name="CustomerModule",
    screens={CustomerManagementScreen}
)

# Application definition
CustomerApp: Application = Application(
    name="Customer Management App",
    package="com.example.customermanagement",
    versionCode="1",
    versionName="1.0",
    description="Application for managing customer data",
    screenCompatibility=True,
    modules={CustomerModule}
)
```