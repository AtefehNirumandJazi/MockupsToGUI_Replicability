
from besser.BUML.metamodel.gui import *

# Input fields
first_name_input = InputField(name="First Name", description="First Name", fieldType="Text", validationRules="")
last_name_input = InputField(name="Last Name", description="Last Name", fieldType="Text", validationRules="")
email_input = InputField(name="Email", description="Email Address", fieldType="Email", validationRules="")
phone_input = InputField(name="Phone", description="Phone Number", fieldType="Tel", validationRules="")
address_input = InputField(name="Address", description="Address", fieldType="Text", validationRules="")
city_input = InputField(name="City", description="City", fieldType="Text", validationRules="")
state_input = InputField(name="State", description="Please select your state", fieldType="Text", validationRules="")
zip_code_input = InputField(name="Zip Code", description="Zip Code", fieldType="Text", validationRules="")
website_input = InputField(name="Website", description="Website or Domain Name", fieldType="URL", validationRules="")
project_description_input = InputField(name="Project Description", description="Project Description", fieldType="Text", validationRules="")

# Radio buttons for hosting
hosting_yes = InputField(name="Hosting Yes", description="Yes", fieldType="Boolean", validationRules="")
hosting_no = InputField(name="Hosting No", description="No", fieldType="Boolean", validationRules="")

# Button
send_button = Button(name="Send Button", description="Send", label="Send", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Form
contact_form = Form(name="Contact Form", description="Contact Us Today", inputFields={
    first_name_input, last_name_input, email_input, phone_input, address_input, city_input, state_input, zip_code_input, website_input, project_description_input, hosting_yes, hosting_no
})

# Screen
contact_screen = Screen(name="Contact Screen", description="Contact Us Form", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={contact_form, send_button})

# Time taken to generate the structural model: 11.10 seconds

# Time taken to generate the GUI model: 26.29 seconds

# Total time taken: 37.39 seconds
