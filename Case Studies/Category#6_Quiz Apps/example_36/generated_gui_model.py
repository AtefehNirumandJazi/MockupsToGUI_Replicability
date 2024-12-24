
from besser.BUML.metamodel.gui import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="quiz_component", description="CSS Quiz Page")

# Question Text
questionText: InputField = InputField(
    name="question_text",
    description="What does CSS stand for?",
    fieldType="Text"
)

# Option A
optionA: Button = Button(
    name="option_a",
    description="Option A: Cascading Style Sheets",
    label="A",
    buttonType=ButtonType.RaisedButton
)

# Option B
optionB: Button = Button(
    name="option_b",
    description="Option B: Creative Style Sheets",
    label="B",
    buttonType=ButtonType.RaisedButton
)

# Option C
optionC: Button = Button(
    name="option_c",
    description="Option C: Computer Style Sheets",
    label="C",
    buttonType=ButtonType.RaisedButton
)

# Option D
optionD: Button = Button(
    name="option_d",
    description="Option D: Colorful Style Sheets",
    label="D",
    buttonType=ButtonType.RaisedButton
)

# Check Answer Button
checkAnswerButton: Button = Button(
    name="check_answer",
    description="Check my answer",
    label="Check my answer",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Confirm
)

# Quiz Screen definition
QuizScreen: Screen = Screen(
    name="CSS Quiz Screen",
    description="Screen for CSS Quiz",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={questionText, optionA, optionB, optionC, optionD, checkAnswerButton}
)

# Module definition
QuizModule: Module = Module(name="quiz_module", screens={QuizScreen})

# Application definition
QuizApp: Application = Application(
    name="CSS Quiz App",
    package="com.example.cssquiz",
    versionCode="1",
    versionName="1.0",
    description="An application for CSS quizzes.",
    screenCompatibility=True,
    modules={QuizModule}
)

# Class and attributes
# This page is related to the class: QuizPage
# Attributes of this class:
# - dateCreated: DateType
# - optionD: StringType
# - questionText: StringType
# - optionA: StringType
# - title: StringType
# - isAnswered: BooleanType
# - questionNumber: IntegerType
# - optionB: StringType
# - timeLimit: TimeType
# - optionC: StringType

# Time taken to generate the structural model: 9.73 seconds

# Time taken to generate the GUI model: 25.13 seconds

# Total time taken: 34.85 seconds
