"""
A module for the custom exceptions I will use in my program.
"""


class InvalidWorldAsset(Exception):
    def __str__(self) -> str:
        return 'Type WorldAsset expected.'


class PromoteWorldError(Exception):
    def __str__(self) -> str:
        return 'The World cannot be promoted to a higher community level.'
