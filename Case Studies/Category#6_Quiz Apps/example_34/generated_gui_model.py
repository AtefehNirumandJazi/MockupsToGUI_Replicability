
from besser.BUML.metamodel.gui import *

# ViewComponent definition
progressBar: ViewComponent = ViewComponent(name="Progress Bar", description="0% complete")

# Question Text
questionText: ViewComponent = ViewComponent(name="Question Text", description="What is the full form of HTTP?")

# Answer Options
answerOptionA: Button = Button(name="Answer Option A", description="Hyper text transfer package", label="a. Hyper text transfer package", buttonType=ButtonType.TextButton)
answerOptionB: Button = Button(name="Answer Option B", description="Hyper text transfer protocol", label="b. Hyper text transfer protocol", buttonType=ButtonType.TextButton)
answerOptionC: Button = Button(name="Answer Option C", description="Hyphenation text test program", label="c. Hyphenation text test program", buttonType=ButtonType.TextButton)
answerOptionD: Button = Button(name="Answer Option D", description="None of the above", label="d. None of the above", buttonType=ButtonType.TextButton)

# Navigation Buttons
backButton: Button = Button(name="Back Button", description="Go back", label="Back", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Back)
skipButton: Button = Button(name="Skip Button", description="Skip question", label="Skip", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Next)

# Quiz Screen definition
QuizScreen: Screen = Screen(name="Quiz Screen", description="Quiz interface for answering questions",
                            x_dpi="x_dpi", y_dpi="y_dpi", size="Medium",
                            view_elements={progressBar, questionText, answerOptionA, answerOptionB, answerOptionC, answerOptionD, backButton, skipButton})

# Module definition
QuizModule: Module = Module(name="quiz_module", screens={QuizScreen})

# Application definition
QuizApp: Application = Application(name="VueQuiz", package="com.example.vuequiz", versionCode="1",
                                   versionName="1.0", description="A quiz application for testing knowledge.",
                                   screenCompatibility=True, modules={QuizModule})

# Class and attributes
# This page is related to the class: QuizPage
# Attributes of this class based on the structural model:
# - currentQuestion
# - answerOptionA
# - answerOptionB
# - answerOptionC
# - answerOptionD
# - progressPercentage

# Time taken to generate the structural model: 11.64 seconds

# Time taken to generate the GUI model: 27.66 seconds

# Total time taken: 39.31 seconds
