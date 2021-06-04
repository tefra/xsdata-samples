from dataclasses import dataclass
from netex.models.level_version_structure import LevelVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Level(LevelVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
