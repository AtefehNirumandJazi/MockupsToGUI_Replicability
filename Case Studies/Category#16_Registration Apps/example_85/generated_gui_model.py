
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="student_registration_form", description="Student Registration Form")

# Input Fields for Student Personal Details
fileInput: InputField = InputField(name="file", description="File Upload", fieldType="File")
nameInput: InputField = InputField(name="name", description="Name", fieldType="Text")
dobInput: InputField = InputField(name="dateOfBirth", description="Date of Birth", fieldType="Date")
emailInput: InputField = InputField(name="emailAddress", description="Email Address", fieldType="Email")
contactInput: InputField = InputField(name="contact", description="Contact", fieldType="Text")

# Buttons for Student Personal Details
saveButton1: Button = Button(name="saveButton1", description="Save", label="Save", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)
clearButton1: Button = Button(name="clearButton1", description="Clear", label="Clear", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)

# Form for Student Personal Details
studentPersonalDetailsForm: Form = Form(name="studentPersonalDetailsForm", description="Student Personal Details", inputFields={fileInput, nameInput, dobInput, emailInput, contactInput})

# Input Fields for Area of Residence
countyInput: InputField = InputField(name="county", description="County", fieldType="Text")
subcountyInput: InputField = InputField(name="subcounty", description="Subcounty", fieldType="Text")
divisionInput: InputField = InputField(name="division", description="Division", fieldType="Text")
wardInput: InputField = InputField(name="ward", description="Ward", fieldType="Text")
locationInput: InputField = InputField(name="location", description="Location", fieldType="Text")
villageInput: InputField = InputField(name="village", description="Village", fieldType="Text")

# Buttons for Area of Residence
saveButton2: Button = Button(name="saveButton2", description="Save", label="Save", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)
clearButton2: Button = Button(name="clearButton2", description="Clear", label="Clear", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)

# Form for Area of Residence
areaOfResidentForm: Form = Form(name="areaOfResidentForm", description="Area of Residence", inputFields={countyInput, subcountyInput, divisionInput, wardInput, locationInput, villageInput})

# Input Fields for Course Details
studentNumberInput: InputField = InputField(name="studentNumber", description="Student Number", fieldType="Text")
levelInput: InputField = InputField(name="level", description="Level", fieldType="Text")
programInput: InputField = InputField(name="program", description="Program", fieldType="Text")
studentEmailInput: InputField = InputField(name="studentEmail", description="Student Email", fieldType="Email")

# Buttons for Course Details
saveButton3: Button = Button(name="saveButton3", description="Save", label="Save", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)
clearButton3: Button = Button(name="clearButton3", description="Clear", label="Clear", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)

# Form for Course Details
courseDetailsForm: Form = Form(name="courseDetailsForm", description="Course Details", inputFields={studentNumberInput, levelInput, programInput, studentEmailInput})

# Screen definition
studentRegistrationScreen: Screen = Screen(
    name="StudentRegistrationScreen",
    description="Student Registration Form Screen",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={studentPersonalDetailsForm, saveButton1, clearButton1, areaOfResidentForm, saveButton2, clearButton2, courseDetailsForm, saveButton3, clearButton3}
)

# Module definition
studentRegistrationModule: Module = Module(name="studentRegistrationModule", screens={studentRegistrationScreen})

# Application definition
studentRegistrationApp: Application = Application(
    name="StudentRegistrationApp",
    package="com.example.studentregistration",
    versionCode="1",
    versionName="1.0",
    description="An application for student registration.",
    screenCompatibility=True,
    modules={studentRegistrationModule}
)

# Class related to this page: StudentRegistrationForm
# Attributes: emailAddress, dateOfBirth, contact, name, file

# Time taken to generate the structural model: 8.84 seconds

# Time taken to generate the GUI model: 82.86 seconds

# Total time taken: 91.70 seconds
