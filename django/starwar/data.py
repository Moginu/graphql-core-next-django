luke = dict(
    id='1000', name='Luke Skywalker', homePlanet='Tatooine',
    friends=['1002', '1003', '2000', '2001'], appearsIn=[4, 5, 6])

vader = dict(
    id='1001', name='Darth Vader', homePlanet='Tatooine',
    friends=['1004'], appearsIn=[4, 5, 6])

han = dict(
    id='1002', name='Han Solo', homePlanet=None,
    friends=['1000', '1003', '2001'], appearsIn=[4, 5, 6])

leia = dict(
    id='1003', name='Leia Organa', homePlanet='Alderaan',
    friends=['1000', '1002', '2000', '2001'], appearsIn=[4, 5, 6])

tarkin = dict(
    id='1004', name='Wilhuff Tarkin', homePlanet=None,
    friends=['1001'], appearsIn=[4])

human_data = {
    '1000': luke, '1001': vader, '1002': han, '1003': leia, '1004': tarkin}

threepio = dict(
    id='2000', name='C-3PO', primaryFunction='Protocol',
    friends=['1000', '1002', '1003', '2001'], appearsIn=[4, 5, 6])

artoo = dict(
    id='2001', name='R2-D2', primaryFunction='Astromech',
    friends=['1000', '1002', '1003'], appearsIn=[4, 5, 6])

droid_data = {
    '2000': threepio, '2001': artoo}


def get_character_type(character, info):
        return 'Droid' if character['id'] in droid_data else 'Human'


def get_character(id):
    """Helper function to get a character by ID."""
    return human_data.get(id) or droid_data.get(id)


def get_friends(character, info):
    """Allows us to query for a character's friends."""
    return map(get_character, character.friends)


def get_hero(root, info, episode):
    """Allows us to fetch the undisputed hero of the trilogy, R2-D2."""
    if episode == 5:
        return luke  # Luke is the hero of Episode V
    return artoo  # Artoo is the hero otherwise


def get_human(root, info, id):
    """Allows us to query for the human with the given id."""
    return human_data.get(id)


def get_droid(root, info, id):
    """Allows us to query for the droid with the given id."""
    return droid_data.get(id)


def get_secret_backstory(character, info):
    """Raise an error when attempting to get the secret backstory."""
    raise RuntimeError('secretBackstory is secret.')
