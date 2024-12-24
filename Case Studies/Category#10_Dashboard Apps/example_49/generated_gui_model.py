
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="tournament_events_component", description="Tournament Events Management")

# InputField for search
searchField: InputField = InputField(name="searchField", description="Search tournaments", fieldType="Search", validationRules="")

# Button for search
searchButton: Button = Button(name="searchButton", description="Search tournaments", label="Search", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Search)

# Button for new tournament event
newTournamentButton: Button = Button(name="newTournamentButton", description="Create a new tournament event", label="New Tournament Event", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# DataSource for tournament events
tournamentDataSource: ModelElement = ModelElement(name="Tournament Data Source", dataSourceClass=TournamentEventsPage, fields=[
    TournamentEventsPage_id, TournamentEventsPage_title, TournamentEventsPage_club, TournamentEventsPage_eventDate, TournamentEventsPage_enabled
])

# List for displaying tournament events
tournamentList: DataList = DataList(name="tournamentList", description="List of tournament events", list_sources={tournamentDataSource})

# Dropdown for items per page
itemsPerPageDropdown: InputField = InputField(name="itemsPerPageDropdown", description="Select number of items per page", fieldType="Number", validationRules="")

# Screen definition
TournamentEventsScreen: Screen = Screen(name="TournamentEventsScreen", description="Manage tournament events",
                                        x_dpi="x_dpi", y_dpi="y_dpi", size="Large",
                                        view_elements={searchField, searchButton, newTournamentButton, tournamentList, itemsPerPageDropdown})

# Module definition
TournamentModule: Module = Module(name="TournamentModule", screens={TournamentEventsScreen})

# Application definition
TournamentApp: Application = Application(name="Tournament Management App", package="com.example.tournamentmanagement", versionCode="1",
                                         versionName="1.0", description="An application to manage golf tournament events.",
                                         screenCompatibility=True, modules={TournamentModule})

# Class and attributes
# Class: TournamentEventsPage
# Attributes: id, title, club, eventDate, enabled, itemsPerPage, search

# Time taken to generate the structural model: 10.02 seconds

# Time taken to generate the GUI model: 32.08 seconds

# Total time taken: 42.10 seconds
