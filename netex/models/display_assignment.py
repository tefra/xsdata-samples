from dataclasses import dataclass, field
from typing import Optional
from netex.models.display_assignment_version_structure import DisplayAssignmentVersionStructure
from netex.models.status_enumeration import StatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DisplayAssignment(DisplayAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "type": "Attribute",
        }
    )
    derived_from_version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedFromVersionRef",
            "type": "Attribute",
        }
    )
    responsibility_set_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "responsibilitySetRef",
            "type": "Attribute",
        }
    )
