
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="hospital_equipment_inventory_manager", description="Hospital Equipment Inventory Manager")

# Input Fields
equipmentNameField: InputField = InputField(name="equipmentName", description="Equipment Name", fieldType="Text", validationRules="")
serviceOfOriginField: InputField = InputField(name="serviceOfOrigin", description="Service of Origin", fieldType="Text", validationRules="")
operatingStatusField: InputField = InputField(name="operatingStatus", description="Operating Status", fieldType="Text", validationRules="")
registrationNumberField: InputField = InputField(name="registrationNumber", description="Registration Number", fieldType="Text", validationRules="")

# Form
barcodeGenerationForm: Form = Form(name="barcodeGenerationForm", description="Barcode Generation Form", inputFields={equipmentNameField, serviceOfOriginField, operatingStatusField, registrationNumberField})

# Buttons
generateBarcodeButton: Button = Button(name="generateBarcodeButton", description="Generate Barcode", label="Generate Barcode", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)
scanBarcodeButton: Button = Button(name="scanBarcodeButton", description="Scan Barcode", label="Scan Barcode", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Images
barcodeGenerationImage: Image = Image(name="barcodeGenerationImage")
barcodeScanningImage: Image = Image(name="barcodeScanningImage")

# ViewContainer
barcodeGenerationContainer: ViewContainer = ViewContainer(name="barcodeGenerationContainer", description="Barcode Generation Container", view_elements={barcodeGenerationImage, barcodeGenerationForm, generateBarcodeButton})
barcodeScanningContainer: ViewContainer = ViewContainer(name="barcodeScanningContainer", description="Barcode Scanning Container", view_elements={barcodeScanningImage, scanBarcodeButton})

# Menu
footerMenu: Menu = Menu(name="footerMenu", description="Footer Menu", menuItems={MenuItem(label="Home"), MenuItem(label="Inventory"), MenuItem(label="Logout")})

# Screen
hospitalEquipmentScreen: Screen = Screen(name="hospitalEquipmentScreen", description="Hospital Equipment Inventory Manager Screen", x_dpi="x_dpi", y_dpi="y_dpi", size="Large", view_elements={barcodeGenerationContainer, barcodeScanningContainer, footerMenu})

# Module
hospitalEquipmentModule: Module = Module(name="hospitalEquipmentModule", screens={hospitalEquipmentScreen})

# Application
hospitalEquipmentApp: Application = Application(name="Hospital Equipment Inventory Manager", package="com.example.hospital", versionCode="1", versionName="1.0", description="Manage hospital equipment inventory", screenCompatibility=True, modules={hospitalEquipmentModule})

# Class and Attributes
# This page is related to the class: HospitalEquipmentInventoryManager
# Attributes of this class:
# - lastMaintenanceDate
# - serviceOfOrigin
# - equipmentValue
# - registrationNumber
# - acquisitionDate
# - maintenanceSchedule
# - operatingStatus
# - location
# - equipmentName
# - warrantyPeriod
# - isUnderWarranty

# Time taken to generate the structural model: 8.34 seconds

# Time taken to generate the GUI model: 28.31 seconds

# Total time taken: 36.65 seconds
