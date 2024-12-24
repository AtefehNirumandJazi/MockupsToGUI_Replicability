
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="blog_component", description="Blog Application Interface")

# Input Fields
titleInput: InputField = InputField(name="Title Input", description="Input for blog title", fieldType="Text", validationRules="required")
contentInput: InputField = InputField(name="Content Input", description="Input for blog content", fieldType="Text", validationRules="required")

# Form
createPostForm: Form = Form(name="Create Post Form", description="Form to create a new blog post", inputFields={titleInput, contentInput})

# Button
createPostButton: Button = Button(name="Create Post Button", description="Button to create a new post", label="Create post", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Menu
menu: Menu = Menu(name="Main Menu", description="Main navigation menu", menuItems={
    MenuItem(label="Home"),
    MenuItem(label="About"),
    MenuItem(label="Contact")
})

# Image
blogImage: Image = Image(name="Blog Image", description="Image associated with the blog post")

# List
blogList: DataList = DataList(name="Blog List", description="List of blog posts", list_sources=set())

# Screen definition
blogScreen: Screen = Screen(name="Blog Screen", description="Screen for blog application", x_dpi="x_dpi", y_dpi="y_dpi", size="Large", view_elements={createPostForm, createPostButton, blogImage, blogList, menu})

# Module definition
blogModule: Module = Module(name="Blog Module", screens={blogScreen})

# Application definition
blogApp: Application = Application(name="Blog App", package="com.example.blogapp", versionCode="1", versionName="1.0", description="A simple blog application", screenCompatibility=True, modules={blogModule})

# Class and attributes
# This page is related to the BlogAppPage class in the structural model.
# Attributes of BlogAppPage class:
# - title
# - content
# - publishedDate
# - isPublished
# - lastUpdated
# - numberOfComments
# - authorName

# Time taken to generate the structural model: 9.94 seconds

# Time taken to generate the GUI model: 27.79 seconds

# Total time taken: 37.74 seconds
