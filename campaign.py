"""
This will house the Dungeon and Map classes, the former of which
will organize all aspects of the campaign (i.e. NPCs, Communities, etc.) and the
latter will be a map that is composited with the relevant aspects of the
campaign
"""

from __future__ import annotations
from exceptions import *
from typing import List, Optional, Union, Set

# Names for primary communities
PARTY = "Party"
WORLD = "World"


class Dungeon:
    """
    A Dungeon instance. Hold all relevant "interacteable" aspects of the
    campaign.

    TODO: Maybe I'll make all classes private? Since the main module will
    interface directly with an instance of this class. Maybe.

    == Public Attributes ==
    party:
        The Player Party community
    world:
        The highest-level community
    """
    party: Community
    world: Community

    def __init__(self, players: List[Player]) -> None:
        """
        Initialize a Dungeon instance.
        """
        self.party = Community()  # TODO: How is this initialized?


class WorldAsset:
    """
    A non-player entity within the world, such as communities and non-player
    characters

    == Public Attributes ==
    name:
        The name of this WorldAsset
    parent_communities:
        A list of communities this asset immediately belongs to, or None if
        this is the primary campaign community
    event_log:
        A
    """
    name: str
    parent_communities: Optional[List[Community]]

    def __init__(self, name: str, supercomms: Optional[List[Community]] = None) \
            -> None:
        """
        Initialize a WorldAsset instance. If supercomms is not provided,
        initialize the primary
        """
        self.name = name


# noinspection SpellCheckingInspection
class Community(WorldAsset):
    """
    A Community is a grouping of characters. Sometimes it is a city, sometimes
    a family, and sometimes just an arbitrary way of segmenting similar
    characters.

    == Public Attributes ==
    members:
        A set of Characters belonging to this community.
    subcommunities:
        The communities that lie *under* this one, such as families in a city,
        or guilds in a Kingdom
    supercommunity:
        The community this community belongs to
    """
    members: Set[Character]
    subcommunities: Set[Community]
    supercommunity: Optional[Community]

    def __init__(self, name: str, upcomm: Optional[Community] = None) -> None:
        WorldAsset.__init__(self, name)
        self.members = set()
        self.subcommunities = set()
        self.supercommunity = upcomm
        # TODO: Finish this
        #   If there is no supercommunity, this MUST be named "World"

    def __contains__(self, item: WorldAsset) -> bool:
        """
        If <item> is a community, return True if it is a subcommunity of this
        community.
        If <item> is a Character, return true if it is in this community.
        If <item> is not a WorldAsset, raise InvalidWorldAsset error.
        """
        if isinstance(item, Character):
            return self._contains_char_case(item)
        elif isinstance(item, Community):
            return self._contains_comm_case(item)

        raise exceptions.InvalidWorldAsset

    def _contains_char_case(self, character: Character) -> bool:
        """
        A helper for __contains__, taking care of the Character case.
        """
        # Check if the character is a first-level member
        if character in self.members:
            return True
        # If the above did not return, see if there are subcommunities to check
        elif len(self.subcommunities) == 0:
            return False
        # Check through subcommunities
        else:
            for community in self.subcommunities:
                if character in community:
                    return True
        return False

    def _contains_comm_case(self, community: Community) -> bool:
        """
        A helper for __contains__, taking care of the Community case.
        """

    def add_character(self, character: Character) -> bool:
        """
        Add <character> as a direct member of this community

        Return True if this was successful, False otherwise (character
        was already a part of the community, INCLUDING supercommunities)

        TODO: Don't include this here, but when the USER is adding a character,
            check they didn't mean to add it to a SUBcommunity.
        """
        if character not in self:
            self.members.add(character)
            return True
        return False

    def add_subcommunity(self, comm: Community) -> bool:
        """
        Add <comm> as a direct subcommunity of this community

        TODO: Same as add_character, double check with user
        """

    def remove_subcommunity(self, comm: Community) -> bool:
        """
        Remove <comm> from the immediate list of subcommunities
        """

    def promote(self) -> None:
        """
        Promote this community to being a direct subcommunity of its
        supercommunity's supercommunity (i.e. its supercommunity is now the
        same level)
        """


class World(Community):
    """
    The world all other WorldAssets inhabit.
    """

    def __init__(self):
        pass
        # TODO: Finish this

    def promote(self) -> None:
        """
        The World cannot be promoted, so raise an error.
        """
        raise PromoteWorldError


class Character(WorldAsset):
    """
    A character within this campaign. This is an abstract class.

    == Public Attributes ==
    name:
        This Character instance's name
    communities:
        A list of communities of which this Character instance is a direct
        member (i.e. supercommunities are not listed)

    TODO: Implement this
    """
    name: str
    communities: List[Community]

    def __init__(self, name: str, comms: List[Community]) -> None:
        """
        Initialize a character
        """
        WorldAsset.__init__(self, name)


class Player(Character):
    """
    A player of this campaign.

    TODO: Implement this
    """

    def __init__(self, name):
        Character.__init__(self, name, [])


class NonPlayer(Character):
    """
    A non-player character.

    TODO: Implement this
    """

