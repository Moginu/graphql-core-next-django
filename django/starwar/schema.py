from graphql import build_schema

from .data import *


schema = build_schema("""

    enum Episode { NEWHOPE, EMPIRE, JEDI }

    interface Character {
      id: String!
      name: String
      friends: [Character]
      appearsIn: [Episode]
    }

    type Human implements Character {
      id: String!
      name: String
      friends: [Character]
      appearsIn: [Episode]
      homePlanet: String
    }

    type Droid implements Character {
      id: String!
      name: String
      friends: [Character]
      appearsIn: [Episode]
      primaryFunction: String
    }

    type Query {
      hero(episode: Episode): Character
      human(id: String!): Human
      droid(id: String!): Droid
    }
    """)

schema.query_type.fields['hero'].resolve = get_hero
schema.get_type('Character').resolve_type = get_character_type

# for name, value in schema.get_type('Episode').values.items:
#     value.value = EpisodeEnum[name].value
