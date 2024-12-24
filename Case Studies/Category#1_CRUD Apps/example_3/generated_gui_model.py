
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="simple_crud_angular1", description="Simple CRUD Angular1")

# InputField for search
searchField: InputField = InputField(name="search", description="Search", fieldType="Search", validationRules="")

# DataSource for table
datasource_sample_table: ModelElement = ModelElement(
    name="Sample Table Data Source",
    dataSourceClass=SimpleCRUDPage,
    fields=[
        SimpleCRUDPage_id,
        SimpleCRUDPage_name,
        SimpleCRUDPage_value
    ]
)

# List for displaying table
sampleTableList: DataList = DataList(
    name="SampleTable",
    description="Sample table",
    list_sources={datasource_sample_table}
)

# Button for inserting a row
insertRowButton: Button = Button(
    name="Insert Row Button",
    description="Insert a new row",
    label="INSERT ROW",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Button for creating a table
createTableButton: Button = Button(
    name="Create Table Button",
    description="Create a new table",
    label="CREATE TABLE",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Button for dropping a table
dropTableButton: Button = Button(
    name="Drop Table Button",
    description="Drop the table",
    label="DROP TABLE",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Delete
)

# Screen definition
SimpleCRUDScreen: Screen = Screen(
    name="SimpleCRUDScreen",
    description="Screen for Simple CRUD operations",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={
        searchField,
        sampleTableList,
        insertRowButton,
        createTableButton,
        dropTableButton
    }
)

# Module definition
SimpleCRUDModule: Module = Module(name="SimpleCRUDModule", screens={SimpleCRUDScreen})

# Application definition
SimpleCRUDApp: Application = Application(
    name="Simple CRUD Application",
    package="com.example.simplecrud",
    versionCode="1",
    versionName="1.0",
    description="A simple CRUD application for managing data.",
    screenCompatibility=True,
    modules={SimpleCRUDModule}
)

# Class and attributes related to this page
# Class: SimpleCRUDPage
# Attributes: id, name, value, is_active, created_at, updated_at
