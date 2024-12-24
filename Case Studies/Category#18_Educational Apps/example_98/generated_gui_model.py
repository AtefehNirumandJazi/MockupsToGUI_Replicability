
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="AGT Page", description="Welcome to AGT")

# Button for Explore Courses
exploreCoursesButton: Button = Button(
    name="Explore Courses Button",
    description="Button to explore courses",
    label="Explore Courses",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate
)

# Course List
courseList: List = List(
    name="Course List",
    description="List of courses",
    list_sources=set()
)

# Course Items
courseItem1: MenuItem = MenuItem(label="1st standard to 5th")
courseItem2: MenuItem = MenuItem(label="6th standard to 7th")
courseItem3: MenuItem = MenuItem(label="7th standard to 10th")
courseItem4: MenuItem = MenuItem(label="11th and 12th commerce")

# Adding course items to the list
courseList.menuItems = {courseItem1, courseItem2, courseItem3, courseItem4}

# Contact Form
contactForm: Form = Form(
    name="Contact Form",
    description="Form to contact us",
    inputFields={
        InputField(name="Name", description="Your Name", fieldType="Text"),
        InputField(name="Email", description="Your Email", fieldType="Email"),
        InputField(name="Message", description="Your Message", fieldType="Text")
    }
)

# Submit Button
submitButton: Button = Button(
    name="Submit Button",
    description="Submit the contact form",
    label="Submit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.SubmitForm
)

# Screen definition
AGTScreen: Screen = Screen(
    name="AGT Screen",
    description="AGT main page",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={exploreCoursesButton, courseList, contactForm, submitButton}
)

# Module definition
AGTModule: Module = Module(name="AGT Module", screens={AGTScreen})

# Application definition
AGTApp: Application = Application(
    name="AGT Application",
    package="com.example.agt",
    versionCode="1",
    versionName="1.0",
    description="AGT web application",
    screenCompatibility=True,
    modules={AGTModule}
)

# Class and attributes related to this page
# Class: WebPage
# Attributes: title, subtitle

# Time taken to generate the structural model: 10.44 seconds

# Time taken to generate the GUI model: 33.68 seconds

# Total time taken: 44.11 seconds
