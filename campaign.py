"""
First of all, I'm gonna get rid of all the "DEM"s that I've got in these files.
They're redundant.

Second of all, this will house the Dungeon and Map classes, the former of which
will organize all aspects of the campaign (i.e. NPCs, Communities, etc.) and the
latter will be a map that is composited with the relevant aspects of the
campaign
"""


class Dungeon:
    """
    A Dungeon instance. Hold all relevant "interacteable" aspects of the
    campaign.

    == Public Attributes ==
    TODO: Fill this out

    == Private Attributes ==
    _map:
        The map upon which this campaign takes place
    """


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
