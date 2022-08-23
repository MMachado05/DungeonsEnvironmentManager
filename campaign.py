"""
This will house the Dungeon and Map classes, the former of which
will organize all aspects of the campaign (i.e. NPCs, Communities, etc.) and the
latter will be a map that is composited with the relevant aspects of the
campaign
"""

from __future__ import annotations
from typing import List, Set


class Dungeon:
    """
    A Dungeon instance. Hold all relevant "interacteable" aspects of the
    campaign.

    == Public Attributes ==
    party:
        The Player Party community
    world:
        The highest-level community
    """
    party: Community
    world: Community

    def __init__(self) -> None:
        """
        Initialize a Dungeon
        """


class Character:
    """
    A character within this campaign. This is an abstract class.

    TODO: Implement this
        Characters will have a LinkedList of communities they belong to, in
        order of "size," to represent priority. Such that, If something happens
        within that community, it affects everyone. Or something.
    """
    communities: List[Community]

    def __init__(self, name: str, comm: Community) -> None:
        """
        Initialize a character
        """


class Player(Character):
    """
    A player of this campaign.

    TODO: Implement this
    """


class NonPlayer(Character):
    """
    A non-player character.

    TODO: Implement this
    """


class Community:
    """
    A Community is a grouping of characters. Sometimes it is a city, sometimes
    a family, and sometimes just an arbitrary way of segmenting similar
    characters.

    TODO: Implement this
        I've gotta composite this with a map, in the case of people of the same
        city, for example. Or household.
    """
    # == Private Attributes ==
    # _subcommunities
    #   The communities that lie *under* this one, such as families in a city,
    #   or guilds in a Kingdom
    # _supercommunity
    #   The community this community belongs to
