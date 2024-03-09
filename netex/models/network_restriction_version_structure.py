from dataclasses import dataclass, field

from .assignment_version_structure_1 import AssignmentVersionStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkRestrictionVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "NetworkRestriction_VersionStructure"

    restricted: bool = field(
        default=True,
        metadata={
            "name": "Restricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
