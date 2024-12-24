
from besser.BUML.metamodel.gui import *

# DataSource for SuperheroList
datasource_superhero: ModelElement = ModelElement(
    name="Superhero Data Source",
    dataSourceClass=SuperheroList,
    fields=[SuperheroList_name, SuperheroList_power, SuperheroList_badassLevel]
)

# Superhero List definition
superheroList: DataList = DataList(
    name="SuperheroList",
    description="List of superheroes",
    list_sources={datasource_superhero}
)

# Edit and Delete Buttons
editDeleteButton: Button = Button(
    name="Edit/Delete Button",
    description="Edit or delete superhero details",
    label="Edit / Delete",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.OpenForm
)

# Add Superhero Button
addSuperheroButton: Button = Button(
    name="Add Superhero Button",
    description="Add a new superhero",
    label="Add Superhero",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add
)

# Superhero Screen definition
SuperheroScreen: Screen = Screen(
    name="SuperheroScreen",
    description="Screen displaying a list of superheroes",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    size="Medium",
    view_elements={superheroList, editDeleteButton, addSuperheroButton}
)

# Module definition
SuperheroModule: Module = Module(
    name="SuperheroModule",
    screens={SuperheroScreen}
)

# Application definition
SuperheroApp: Application = Application(
    name="Superhero Management",
    package="com.example.superheromanagement",
    versionCode="1",
    versionName="1.0",
    description="Application for managing superheroes",
    screenCompatibility=True,
    modules={SuperheroModule}
)

# Class and attributes
# This page is related to the class: SuperheroList
# Attributes of this class: name, power, badassLevel

# Time taken to generate the structural model: 6.19 seconds

# Time taken to generate the GUI model: 20.69 seconds

# Total time taken: 26.88 seconds
