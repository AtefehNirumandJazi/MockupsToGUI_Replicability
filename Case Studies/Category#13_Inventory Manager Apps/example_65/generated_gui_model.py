
from besser.BUML.metamodel.gui import *
from library import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="inventory_manager_component", description="Inventory Management Interface")

# Menu definition
inventoryMenu: Menu = Menu(name="Inventory Menu", description="Navigation Menu")
currentInventoryItem: MenuItem = MenuItem(label="Current Inventory")
incomingPurchaseItem: MenuItem = MenuItem(label="Incoming Purchase")
outgoingOrdersItem: MenuItem = MenuItem(label="Outgoing Orders")
inventoryMenu.menuItems = {currentInventoryItem, incomingPurchaseItem, outgoingOrdersItem}

# Form definition
inventoryForm: Form = Form(name="Inventory Form", description="Form to add or reset inventory items")
productNameField: InputField = InputField(name="Product Name", description="Enter product name", fieldType="Text")
productBrandField: InputField = InputField(name="Product Brand", description="Enter product brand", fieldType="Text")
quantityField: InputField = InputField(name="Quantity", description="Enter quantity", fieldType="Number")
productPriceField: InputField = InputField(name="Product Price", description="Enter product price", fieldType="Number")
inventoryForm.inputFields = {productNameField, productBrandField, quantityField, productPriceField}

# Buttons
clearInventoryButton: Button = Button(name="Clear Inventory Button", description="Clear inventory", label="Clear Inventory", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete)
addButton: Button = Button(name="Add Button", description="Add inventory item", label="Add", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)
resetButton: Button = Button(name="Reset Button", description="Reset form", label="Reset", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)

# DataSource definition
datasource_inventory: ModelElement = ModelElement(name="Inventory Data Source", dataSourceClass=Inventory, fields=[Inventory_productName, Inventory_productBrand, Inventory_quantity, Inventory_productPrice])

# Inventory List definition
inventoryList: DataList = DataList(name="Inventory List", description="List of current inventory items", list_sources={datasource_inventory})

# Screen definition
InventoryScreen: Screen = Screen(name="Inventory Manager Screen", description="Screen for managing inventory",
                                 x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                                 view_elements={inventoryMenu, clearInventoryButton, inventoryForm, addButton, resetButton, inventoryList})

# Module definition
InventoryModule: Module = Module(name="Inventory Module", screens={InventoryScreen})

# Application definition
InventoryApp: Application = Application(name="Inventory Management App", package="com.example.inventorymanagement", versionCode="1",
                                        versionName="1.0", description="Application for managing inventory operations",
                                        screenCompatibility=True, modules={InventoryModule})

# Class and attributes
# This page is related to the Inventory class in the structural model.
# Attributes of the Inventory class:
# - productName
# - productBrand
# - quantity
# - productPrice

# Time taken to generate the structural model: 11.40 seconds

# Time taken to generate the GUI model: 34.95 seconds

# Total time taken: 46.35 seconds
