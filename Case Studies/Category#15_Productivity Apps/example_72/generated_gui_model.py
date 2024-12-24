
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="customer_page_component", description="Customer Page with Company Details")

# Buttons
viewAllButton: Button = Button(name="View All Button", description="View all companies", label="View all", buttonType=ButtonType.TextButton)
monitoredButton: Button = Button(name="Monitored Button", description="View monitored companies", label="Monitored", buttonType=ButtonType.TextButton)
unmonitoredButton: Button = Button(name="Unmonitored Button", description="View unmonitored companies", label="Unmonitored", buttonType=ButtonType.TextButton)
importButton: Button = Button(name="Import Button", description="Import data", label="Import", buttonType=ButtonType.IconButton)
addVendorButton: Button = Button(name="Add Vendor Button", description="Add a new vendor", label="Add vendor", buttonType=ButtonType.RaisedButton)

# InputField
searchField: InputField = InputField(name="Search Field", description="Search companies", fieldType="Search", validationRules="")

# DataSource
companyDataSource: ModelElement = ModelElement(name="Company Data Source", dataSourceClass=Company, fields=[
    Company_name, Company_website, Company_status, Company_about, Company_users, Company_licenseUse
])

# List
companyList: DataList = DataList(name="Company List", description="List of companies", list_sources={companyDataSource})

# Screen definition
CustomerPageScreen: Screen = Screen(
    name="Customer Page Screen",
    description="Screen displaying customer companies",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Large",
    view_elements={viewAllButton, monitoredButton, unmonitoredButton, importButton, addVendorButton, searchField, companyList}
)

# Module definition
CustomerModule: Module = Module(name="Customer Module", screens={CustomerPageScreen})

# Application definition
CustomerApp: Application = Application(
    name="Customer Management App",
    package="com.example.customermanagement",
    versionCode="1",
    versionName="1.0",
    description="Application for managing customer companies",
    screenCompatibility=True,
    modules={CustomerModule}
)

# Class and attributes
# This page is related to the "Company" class in the structural model.
# Attributes of the "Company" class:
# - name
# - website
# - status
# - about
# - users
# - licenseUse

# Time taken to generate the structural model: 14.75 seconds

# Time taken to generate the GUI model: 33.86 seconds

# Total time taken: 48.61 seconds
