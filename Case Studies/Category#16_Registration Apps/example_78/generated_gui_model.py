
# Input Fields
your_name_field = InputField(name="Your Name", description="Your Name", fieldType="Text", validationRules="")
phone_number_field = InputField(name="Phone Number", description="Phone Number", fieldType="Tel", validationRules="")
service_number_field = InputField(name="Service Number", description="Service Number", fieldType="Text", validationRules="")
residence_area_field = InputField(name="Residence Area", description="Residence Area", fieldType="Text", validationRules="")
fault_location_field = InputField(name="Fault Location", description="Fault Location", fieldType="Text", validationRules="")
type_of_fault_field = InputField(name="Type of Fault", description="Type of Fault", fieldType="Text", validationRules="")

# Submit Button
submit_button = Button(name="Submit Button", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Form
fault_registration_form = Form(name="Fault Registration Form", description="Form for registering faults", inputFields={your_name_field, phone_number_field, service_number_field, residence_area_field, fault_location_field, type_of_fault_field})

# Screen
fault_registration_screen = Screen(name="Fault Registration Screen", description="Screen for fault registration", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={fault_registration_form, submit_button})

# Module
fault_registration_module = Module(name="Fault Registration Module", screens={fault_registration_screen})

# Application
fault_registration_app = Application(name="EthioTelecom Fault Registration App", package="com.example.faultregistration", versionCode="1", versionName="1.0", description="App for registering faults", screenCompatibility=True, modules={fault_registration_module})

# Class and Attributes
# This page is related to the class: FaultRegistrationApp
# Attributes of this class:
# - yourName
# - phoneNumber
# - serviceNumber
# - residenceArea
# - faultLocation
# - typeOfFault

# Time taken to generate the structural model: 6.78 seconds

# Time taken to generate the GUI model: 18.79 seconds

# Total time taken: 25.57 seconds
