
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="Medical Inventory Manager", description="Manage medical inventory and patient data")

# Inventory Management Elements
inventoryFileButton: Button = Button(name="Choose Inventory File", label="Choose file", buttonType=ButtonType.TextButton)
loadInventoryButton: Button = Button(name="Load Inventory CSV", label="Load Inventory CSV", buttonType=ButtonType.RaisedButton)
exportInventoryButton: Button = Button(name="Export Inventory CSV", label="Export Inventory CSV", buttonType=ButtonType.RaisedButton)

inventoryDataSource: ModelElement = ModelElement(name="Inventory Data Source", dataSourceClass=Inventory, fields=[
    Inventory_ID, Inventory_Name, Inventory_Category, Inventory_Quantity, Inventory_Price
])
inventoryList: DataList = DataList(name="InventoryList", description="List of inventory items", list_sources={inventoryDataSource})

# Patient Management Elements
patientFileButton: Button = Button(name="Choose Patient File", label="Choose file", buttonType=ButtonType.TextButton)
loadPatientButton: Button = Button(name="Load Patient CSV", label="Load Patient CSV", buttonType=ButtonType.RaisedButton)
exportPatientButton: Button = Button(name="Export Patient CSV", label="Export Patient CSV", buttonType=ButtonType.RaisedButton)

patientForm: Form = Form(name="PatientForm", description="Form to add a new patient", inputFields={
    InputField(name="Patient ID", fieldType="Number"),
    InputField(name="Patient Name", fieldType="Text"),
    InputField(name="Patient Age", fieldType="Number"),
    InputField(name="Patient Condition", fieldType="Text")
})
addPatientButton: Button = Button(name="Add Patient", label="Add Patient", buttonType=ButtonType.RaisedButton)

patientDataSource: ModelElement = ModelElement(name="Patient Data Source", dataSourceClass=PatientManagement, fields=[
    PatientManagement_ID, PatientManagement_Name, PatientManagement_Age, PatientManagement_Condition
])
patientList: DataList = DataList(name="PatientList", description="List of patients", list_sources={patientDataSource})

# Screen definition
MedicalInventoryScreen: Screen = Screen(name="MedicalInventoryScreen", description="Screen for managing medical inventory and patients",
                                        x_dpi="x_dpi", y_dpi="y_dpi", size="Large",
                                        view_elements={inventoryFileButton, loadInventoryButton, exportInventoryButton, inventoryList,
                                                       patientFileButton, loadPatientButton, exportPatientButton, patientForm, addPatientButton, patientList})

# Module definition
MedicalModule: Module = Module(name="MedicalModule", screens={MedicalInventoryScreen})

# Application definition
MedicalApp: Application = Application(name="Medical Inventory Manager", package="com.example.medicalinventory", versionCode="1",
                                      versionName="1.0", description="Application for managing medical inventory and patient data",
                                      screenCompatibility=True, modules={MedicalModule})

# Class and Attributes
# This page is related to the class: PatientManagement
# Attributes of this class: ID, Name, Age, Condition

# Time taken to generate the structural model: 12.31 seconds

# Time taken to generate the GUI model: 28.76 seconds

# Total time taken: 41.08 seconds
