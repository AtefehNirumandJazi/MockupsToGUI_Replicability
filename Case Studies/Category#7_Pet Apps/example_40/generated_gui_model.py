
from library import *

# Input fields for the form
pet_name_field = InputField(name="Pet's name", description="The name of your pet.", fieldType="Text")
owner_name_field = InputField(name="Owner's name", description="Your name.", fieldType="Text")
phone_field = InputField(name="Phone", description="Your phone.", fieldType="Tel")
date_field = InputField(name="Date", description="Appointment date.", fieldType="Date")
hour_field = InputField(name="Hour", description="Appointment hour.", fieldType="Time")
symptoms_field = InputField(name="Symptoms", description="Symptoms description.", fieldType="Text")

# Form definition
appointment_form = Form(
    name="Get an Appointment",
    description="Form to get an appointment.",
    inputFields={pet_name_field, owner_name_field, phone_field, date_field, hour_field, symptoms_field}
)

# Button for adding an appointment
add_button = Button(
    name="Add Button",
    description="Button to add an appointment.",
    label="ADD",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# List for displaying appointments
appointments_list = List(
    name="Add appointments",
    description="List of added appointments.",
    list_sources=set()
)

# Screen definition
appointment_screen = Screen(
    name="Appointment Screen",
    description="Screen for managing appointments.",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={appointment_form, add_button, appointments_list}
)

# Module definition
appointment_module = Module(
    name="Appointment Module",
    screens={appointment_screen}
)

# Application definition
appointment_app = Application(
    name="Appointment Management",
    package="com.example.appointmentmanagement",
    versionCode="1",
    versionName="1.0",
    description="Application for managing appointments.",
    screenCompatibility=True,
    modules={appointment_module}
)

# Class and attributes based on the structural model
# Class: AppointmentPage
# Attributes: appointmentDate, ownerName, appointmentTime, symptoms, phone, petName

# Time taken to generate the structural model: 8.08 seconds

# Time taken to generate the GUI model: 30.06 seconds

# Total time taken: 38.14 seconds
