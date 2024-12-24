
from besser.BUML.metamodel.gui import *

# ViewComponent definition
dashboardComponent: ViewComponent = ViewComponent(
    name="dashboard_component",
    description="Dashboard with navigation and invoice display"
)

# Navigation Menu
navigationMenu: Menu = Menu(
    name="Navigation Menu",
    description="Main navigation menu",
    menuItems={
        MenuItem(label="Upload"),
        MenuItem(label="Media"),
        MenuItem(label="Users"),
        MenuItem(label="Payments"),
        MenuItem(label="Settings"),
        MenuItem(label="Profile"),
        MenuItem(label="Logout")
    }
)

# Dashboard Screen
dashboardScreen: Screen = Screen(
    name="Dashboard Screen",
    description="Main dashboard screen",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Large",
    view_elements={
        navigationMenu,
        Button(
            name="Create Invoice Button",
            description="Button to create a new invoice",
            label="Create Invoice",
            buttonType=ButtonType.RaisedButton,
            actionType=ButtonActionType.Add
        ),
        DataList(
            name="Last Invoices",
            description="List of last invoices",
            list_sources={
                ModelElement(
                    name="Invoice Data Source",
                    dataSourceClass=Invoice,
                    fields={Invoice_invoiceNumber, Invoice_companyName}
                )
            }
        ),
        Button(
            name="Take a Tour Button",
            description="Button to take a tour",
            label="Take a Tour",
            buttonType=ButtonType.RaisedButton,
            actionType=ButtonActionType.Navigate
        ),
        Image(
            name="Dashboard Illustration",
            description="Illustration on the dashboard"
        )
    }
)

# Module definition
dashboardModule: Module = Module(
    name="Dashboard Module",
    screens={dashboardScreen}
)

# Application definition
dashboardApp: Application = Application(
    name="Dashboard Application",
    package="com.example.dashboard",
    versionCode="1",
    versionName="1.0",
    description="Dashboard application for managing invoices and navigation",
    screenCompatibility=True,
    modules={dashboardModule}
)

# Class and attributes
# This page is related to the class: DashboardPage
# Attributes of this class based on the structural model:
# - title
# - subtitle

# Time taken to generate the structural model: 22.40 seconds

# Time taken to generate the GUI model: 55.40 seconds

# Total time taken: 77.81 seconds
