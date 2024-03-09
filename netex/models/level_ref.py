from dataclasses import dataclass

from .level_ref_structure import LevelRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LevelRef(LevelRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
