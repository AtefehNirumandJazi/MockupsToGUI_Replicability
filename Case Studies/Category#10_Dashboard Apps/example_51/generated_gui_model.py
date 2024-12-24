
from besser.BUML.metamodel.gui import *

# Input fields
fullBusinessNameField = InputField(name="Full Business Name", description="Your Full Business Name *", fieldType="Text", validationRules="required")
firstNameField = InputField(name="First Name", description="Your First Name *", fieldType="Text", validationRules="required")
lastNameField = InputField(name="Last Name", description="Your Last Name *", fieldType="Text", validationRules="required")
mainBusinessPhoneNumberField = InputField(name="Main Business Phone Number", description="Main Business Phone Number*", fieldType="Tel", validationRules="required")
businessAddressField = InputField(name="Business Address", description="Business Address*", fieldType="Text", validationRules="required")
businessCityField = InputField(name="Business City", description="Business City*", fieldType="Text", validationRules="required")
businessStateField = InputField(name="Business State", description="Business State*", fieldType="Text", validationRules="required")
businessZipCodeField = InputField(name="Business Zip Code", description="Business Zip Code*", fieldType="Text", validationRules="required")
businessCountryField = InputField(name="Business Country", description="Business Country*", fieldType="Text", validationRules="required")
timeZoneField = InputField(name="TimeZone", description="Choose one..", fieldType="Text", validationRules="required")
businessPhoneAreaCodeField = InputField(name="Business Phone Area Code", description="Business Phone Area Code (e.g. 919, 503)", fieldType="Text", validationRules="required")
businessTypeField = InputField(name="Business Type", description="Select Your Business Type *", fieldType="Text", validationRules="required")
businessWebsiteURLField = InputField(name="Business Website URL", description="Your Business Website URL (optional) Format: https://yourdomain.com *", fieldType="URL", validationRules="optional")

# Form
businessForm = Form(name="Business Form", description="Business Information Form", inputFields={
    fullBusinessNameField, firstNameField, lastNameField, mainBusinessPhoneNumberField, businessAddressField,
    businessCityField, businessStateField, businessZipCodeField, businessCountryField, timeZoneField,
    businessPhoneAreaCodeField, businessTypeField, businessWebsiteURLField
})

# Submit button
submitButton = Button(name="Submit Button", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Screen
businessFormScreen = Screen(name="Business Form Screen", description="Screen for entering business information",
                            x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={businessForm, submitButton})

# Module
businessModule = Module(name="Business Module", screens={businessFormScreen})

# Application
businessApp = Application(name="Business Application", package="com.example.businessapp", versionCode="1",
                          versionName="1.0", description="Application for managing business information",
                          screenCompatibility=True, modules={businessModule})

# Class and attributes
# This page is related to the "BusinessForm" class in the structural model.
# Attributes of the "BusinessForm" class:
# - businessAddress
# - businessCountry
# - mainBusinessPhoneNumber
# - businessPhoneAreaCode
# - businessType
# - firstName
# - businessCity
# - timeZone
# - businessWebsiteURL
# - businessState
# - lastName
# - fullBusinessName
# - businessZipCode

# Time taken to generate the structural model: 10.23 seconds

# Time taken to generate the GUI model: 33.80 seconds

# Total time taken: 44.02 seconds
