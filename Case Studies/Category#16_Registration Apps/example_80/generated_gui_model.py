
# Input Fields
name_input = InputField(name="Name", description="Enter your name", fieldType="Text", validationRules="")
year_input = InputField(name="Year of Studying", description="Enter your year of study", fieldType="Number", validationRules="")
branch_input = InputField(name="Engineering Branch", description="Enter your engineering branch", fieldType="Text", validationRules="")

# Button
next_button = Button(name="Next Button", description="Proceed to the next step", label="Next", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Next)

# Form
registration_form = Form(name="College Bus Registration Form", description="Form for college bus registration", inputFields={name_input, year_input, branch_input})

# Screen
registration_screen = Screen(name="College Bus Registration", description="College Bus Registration Screen", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={registration_form, next_button})

# Module
registration_module = Module(name="Registration Module", screens={registration_screen})

# Application
registration_app = Application(name="College Bus Registration App", package="com.example.collegebusregistration", versionCode="1", versionName="1.0", description="App for college bus registration", screenCompatibility=True, modules={registration_module})

# Class and Attributes
# This page is related to the class: CollegeBusRegistration
# Attributes of this class:
# - studentName: StringType
# - yearOfStudy: IntegerType
# - branchOfEngineering: StringType
# - isHosteller: BooleanType
# - registrationDate: DateType

# Time taken to generate the structural model: 11.48 seconds

# Time taken to generate the GUI model: 16.47 seconds

# Total time taken: 27.94 seconds
