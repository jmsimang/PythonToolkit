import pandas as pd


def load_players_data(f):
    """
    Function loads a given csv file into a Pandas DataFrame, and returns it.
    :param f: File path / location
    :return: A DataFrame with the loaded data
    """
    df = pd.read_csv(f, index_col='Name', encoding='latin-1')
    return df


file = '../data-files/football_players-a-26.csv'
# Load csv file into DataFrame
players = load_players_data(file)
print(players.head())


# Create column of rating per year of age
players['Rating Per Year of Age'] = players['Overall'] / players['Age']
print(players['Rating Per Year of Age'].head())


# Drop column just created, specify axis
players.drop('Rating Per Year of Age', axis=1, inplace=True)
print(players.head())


# Grouping data
# Look at the average rating by age
print(players.groupby('Age').mean().head())
# Look at the average rating by age and nationality
print(players.groupby(['Age', 'Nationality']).mean().head())


# Transforming data - using apply() method - lambda and function def
def year_to_month(x):
    """ Convert no of years to no of months """
    return x * 12


print(players['Age'].apply(year_to_month).head())
print(players['Age'].apply(lambda x: x * 12).head())


def position_type(s):
    """ This function converts the individual positions (abbreviations) and classifies
    it as either a forward, midfielder, back or goal keeper
    :param s: The abbreviated player position
    :return: The player classification
    """
    if (s[-2] == 'T') | (s[-2] == 'W'):
        return 'Forward'
    elif s[-2] == 'M':
        return 'Midfielder'
    elif s[-2] == 'B':
        return 'Back'
    else:
        return 'GoalKeeper'


# Create position type column
players['Preferred Positions Type'] = players['Preferred Positions'].apply(position_type)
print(players['Preferred Positions Type'].head())
print(players.head())

# Transforming data - using applymap() function


def to_float(x):
    """
    Function transforms DataFrame attribute columns to type float
    :param x: The attribute column
    :return: The converted attribute column
    """
    if type(x) is int:
        return float(x)
    else:
        return float(x[0:2])


cols = [
    'Overall', 'Acceleration', 'Aggression', 'Agility', 'Balance',
    'Ball control', 'Composure', 'Crossing', 'Curve', 'Dribbling',
    'Finishing', 'Free kick accuracy', 'GK diving', 'GK handling',
    'GK kicking', 'GK positioning', 'GK reflexes', 'Heading accuracy',
    'Interceptions', 'Jumping', 'Long passing', 'Long shots', 'Marking',
    'Penalties', 'Positioning', 'Reactions', 'Short passing', 'Shot power',
    'Sliding tackle', 'Sprint speed', 'Stamina', 'Standing tackle',
    'Strength', 'Vision', 'Volleys'
]
players[cols] = players[cols].applymap(to_float)
print(players.info())


# 1. Country with the highest overall rating on average
print(players.groupby('Nationality').mean()['Overall'].sort_values(ascending=False).head())


# 2. Algeria player with highest overall rating
p = players[players['Preferred Positions Type'] == 'Back']
print(p.head())


# 3. Which back had the highest rating for 'Sliding tackle'?
rating = players[players['Preferred Positions Type'] == 'Back'].max()[2]
p2 = players[players['Preferred Positions Type'] == 'Back']
result = players[(players['Sliding tackle'] == rating) & (players['Preferred Positions Type'] == 'Back')]
print(result)


# 4. Preferred position type of England has on average the highest overall rating
result3 = players[players['Nationality'] == 'England'].groupby('Preferred Positions Type').mean()['Overall']
print(result3)


# 5. Brazil's forwards have a higher average overall rating than the backs
result4 = players[players['Nationality'] == 'Brazil'].groupby('Preferred Positions Type').mean()['Overall']\
    .sort_values(ascending=False)
print(result4)


# 6. Which country has the oldest player?
old = players['Age'].max()
result5 = players[players['Age'] == old]['Nationality']
print(result5)


# 7. Forwards have on average higher Acceleration than Reactions
result6 = players\
    .groupby('Preferred Positions Type').mean()[['Acceleration', 'Reactions']]
print(result6)


# 8. Which attribute is on average the lowest for goalkeepers?
result7 = players[players['Preferred Positions Type'] == 'GoalKeeper'].mean().sort_values()
print(result7)


# 9. Which preferred positions type has the most entries in this dataset?
result8 = players\
    .groupby('Preferred Positions Type')\
    .count()\
    .sort_values(by='Preferred Positions Type', ascending=False)
print(result8)


# 10. Which player from Portugal, that is younger than 25, has the highest overall rating?
result9 = players[(players['Nationality'] == 'Portugal') & (players['Age'] < 25)]
print(result9)
