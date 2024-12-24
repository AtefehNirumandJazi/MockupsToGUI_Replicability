
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="MessagingAppPage", description="Messaging Application Page")

# Menu definition
menu: Menu = Menu(name="Main Menu", description="Main navigation menu", menuItems={
    MenuItem(label="Inbox"),
    MenuItem(label="Drafts"),
    MenuItem(label="Sent"),
    MenuItem(label="Favourites"),
    MenuItem(label="Trash"),
    MenuItem(label="Paid"),
    MenuItem(label="Pending"),
    MenuItem(label="Denied")
})

# InputField definition
searchField: InputField = InputField(name="Search", description="Search bar", fieldType="Search", validationRules="")

# List definition for Friends
friendsList: List = List(name="Friends List", description="List of friends", list_sources={
    ModelElement(name="Friend Data Source", dataSourceClass=Friend, fields={Friend_name, Friend_lastActive})
})

# List definition for Messages
messagesList: List = List(name="Messages List", description="List of messages", list_sources={
    ModelElement(name="Message Data Source", dataSourceClass=Message, fields={Message_content, Message_sender, Message_timestamp})
})

# Screen definition
MessagingAppScreen: Screen = Screen(name="MessagingAppScreen", description="Screen for messaging application",
                                    x_dpi="x_dpi", y_dpi="y_dpi", size="Large", view_elements={
                                        menu, searchField, friendsList, messagesList
                                    })

# Module definition
MessagingModule: Module = Module(name="MessagingModule", screens={MessagingAppScreen})

# Application definition
MessagingApp: Application = Application(name="Messaging Application", package="com.example.messagingapp", versionCode="1",
                                        versionName="1.0", description="A messaging application for communication.",
                                        screenCompatibility=True, modules={MessagingModule})

# Class and attributes
# This page is related to the class: MessagingAppPage
# Attributes of this class based on the structural model:
# - inboxCount: IntegerType
# - friendCount: IntegerType

# Time taken to generate the structural model: 11.44 seconds

# Time taken to generate the GUI model: 26.88 seconds

# Total time taken: 38.33 seconds
