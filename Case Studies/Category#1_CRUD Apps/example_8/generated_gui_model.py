
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="crud_table_component", description="CRUD Table for Vehicle Management")

# Input Fields
makeInput: InputField = InputField(name="Make Input", description="Input for vehicle make", fieldType="Text", validationRules="")
modelInput: InputField = InputField(name="Model Input", description="Input for vehicle model", fieldType="Text", validationRules="")
mileageInput: InputField = InputField(name="Mileage Input", description="Input for vehicle mileage", fieldType="Number", validationRules="")
statusInput: InputField = InputField(name="Status Input", description="Toggle for vehicle status", fieldType="Boolean", validationRules="")

# Form
vehicleForm: Form = Form(name="Vehicle Form", description="Form for vehicle details", inputFields={makeInput, modelInput, mileageInput, statusInput})

# Submit Button
submitButton: Button = Button(name="Submit Button", description="Submit vehicle details", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Add Vehicle Button
addVehicleButton: Button = Button(name="Add Vehicle Button", description="Add a new vehicle", label="Add Vehicle", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Data Source
vehicleDataSource: ModelElement = ModelElement(name="Vehicle Data Source", dataSourceClass=VehiclePage, fields={VehiclePage_make, VehiclePage_model, VehiclePage_mileage, VehiclePage_status})

# Vehicle List
vehicleList: DataList = DataList(name="Vehicle List", description="List of vehicles", list_sources={vehicleDataSource})

# Screen definition
vehicleScreen: Screen = Screen(name="Vehicle Screen", description="Screen for managing vehicles",
                               x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                               view_elements={vehicleForm, submitButton, addVehicleButton, vehicleList})

# Module definition
vehicleModule: Module = Module(name="Vehicle Module", screens={vehicleScreen})

# Application definition
vehicleApp: Application = Application(name="Vehicle Management App", package="com.example.vehiclemanagement", versionCode="1",
                                      versionName="1.0", description="Application for managing vehicles",
                                      screenCompatibility=True, modules={vehicleModule})

# Class and Attributes
# This page is related to the class: VehiclePage
# Attributes of this class: make, model, mileage, status
