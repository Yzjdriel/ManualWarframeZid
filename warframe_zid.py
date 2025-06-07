from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

#Options Dataclass
@dataclass
class WarframeZidArchipelagoOptions:
  include_hard_challenges: IncludeHardChallenges
#end classdef
  
#Main class
class WarframeZid(Game):
  name = "Warframe_Zid"
  platform = KeymastersKeepGamePlatforms.PC
  
  is_adult_only_or_unrated = False
  options_cls = WarframeZidArchipelagoOptions

  #Optional Game Constraints
  def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
    return [
      GameObjectiveTemplate(
        label="Cannot use WEAPONS",
        data={
          "WEAPONS": (self.weaponclasses, 1)
        },
      ),
    ]
    #enddef

    #Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
      return [
        GameObjectiveTemplate(
          label="Clear the full Manual",
          is_time_consuming=True,
          is_difficult=True,
          weight=1,
        ),
        GameObjectiveTemplate(
          label="Clear PLANET Solo",
          data={
            "PLANET": (self.planets, 1)
          },
          is_time_consuming=True,
          is_difficult=False,
          weight=3,
        ),
        GameObjectiveTemplate(
          label="Do the Sortie",
          is_time_consuming=False,
          is_difficult=False,
          weight=2,
        ),
        GameObjectiveTemplate(
          label="Do an Archon Hunt",
          is_time_consuming=False,
          is_difficult=False,
          weight=2,
        ),
        GameObjectiveTemplate(
          label="Clear PLANET Solo with WARFRAME",
          data={
            "PLANET": (self.planets, 1),
            "WARFRAME": (self.warframes, 1)
          },
          is_time_consuming=True,
          is_difficult=False,
          weight=3,
        ),
      ]
    #enddef

    #Option Properties
    @property
    def include_hard_challenges(self) -> bool:
      return bool(self.archipelago_options_include_hard_challenges.value)

    #Datasets
    @staticmethod
    def weaponclasses() -> List[str]:
      return [
        "Automatic Rifles",
        "Shotguns",
        "Sniper Rifles",
        "Semiautomatic Rifles",
        "Beam Weapons",
        "Bows",
        "Pistols",
        "Swords",
        "Whips",
        "Fisticuffs",
        "Polearms",
        "Exalted Weapons",
      ]
    
#end classdef
