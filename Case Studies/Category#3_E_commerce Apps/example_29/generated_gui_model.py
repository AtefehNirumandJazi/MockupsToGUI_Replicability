
from besser.BUML.metamodel.gui import *

# Categories Menu
categoriesMenu: Menu = Menu(
    name="Categories Menu",
    description="Product categories",
    menuItems={
        MenuItem(label="Woman"),
        MenuItem(label="Man"),
        MenuItem(label="Shoes"),
        MenuItem(label="T-shirt"),
        MenuItem(label="Jewellery")
    }
)

# Subscription Form
subscriptionForm: Form = Form(
    name="Subscription Form",
    description="Subscribe to our newsletter",
    inputFields={
        InputField(name="Name", description="Your name", fieldType="Text", validationRules="required"),
        InputField(name="Email", description="Your email", fieldType="Email", validationRules="required")
    }
)

submitButton: Button = Button(
    name="Submit Button",
    description="Submit subscription form",
    label="Submit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.SubmitForm
)

# What's New Section
whatsNewImage: Image = Image(name="What's New Image", description="Featured products")

# Product List
productList: DataList = DataList(
    name="Product List",
    description="Featured products",
    list_sources={
        ModelElement(name="Product Data Source", dataSourceClass=Product, fields=[Product_name, Product_description, Product_price])
    }
)

# Screen definition
HomePageScreen: Screen = Screen(
    name="HomePageScreen",
    description="Main page of the e-commerce site",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={categoriesMenu, subscriptionForm, submitButton, whatsNewImage, productList}
)

# Module definition
ECommerceModule: Module = Module(name="ECommerceModule", screens={HomePageScreen})

# Application definition
ECommerceApp: Application = Application(
    name="E-Commerce App",
    package="com.example.ecommerce",
    versionCode="1",
    versionName="1.0",
    description="An e-commerce application for shopping",
    screenCompatibility=True,
    modules={ECommerceModule}
)

# Class and attributes
# This page is related to the 'Product' class in the structural model.
# Attributes of the 'Product' class: name, description, price



# Time taken to generate the structural model: 13.25 seconds

# Time taken to generate the GUI model: 22.88 seconds

# Total time taken: 36.13 seconds

