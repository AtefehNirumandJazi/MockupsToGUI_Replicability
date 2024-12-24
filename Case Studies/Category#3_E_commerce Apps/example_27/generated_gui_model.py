
# Input Fields
first_name_field = InputField(name="First Name", description="First Name", fieldType="Text", validationRules="")
last_name_field = InputField(name="Last Name", description="Last Name", fieldType="Text", validationRules="")
email_field = InputField(name="E-Mail", description="E-Mail Address", fieldType="Email", validationRules="")
phone_field = InputField(name="Phone", description="Phone #", fieldType="Tel", validationRules="")
address_field = InputField(name="Address", description="Address", fieldType="Text", validationRules="")
city_field = InputField(name="City", description="City", fieldType="Text", validationRules="")
state_field = InputField(name="State", description="State", fieldType="Text", validationRules="")
zip_code_field = InputField(name="Zip Code", description="Zip Code", fieldType="Text", validationRules="")
website_field = InputField(name="Website or domain name", description="Website or domain name", fieldType="URL", validationRules="")
project_description_field = InputField(name="Project Description", description="Project Description", fieldType="Text", validationRules="")

# Radio Buttons for Hosting
hosting_yes = InputField(name="Hosting Yes", description="Yes", fieldType="Boolean", validationRules="")
hosting_no = InputField(name="Hosting No", description="No", fieldType="Boolean", validationRules="")

# Button
send_button = Button(name="Send Button", description="Send", label="Send", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Form
contact_form = Form(name="Contact Us Form", description="Contact Us Today!", inputFields={
    first_name_field, last_name_field, email_field, phone_field, address_field, city_field, state_field,
    zip_code_field, website_field, project_description_field, hosting_yes, hosting_no
})

# Screen
contact_screen = Screen(name="Contact Us Screen", description="Contact Us Form Screen", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={
    contact_form, send_button
})

# Module
contact_module = Module(name="Contact Module", screens={contact_screen})

# Application
contact_app = Application(name="Contact Application", package="com.example.contactapp", versionCode="1", versionName="1.0", description="Contact Us Application", screenCompatibility=True, modules={contact_module})

# Class and Attributes
# This page is related to the class: ContactForm
# Attributes of this class:
# - firstName
# - lastName
# - email
# - phone
# - address
# - city
# - state
# - zipCode
# - websiteOrDomainName
# - projectDescription
# - hasHosting

# Time taken to generate the structural model: 9.93 seconds

# Time taken to generate the GUI model: 25.39 seconds

# Total time taken: 35.33 seconds
