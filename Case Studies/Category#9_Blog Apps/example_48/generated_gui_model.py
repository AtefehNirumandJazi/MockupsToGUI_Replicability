
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="blog_component", description="Blog App Interface")

# Input Fields
titleInput: InputField = InputField(name="Blog Title", description="Title of the blog", fieldType="Text", validationRules="")
contentInput: InputField = InputField(name="Blog Content", description="Content of the blog", fieldType="Text", validationRules="")
categoriesInput: InputField = InputField(name="Blog Categories", description="Categories of the blog", fieldType="Text", validationRules="")

# File Input
attachmentInput: InputField = InputField(name="Blog Attachment", description="Attachment for the blog", fieldType="File", validationRules="")

# Button
publishButton: Button = Button(name="Publish Button", description="Publish the blog", label="Publish", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Form definition
blogForm: Form = Form(name="Blog Form", description="Form to create a blog post", inputFields={titleInput, contentInput, categoriesInput, attachmentInput})

# Screen definition
BlogScreen: Screen = Screen(name="Blog App", description="Screen for creating a blog post", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={blogForm, publishButton})

# Module definition
BlogModule: Module = Module(name="Blog Module", screens={BlogScreen})

# Application definition
BlogApp: Application = Application(name="Blog Application", package="com.example.blogapp", versionCode="1", versionName="1.0", description="A simple blog application", screenCompatibility=True, modules={BlogModule})

# Class and attributes
# This page is related to the class: BlogPage
# Attributes of this class: content, attachment, title, categories

# Time taken to generate the structural model: 7.90 seconds

# Time taken to generate the GUI model: 28.48 seconds

# Total time taken: 36.39 seconds
