
from besser.BUML.metamodel.gui import *

# Input fields for the form
title_input: InputField = InputField(
    name="Title Input",
    description="Input field for the post title",
    fieldType="Text",
    validationRules=""
)

content_input: InputField = InputField(
    name="Content Input",
    description="Input field for the post content",
    fieldType="Text",
    validationRules=""
)

# Form containing the input fields
create_post_form: Form = Form(
    name="Create Post Form",
    description="Form to create a new blog post",
    inputFields={title_input, content_input}
)

# Button to submit the form
create_post_button: Button = Button(
    name="Create Post Button",
    description="Button to create a new post",
    label="Create Post",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.SubmitForm
)

# List to display all posts
all_posts_list: DataList = DataList(
    name="All Posts List",
    list_sources=set()  # Assuming data source will be added later
)

# Screen containing the form, button, and list
blog_screen: Screen = Screen(
    name="Blog Screen",
    description="Screen for creating a new blog post",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={create_post_form, create_post_button, all_posts_list}
)

# Module containing the screen
blog_module: Module = Module(
    name="Blog Module",
    screens={blog_screen}
)

# Application containing the module
blog_app: Application = Application(
    name="Blog Application",
    package="com.example.blog",
    versionCode="1",
    versionName="1.0",
    description="A web application for creating and managing blog posts.",
    screenCompatibility=True,
    modules={blog_module}
)

# Class and attributes related to this page
# Class: BlogPage
# Attributes: author, category, createdDate, title, tags, isPublished, lastModifiedDate, content

# Time taken to generate the structural model: 7.58 seconds

# Time taken to generate the GUI model: 23.08 seconds

# Total time taken: 30.66 seconds
