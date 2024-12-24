
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="partner_codes_component", description="Partner Codes Management")

# InputFields
codeIDInput: InputField = InputField(name="Code ID Input", description="Input for Code ID", fieldType="Text", validationRules="")
partnerCodeInput: InputField = InputField(name="Partner Code Input", description="Input for Partner Code", fieldType="Text", validationRules="")
userIDInput: InputField = InputField(name="User ID Input", description="Input for User ID", fieldType="Text", validationRules="")
titleInput: InputField = InputField(name="Title Input", description="Input for Title", fieldType="Text", validationRules="")
statusInput: InputField = InputField(name="Status Input", description="Input for Status", fieldType="Text", validationRules="")
dateOfCreationInput: InputField = InputField(name="Date of Creation Input", description="Input for Date of Creation", fieldType="Date", validationRules="")

# Buttons
findButton: Button = Button(name="Find Button", description="Button to find records", label="Find", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Search)
cancelButton: Button = Button(name="Cancel Button", description="Button to cancel search", label="Cancel", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)

# DataSource
partnerCodesDataSource: ModelElement = ModelElement(name="Partner Codes Data Source", dataSourceClass=PartnerCodesPage, fields=[
    PartnerCodesPage_codeID, PartnerCodesPage_partnerCode, PartnerCodesPage_userID, PartnerCodesPage_title, PartnerCodesPage_status, PartnerCodesPage_dateOfCreation
])

# List
partnerCodesList: DataList = DataList(name="Partner Codes List", description="List of Partner Codes", list_sources={partnerCodesDataSource})

# Screen definition
PartnerCodesScreen: Screen = Screen(name="Partner Codes Screen", description="Screen for managing partner codes",
                                    x_dpi="x_dpi", y_dpi="y_dpi", size="Large",
                                    view_elements={codeIDInput, partnerCodeInput, userIDInput, titleInput, statusInput, dateOfCreationInput, findButton, cancelButton, partnerCodesList})

# Module definition
PartnerCodesModule: Module = Module(name="Partner Codes Module", screens={PartnerCodesScreen})

# Application definition
PartnerCodesApp: Application = Application(name="Partner Codes Management App", package="com.example.partnercodes", versionCode="1",
                                           versionName="1.0", description="Application for managing partner codes",
                                           screenCompatibility=True, modules={PartnerCodesModule})

# Class and Attributes
# This page is related to the class: PartnerCodesPage
# Attributes of this class based on the structural model:
# - partnerCode
# - title
# - status
# - userID
# - codeID
# - dateOfCreation

# Time taken to generate the structural model: 7.68 seconds

# Time taken to generate the GUI model: 29.68 seconds

# Total time taken: 37.37 seconds
