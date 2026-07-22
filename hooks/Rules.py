from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

PUZZLES = {
    "Queens Unlock": ("include_queens", "include_linkedin"),
    "Tango Unlock": ("include_tango", "include_linkedin"),
    "Pinpoint Unlock": ("include_pinpoint", "include_linkedin"),
    "Crossclimb Unlock": ("include_crossclimb", "include_linkedin"),
    "Zip Unlock": ("include_zip", "include_linkedin"),
    "Wend Unlock": ("include_wend", "include_linkedin"),
    "Patches Unlock": ("include_patches", "include_linkedin"),
    "Mini Sudoku Unlock": ("include_mini_sudoku", "include_linkedin"),
    "Wordle Unlock": ("include_wordle", "include_nyt"),
    "Connections Unlock": ("include_connections", "include_nyt"),
    "Mini Crossword Unlock": ("include_mini_crossword", "include_nyt"),
    "Strands Unlock": ("include_strands", "include_nyt"),
    "Spelling Bee Unlock": ("include_spelling_bee", "include_nyt"),
    "Pips (Easy) Unlock": ("include_pips", "include_nyt"),
    "Pips (Medium) Unlock": ("include_pips", "include_nyt"),
    "Pips (Hard) Unlock": ("include_pips", "include_nyt"),
    "Letter Boxed Unlock": ("include_letter_boxed", "include_nyt"),
    "Tiles Unlock": ("include_tiles", "include_nyt"),
    "Sudoku (Easy) Unlock": ("include_sudoku", "include_nyt"),
    "Sudoku (Medium) Unlock": ("include_sudoku", "include_nyt"),
    "Sudoku (Hard) Unlock": ("include_sudoku", "include_nyt"),
}


def enabledPuzzles(world):
    return [
        name
        for name, (puzzle_opt, site_opt) in PUZZLES.items()
        if getattr(world.options, puzzle_opt).value
        and getattr(world.options, site_opt).value
    ]


def requiresPuzzleGoal(world: World, multiworld: MultiWorld, state: CollectionState, player: int) -> bool:
    enabled = enabledPuzzles(world)
    needed = min(world.options.puzzles_required.value, len(enabled))
    count = sum(1 for name in enabled if state.has(name, player))
    return count >= needed
