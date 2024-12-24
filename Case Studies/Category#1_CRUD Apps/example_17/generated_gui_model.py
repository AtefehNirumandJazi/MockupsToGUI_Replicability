
from library import *

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="dessert_component", description="Dessert Information Table")

# Dessert DataSource definition
datasource_dessert: ModelElement = ModelElement(
    name="Dessert Data Source",
    dataSourceClass=DessertPage,
    fields=[
        DessertPage_dessertName,
        DessertPage_calories,
        DessertPage_fat,
        DessertPage_carbs,
        DessertPage_protein,
        DessertPage_actions
    ]
)

# Dessert List definition
dessertList: DataList = DataList(
    name="DessertList",
    description="A list of desserts with nutritional information",
    list_sources={datasource_dessert}
)

# Dessert page screen definition
DessertPageScreen: Screen = Screen(
    name="DessertPageScreen",
    description="Screen displaying a list of desserts with their nutritional information",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="LargeScreen",
    view_elements={dessertList}
)

# Module definition
DessertModule: Module = Module(
    name="dessert_module",
    screens={DessertPageScreen}
)

# Application definition
DessertApp: Application = Application(
    name="Dessert Management",
    package="com.example.dessertmanagement",
    versionCode="1",
    versionName="1.0",
    description="An application for managing dessert nutritional information.",
    screenCompatibility=True,
    modules={DessertModule}
)

# Class and attributes
# This page is related to the class: DessertPage
# Attributes of this class:
# - dessertName: StringType
# - calories: IntegerType
# - fat: FloatType
# - carbs: FloatType
# - protein: IntegerType
# - actions: StringType

# Time taken to generate the structural model: 6.90 seconds

# Time taken to generate the GUI model: 21.92 seconds

# Total time taken: 28.82 seconds
