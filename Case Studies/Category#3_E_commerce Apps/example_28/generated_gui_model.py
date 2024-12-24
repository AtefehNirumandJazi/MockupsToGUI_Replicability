
# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="payment_component", description="Payment Form")

# Input Fields
cardNumberField: InputField = InputField(name="Card Number", description="Enter card number", fieldType="Text", validationRules="required")
cardHolderField: InputField = InputField(name="Card Holder", description="Enter card holder name", fieldType="Text", validationRules="required")
expirationMonthField: InputField = InputField(name="Expiration Month", description="Select expiration month", fieldType="Text", validationRules="required")
expirationYearField: InputField = InputField(name="Expiration Year", description="Select expiration year", fieldType="Text", validationRules="required")
cvvField: InputField = InputField(name="CVV", description="Enter CVV", fieldType="Number", validationRules="required")

# Form
paymentForm: Form = Form(name="Payment Form", description="Form to enter payment details", inputFields={cardNumberField, cardHolderField, expirationMonthField, expirationYearField, cvvField})

# Submit Button
submitButton: Button = Button(name="Submit Button", description="Submit payment details", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm)

# Payment Screen
PaymentScreen: Screen = Screen(name="Payment Screen", description="Screen for entering payment details", x_dpi="x_dpi", y_dpi="y_dpi", size="Medium", view_elements={paymentForm, submitButton})

# Module definition
PaymentModule: Module = Module(name="Payment Module", screens={PaymentScreen})

# Application definition
PaymentApp: Application = Application(name="Payment Application", package="com.example.paymentapp", versionCode="1", versionName="1.0", description="Application for processing payments", screenCompatibility=True, modules={PaymentModule})

# Class and Attributes
# This page is related to the class: PaymentPage
# Attributes of this class:
# - cardNumber
# - cardHolder
# - expirationMonth
# - expirationYear
# - cvv

# Time taken to generate the structural model: 7.07 seconds

# Time taken to generate the GUI model: 28.22 seconds

# Total time taken: 35.29 seconds
