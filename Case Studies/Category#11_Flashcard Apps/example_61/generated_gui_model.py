
from besser.BUML.metamodel.gui import *

# InputFields
interestInput: InputField = InputField(name="Interest Input", description="sich interessieren für", fieldType="Text")
excitementInput: InputField = InputField(name="Excitement Input", description="sich freuen auf\nIch freue mich auf das Wochenende.", fieldType="Text")
activityInput: InputField = InputField(name="Activity Input", description="sich beschäftigen mit\nSie beschäftigt sich mit Umweltfragen.", fieldType="Text")
apologyInput: InputField = InputField(name="Apology Input", description="sich entschuldigen bei\nEr entschuldigte sich bei seinem Freund.", fieldType="Text")

# Button
nextCardButton: Button = Button(name="Next Card Button", description="Proceed to the next card", label="Next Card", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Next)

# Screen definition
WebPageScreen: Screen = Screen(name="WebPageScreen", description="Web page for CRUD operations on WebPage entity",
                               x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                               view_elements={interestInput, excitementInput, activityInput, apologyInput, nextCardButton})

# Module definition
WebPageModule: Module = Module(name="WebPageModule", screens={WebPageScreen})

# Application definition
WebApp: Application = Application(name="Web Application", package="com.example.webapp", versionCode="1",
                                  versionName="1.0", description="Web application for managing web pages.",
                                  screenCompatibility=True, modules={WebPageModule})

# Class and attributes
# This page is related to the WebPage class in the structural model.
# Attributes of the WebPage class:
# - duration
# - excitement
# - isActive
# - interest
# - apology
# - activity
# - timestamp

# Time taken to generate the structural model: 9.46 seconds

# Time taken to generate the GUI model: 43.65 seconds

# Total time taken: 53.11 seconds
