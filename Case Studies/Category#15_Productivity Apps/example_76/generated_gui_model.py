
from besser.BUML.metamodel.gui import *
from besser.BUML.metamodel.structural import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="customer_page_component", description="Customer Page UI Elements")

# Buttons
importButton: Button = Button(name="Import Button", description="Import data", label="Import", buttonType=ButtonType.IconButton)
addVendorButton: Button = Button(name="Add Vendor Button", description="Add a new vendor", label="Add vendor", buttonType=ButtonType.RaisedButton)

# Tabs
viewAllButton: Button = Button(name="View All Button", description="View all customers", label="View all", buttonType=ButtonType.TextButton)
monitoredButton: Button = Button(name="Monitored Button", description="View monitored customers", label="Monitored", buttonType=ButtonType.TextButton)
unmonitoredButton: Button = Button(name="Unmonitored Button", description="View unmonitored customers", label="Unmonitored", buttonType=ButtonType.TextButton)

# Search Input
searchInput: InputField = InputField(name="Search Input", description="Search customers", fieldType="Search", validationRules="")

# Company DataSource
datasource_company: ModelElement = ModelElement(name="Company Data Source", dataSourceClass=Company, fields=[
    Company_name, Company_status, Company_about, Company_users, Company_licenseUse, Company_website
])

# Company List
companyList: DataList = DataList(name="Company List", description="List of companies", list_sources={datasource_company})

# Pagination Buttons
previousButton: Button = Button(name="Previous Button", description="Go to previous page", label="Previous", buttonType=ButtonType.TextButton)
nextButton: Button = Button(name="Next Button", description="Go to next page", label="Next", buttonType=ButtonType.TextButton)

# Customer Page Screen definition
CustomerPageScreen: Screen = Screen(name="Customer Page Screen", description="Screen for managing customers",
                                    x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                                    view_elements={importButton, addVendorButton, viewAllButton, monitoredButton, unmonitoredButton, searchInput, companyList, previousButton, nextButton})

# Module definition
CustomerModule: Module = Module(name="Customer Module", screens={CustomerPageScreen})

# Application definition
CustomerApp: Application = Application(name="Customer Management App", package="com.example.customermanagement", versionCode="1",
                                       versionName="1.0", description="Application for managing customer data.",
                                       screenCompatibility=True, modules={CustomerModule})

# Class and Attributes
# This page is related to the "CustomerPage" class in the structural model.
# Attributes of the "CustomerPage" class:
# - totalPages: Integer
# - unmonitored: Boolean
# - monitored: Boolean
# - viewAll: Boolean
# - search: String
# - pageNumber: Integer
# - totalVendors: Integer

# Time taken to generate the structural model: 9.55 seconds

# Time taken to generate the GUI model: 47.83 seconds

# Total time taken: 57.38 seconds
