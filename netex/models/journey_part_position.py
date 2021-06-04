from dataclasses import dataclass
from netex.models.journey_part_position_versioned_child_structure import JourneyPartPositionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartPosition(JourneyPartPositionVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
