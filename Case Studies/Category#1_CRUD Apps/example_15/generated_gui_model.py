
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="product_component", description="Product Management Interface")

# Button for adding a product
addProductButton: Button = Button(
    name="Add Product Button",
    description="Button to add a new product",
    label="Add product",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Input field for product name
productNameInput: InputField = InputField(
    name="Product Name Input",
    description="Input field for product name",
    fieldType="Text",
    validationRules=""
)

# Data source for product list
productDataSource: ModelElement = ModelElement(
    name="Product Data Source",
    dataSourceClass=Product,
    fields=[Product_name, Product_description, Product_price]
)

# List of products
productList: DataList = DataList(
    name="Product List",
    description="List of products",
    list_sources={productDataSource}
)

# Screen definition
ProductScreen: Screen = Screen(
    name="Product Management Screen",
    description="Screen for managing products",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={addProductButton, productNameInput, productList}
)

# Module definition
ProductModule: Module = Module(
    name="Product Module",
    screens={ProductScreen}
)

# Application definition
ProductApp: Application = Application(
    name="Product Management App",
    package="com.example.productmanagement",
    versionCode="1",
    versionName="1.0",
    description="An application for managing products.",
    screenCompatibility=True,
    modules={ProductModule}
)

# Class and attributes
# This page is related to the 'Product' class.
# Attributes of the 'Product' class: name, description, price.

# Time taken to generate the structural model: 7.56 seconds

# Time taken to generate the GUI model: 26.51 seconds

# Total time taken: 34.07 seconds
