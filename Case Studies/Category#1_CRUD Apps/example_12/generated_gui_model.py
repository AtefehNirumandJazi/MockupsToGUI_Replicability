
from library import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="pet_management_component", description="Pet Management Interface")

# Input Fields
petIDField: InputField = InputField(name="Pet ID", description="Enter Pet ID", fieldType="Text")
petNameField: InputField = InputField(name="Pet Name", description="Enter Pet Name", fieldType="Text")
ageField: InputField = InputField(name="Age", description="Enter Age", fieldType="Number")
typeField: InputField = InputField(name="Type", description="Select Type", fieldType="Text")
weightField: InputField = InputField(name="Weight", description="Enter Weight", fieldType="Number")
lengthField: InputField = InputField(name="Length", description="Enter Length", fieldType="Number")
colorField: InputField = InputField(name="Color", description="Select Color", fieldType="Color")
breedField: InputField = InputField(name="Breed", description="Select Breed", fieldType="Text")

# Checkboxes
vaccinatedCheckbox: InputField = InputField(name="Vaccinated", description="Vaccinated", fieldType="Boolean")
dewormedCheckbox: InputField = InputField(name="Dewormed", description="Dewormed", fieldType="Boolean")
sterilizedCheckbox: InputField = InputField(name="Sterilized", description="Sterilized", fieldType="Boolean")

# Buttons
submitButton: Button = Button(name="Submit Button", description="Submit Form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)
showHealthyPetButton: Button = Button(name="Show Healthy Pet Button", description="Show Healthy Pets", label="Show Healthy Pet", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Filter)

# Form
petForm: Form = Form(name="Pet Form", description="Form to manage pet details", inputFields={petIDField, petNameField, ageField, typeField, weightField, lengthField, colorField, breedField, vaccinatedCheckbox, dewormedCheckbox, sterilizedCheckbox})

# Data Source
datasource_pet: ModelElement = ModelElement(name="Pet Data Source", dataSourceClass=PetManagement, fields=[PetManagement_petID, PetManagement_petName, PetManagement_age, PetManagement_type, PetManagement_weight, PetManagement_length, PetManagement_color, PetManagement_vaccinated, PetManagement_dewormed, PetManagement_sterilized, PetManagement_dateAdded])

# Pet List
petList: DataList = DataList(name="Pet List", description="List of pets", list_sources={datasource_pet})

# Screen definition
PetManagementScreen: Screen = Screen(name="Pet Management Screen", description="Screen for managing pets",
                                     x_dpi="x_dpi", y_dpi="y_dpi", size="LargeScreen", view_elements={petForm, submitButton, showHealthyPetButton, petList})

# Module definition
PetModule: Module = Module(name="Pet Module", screens={PetManagementScreen})

# Application definition
PetApp: Application = Application(name="Pet Management App", package="com.example.petmanagement", versionCode="1",
                                  versionName="1.0", description="Application for managing pet details",
                                  screenCompatibility=True, modules={PetModule})

# Class and Attributes
# This page is related to the class: PetManagement
# Attributes of this class: petID, petName, age, type, weight, length, color, vaccinated, dewormed, sterilized, dateAdded

# Time taken to generate the structural model: 9.04 seconds

# Time taken to generate the GUI model: 36.34 seconds

# Total time taken: 45.39 seconds
