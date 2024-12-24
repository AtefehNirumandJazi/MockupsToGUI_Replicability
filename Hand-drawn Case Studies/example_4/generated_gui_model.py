
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="blog_component", description="Blog App Interface")

# Input Fields
blogTitleInput: InputField = InputField(name="Blog Title Input", description="Input for blog title", fieldType="Text", validationRules="")
blogContentInput: InputField = InputField(name="Blog Content Input", description="Input for blog content", fieldType="Text", validationRules="")
fileInput: InputField = InputField(name="File Input", description="Input for file upload", fieldType="File", validationRules="")
topicsInput: InputField = InputField(name="Topics Input", description="Input for blog topics", fieldType="Text", validationRules="")

# Publish Button
publishButton: Button = Button(name="Publish Button", description="Button to publish blog", label="Publish", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Blog Page Form
blogForm: Form = Form(name="Blog Form", description="Form for creating a blog", inputFields={blogTitleInput, blogContentInput, fileInput, topicsInput})

# Blog Page Screen definition
BlogPageScreen: Screen = Screen(name="BlogPageScreen", description="Screen for blog creation", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={blogForm, publishButton})

# Module definition
BlogModule: Module = Module(name="BlogModule", screens={BlogPageScreen})

# Application definition
BlogApp: Application = Application(name="Blog Application", package="com.example.blogapp", versionCode="1", versionName="1.0", description="A simple blog application", screenCompatibility=True, modules={BlogModule})

# Class and attributes
# This page is related to the BlogPage class in the structural model.
# Attributes of BlogPage class: blogTitle, blogContent, fileName, topics

# Time taken to generate the structural model: 8.09 seconds

# Time taken to generate the GUI model: 22.23 seconds

# Total time taken: 30.32 seconds
