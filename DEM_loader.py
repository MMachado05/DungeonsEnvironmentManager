"""
This module will serve to hold the functions relating to loading and unloading
(encoding and decoding, in the case of json use) DEM files.

TODO: Decide how to save DEM files
    1. Maybe I could do a folder, and within that folder, include files?
    2. One big ass file (this seems impractical and messy)
"""
import os


def create_dungeon() -> None:
    """
    Create a Dungeon directory for the DEM to manage
    """
    pass
    # TODO: Decide how I'm going to implement this (arguments? returns?)


def save_dungeon() -> None:
    """
    Update the values of an already existing dungeon directory
    """
    pass
    # TODO: Decide how I'm going to implement this (arguments? returns?)


def unwrap_dungeon() -> None:
    """
    Decode the files in an existing dungeon directory.

    TODO: Return what, though? Should I include this in another module? Should
        I move the Dungeon class to a separate module? Maybe just include some
        functions and a __main__ block in the DEM_main??? Coding is hard.
    """
    pass
    # TODO: Decide how I'm going to implement this (arguments? returns?)
