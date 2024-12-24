
from besser.BUML.metamodel.gui import *

# Input Fields
productNameInput: InputField = InputField(
    name="Product Name Input",
    description="Input field for product name",
    fieldType="Text",
    validationRules=""
)

productPriceInput: InputField = InputField(
    name="Product Price Input",
    description="Input field for product price",
    fieldType="Number",
    validationRules=""
)

productDetailsInput: InputField = InputField(
    name="Product Details Input",
    description="Input field for product details",
    fieldType="Text",
    validationRules=""
)

searchProductsInput: InputField = InputField(
    name="Search Products Input",
    description="Input field for searching products",
    fieldType="Search",
    validationRules=""
)

# Button
addProductButton: Button = Button(
    name="Add Product Button",
    description="Button to add a new product",
    label="Add Product",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Form
addProductForm: Form = Form(
    name="Add Product Form",
    description="Form to add a new product",
    inputFields={productNameInput, productPriceInput, productDetailsInput}
)

# List
productList: DataList = DataList(
    name="Product List",
    list_sources=set()
)

# Screen
productInventoryScreen: Screen = Screen(
    name="Product Inventory Manager",
    description="Screen for managing product inventory",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={addProductForm, addProductButton, searchProductsInput, productList}
)

# Module
productInventoryModule: Module = Module(
    name="Product Inventory Module",
    screens={productInventoryScreen}
)

# Application
productInventoryApp: Application = Application(
    name="Product Inventory Manager App",
    package="com.example.productinventory",
    versionCode="1",
    versionName="1.0",
    description="Application for managing product inventory",
    screenCompatibility=True,
    modules={productInventoryModule}
)

# Class and Attributes
# This page is related to the class: ProductInventoryPage
# Attributes of this class:
# - productDescription
# - searchInput
# - productPrice
# - productName

# Time taken to generate the structural model: 8.47 seconds

# Time taken to generate the GUI model: 31.56 seconds

# Total time taken: 40.03 seconds
