from __future__ import annotations

from dataclasses import dataclass

from .level_version_structure import LevelVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Level(LevelVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
