
from BaseClasses import Tutorial
from enum import Enum
from worlds.AutoWorld import World, WebWorld
from .Data import game_table, meta_table
from .Helpers import convert_to_long_string

##############
# Meta Classes
##############
class ManualWeb(WebWorld):
    tutorials = [Tutorial(
        "Daily Puzzles Setup Guide",
        "A guide to configuring the Daily Puzzles Manual world for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["XanthosNLD"]
    )]

######################################
# Convert meta.json data to properties
######################################
def set_world_description(base_doc: str) -> str:
    if meta_table.get("docs", {}).get("apworld_description"):
        return convert_to_long_string(meta_table["docs"]["apworld_description"])

    return base_doc


def set_world_webworld(web: WebWorld) -> WebWorld:
    from .Options import make_options_group
    if meta_table.get("docs", {}).get("web", {}):
        Web_Config = meta_table["docs"]["web"]

        web.theme = Web_Config.get("theme", web.theme)
        web.game_info_languages = Web_Config.get("game_info_languages", web.game_info_languages)
        web.options_presets = Web_Config.get("options_presets", web.options_presets)
        web.options_page = Web_Config.get("options_page", web.options_page)
        web.option_groups = make_options_group()
        if hasattr(web, 'bug_report_page'):
            web.bug_report_page = Web_Config.get("bug_report_page", web.bug_report_page)
        else:
            web.bug_report_page = Web_Config.get("bug_report_page", None)

        if Web_Config.get("tutorials", []):
            tutorials = []
            for tutorial in Web_Config.get("tutorials", []):
                # Converting json to Tutorials
                tutorials.append(Tutorial(
                    tutorial.get("name", "Daily Puzzles Setup Guide"),
                    tutorial.get("description", "A guide to configuring the Daily Puzzles Manual world for Archipelago multiworld games."),
                    tutorial.get("language", "English"),
                    tutorial.get("file_name", "setup_en.md"),
                    tutorial.get("link", "setup/en"),
                    tutorial.get("authors", [game_table.get("creator")])
                ))
            web.tutorials = tutorials
    return web

#################
# Meta Properties
#################
world_description: str = set_world_description("""
    Daily Puzzles is a Manual world built around LinkedIn and NYT daily puzzle games.
    The enabled puzzles are represented by unlock items, and players manually complete those puzzles while Archipelago tracks progress.
    """)
world_webworld: ManualWeb = set_world_webworld(ManualWeb())
