"""
First of all, I'm gonna get rid of all the "DEM"s that I've got in these files.
They're redundant.

Second of all, this will house the Dungeon and Map classes, the former of which
will organize all aspects of the campaign (i.e. NPCs, Communities, etc.) and the
latter will be a map that is composited with the relevant aspects of the
campaign
"""

from __future__ import annotations
from dem_objects import LinkedList


class Dungeon:
    """
    A Dungeon instance. Hold all relevant "interacteable" aspects of the
    campaign.

    == Public Attributes ==
    TODO: Fill this out

    """
    # == Private Attributes ==
    # _map:
    #   The map upon which this campaign takes place
    pass


class Map:
    """
    TODO: What exactly is this?

    == Private attributes ==
    _maps:
        A tuple of sub-maps within this map (i.e. a map of a city within a
        nation, a house within a city, etc). While the way a location is
        organized may change, the actual sub-locations will not, and as such this
        is an immutable type.
    """
    pass


class Character:
    """
    A character within this campaign. This is an abstract class.

    TODO: Implement this
        Characters will have a LinkedList of communities they belong to, in
        order of "size," to represent priority. Such that, If something happens
        within that community, it affects everyone. Or something.
    """

    communities: LinkedList


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
        city, for example. Or househould.
    """
