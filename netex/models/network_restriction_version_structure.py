from dataclasses import dataclass, field
from netex.models.assignment_version_structure_2 import AssignmentVersionStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkRestrictionVersionStructure(AssignmentVersionStructure2):
    class Meta:
        name = "NetworkRestriction_VersionStructure"

    restricted: bool = field(
        default=True,
        metadata={
            "name": "Restricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
