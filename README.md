# Daily Puzzles (Manual Archipelago World)

An [Archipelago](https://archipelago.gg) apworld built on the [Manual for Archipelago](https://github.com/ManualForArchipelago/Manual) framework. It turns everyday puzzle games from LinkedIn (Queens, Tango, Pinpoint, Crossclimb, Zip, Mini Sudoku, Wend, Patches) and the New York Times (Wordle, Connections, Mini Crossword, Strands, Spelling Bee, Pips, Letter Boxed, Tiles, Sudoku) into randomized item unlocks and locations.

There's no game or mod to install — progress is tracked manually by solving the real daily puzzles and checking them off with the Manual client/tracker.

## How it works

- Each enabled puzzle type becomes an unlockable item ("Puzzle Unlock").
- Completing a puzzle in real life corresponds to checking off its location in Archipelago.
- Victory is reached once you've collected and completed the number of puzzles set by the **Puzzles Required for Victory** option.
- You start with one random puzzle already unlocked.

## Player options

Configured on the player settings/YAML page:

| Option | Description |
|---|---|
| `include_linkedin` | Include all LinkedIn puzzles as a group |
| `include_nyt` | Include all NYT puzzles as a group |
| `puzzles_required` | Puzzles needed to goal (1–10, capped to the number enabled) |
| `include_queens`, `include_tango`, `include_pinpoint`, `include_crossclimb`, `include_zip`, `include_wend`, `include_patches`, `include_mini_sudoku` | Toggle individual LinkedIn puzzles |
| `include_wordle`, `include_connections`, `include_mini_crossword`, `include_strands`, `include_spelling_bee`, `include_pips`, `include_letter_boxed`, `include_tiles`, `include_sudoku` | Toggle individual NYT puzzles |

Different players can mix and match freely — one player could run only LinkedIn puzzles while another runs only NYT ones.

## Development

This apworld is meant to be dropped into an Archipelago installation's `custom_worlds/` directory, or zipped into a `.apworld` file.

## Links

- [Manual for Archipelago](https://github.com/ManualForArchipelago/Manual)
- [Archipelago](https://archipelago.gg)
