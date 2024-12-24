
from besser.BUML.metamodel.gui import *
from besser.BUML.metamodel.structural import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="volunteers_component", description="Volunteers Management Page")

# InputField for search
searchField: InputField = InputField(name="Search Volunteers", description="Search volunteers by name", fieldType="Search", validationRules="")

# Dropdown for filter
filterDropdown: Menu = Menu(name="Filter Volunteers", description="Filter volunteers by status")
filterDropdown.menuItems = {MenuItem(label="ALL"), MenuItem(label="APPROVED"), MenuItem(label="APPLIED"), MenuItem(label="DISMISSED")}

# Button for email all volunteers
emailAllButton: Button = Button(name="Email All Volunteers", description="Send email to all volunteers", label="EMAIL ALL VOLUNTEERS (29)", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Send)

# Button for view list of email addresses
viewEmailListButton: Button = Button(name="View List of Email Addresses", description="View list of all volunteer email addresses", label="VIEW LIST OF EMAIL ADDRESSES (29)", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.View)

# DataSource for Volunteer
datasource_volunteer: ModelElement = ModelElement(name="Volunteer Data Source", dataSourceClass=Volunteer, fields=[Volunteer_id, Volunteer_name, Volunteer_phone, Volunteer_email, Volunteer_status, Volunteer_submitted])

# Volunteer List definition
volunteerList: DataList = DataList(name="VolunteerList", description="List of volunteers", list_sources={datasource_volunteer})

# Pagination controls
paginationControls: ViewComponent = ViewComponent(name="Pagination Controls", description="Controls for navigating pages")

# Button for edit action
editButton: Button = Button(name="Edit Volunteer", description="Edit volunteer details", label="EDIT", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.OpenForm)

# Button for delete action
deleteButton: Button = Button(name="Delete Volunteer", description="Delete volunteer", label="DELETE", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)

# Volunteers Page Screen definition
VolunteersPageScreen: Screen = Screen(
    name="VolunteersPageScreen",
    description="Manage volunteers",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={filterDropdown, searchField, emailAllButton, viewEmailListButton, volunteerList, paginationControls, editButton, deleteButton}
)

# Module definition
VolunteersModule: Module = Module(name="VolunteersModule", screens={VolunteersPageScreen})

# Application definition
VolunteersApp: Application = Application(
    name="Volunteers Management App",
    package="com.example.volunteers",
    versionCode="1",
    versionName="1.0",
    description="Application for managing volunteers",
    screenCompatibility=True,
    modules={VolunteersModule}
)

# Class and attributes
# This page is related to the "Volunteer" class.
# Attributes of the "Volunteer" class: id, name, phone, email, status, submitted.
