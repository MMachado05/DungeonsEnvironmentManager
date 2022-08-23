"""
A module for the custom exceptions I will use in my program.
"""


class InvalidWorldAsset(Exception):

    def __str__(self) -> str:
        return 'Type WorldAsset expected.'
