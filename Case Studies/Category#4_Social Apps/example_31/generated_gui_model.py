
from besser.BUML.metamodel.gui import *

# ViewComponent definition
searchBar: InputField = InputField(
    name="SearchBar",
    description="Search contacts",
    fieldType="Search"
)

contactList: List = List(
    name="ContactList",
    description="List of contacts",
    list_sources=set()
)

currentChatHeader: ViewContainer = ViewContainer(
    name="CurrentChatHeader",
    description="Header for the current chat"
)

currentChatName: InputField = InputField(
    name="CurrentChatName",
    description="Name of the current chat",
    fieldType="Text"
)

currentChatStatus: InputField = InputField(
    name="CurrentChatStatus",
    description="Status of the current chat",
    fieldType="Text"
)

messageInput: InputField = InputField(
    name="MessageInput",
    description="Input field for typing messages",
    fieldType="Text"
)

sendMessageButton: Button = Button(
    name="SendMessageButton",
    description="Button to send message",
    label="Send",
    buttonType=ButtonType.IconButton,
    actionType=ButtonActionType.Send
)

# Additional elements from the mock-up
refreshButton: Button = Button(
    name="RefreshButton",
    description="Button to refresh chat",
    label="Refresh",
    buttonType=ButtonType.IconButton,
    actionType=ButtonActionType.Refresh
)

menuButton: Button = Button(
    name="MenuButton",
    description="Button to open menu",
    label="Menu",
    buttonType=ButtonType.IconButton,
    actionType=ButtonActionType.Navigate
)

# ChatPage Screen definition
ChatPageScreen: Screen = Screen(
    name="ChatPageScreen",
    description="Screen for chat page",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={
        searchBar,
        contactList,
        currentChatHeader,
        currentChatName,
        currentChatStatus,
        messageInput,
        sendMessageButton,
        refreshButton,
        menuButton
    }
)

# Module definition
ChatModule: Module = Module(
    name="ChatModule",
    screens={ChatPageScreen}
)

# Application definition
ChatApp: Application = Application(
    name="ChatApplication",
    package="com.example.chatapp",
    versionCode="1",
    versionName="1.0",
    description="A chat application for messaging",
    screenCompatibility=True,
    modules={ChatModule}
)

# Class and attributes based on the structural model
# Class: ChatPage
# Attributes: messageInput, contactMessage, contactName, searchBar, contactTime, currentChatName, currentChatStatus

# Time taken to generate the structural model: 7.47 seconds

# Time taken to generate the GUI model: 28.85 seconds

# Total time taken: 36.32 seconds
