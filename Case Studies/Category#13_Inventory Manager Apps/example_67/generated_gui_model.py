
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="product_inventory_manager", description="Product Inventory Manager")

# Input Fields
productNameField: InputField = InputField(name="Product Name", description="Product Name", fieldType="Text")
productPriceField: InputField = InputField(name="Product Price", description="Product Price", fieldType="Number")
productDetailsField: InputField = InputField(name="Product Details", description="Product Details", fieldType="Text")

# Button
addProductButton: Button = Button(name="Add Product Button", description="Add Product", label="Add Product", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add)

# Form
addProductForm: Form = Form(name="Add Product Form", description="Add a New Product", inputFields={productNameField, productPriceField, productDetailsField})

# Search Input Field
searchProductsField: InputField = InputField(name="Search Products", description="Search for products...", fieldType="Search")

# Product List
productList: DataList = DataList(name="Product List", list_sources=set())

# Screen definition
ProductInventoryScreen: Screen = Screen(
    name="ProductInventoryScreen",
    description="Screen for managing product inventory",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Large",
    view_elements={addProductForm, addProductButton, searchProductsField, productList}
)

# Module definition
ProductInventoryModule: Module = Module(name="ProductInventoryModule", screens={ProductInventoryScreen})

# Application definition
ProductInventoryApp: Application = Application(
    name="Product Inventory Manager",
    package="com.example.productinventory",
    versionCode="1",
    versionName="1.0",
    description="Application for managing product inventory",
    screenCompatibility=True,
    modules={ProductInventoryModule}
)

# Class and attributes
# This page is related to the class: ProductInventoryPage
# Attributes of this class: productPrice, productDescription, productName, searchQuery

# Time taken to generate the structural model: 8.88 seconds

# Time taken to generate the GUI model: 27.38 seconds

# Total time taken: 36.27 seconds
