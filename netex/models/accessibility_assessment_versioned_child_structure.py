from dataclasses import dataclass, field

from .accessibility_limitations_rel_structure import (
    AccessibilityLimitationsRelStructure,
)
from .entity_in_version_structure import VersionedChildStructure
from .limitation_status_enumeration import LimitationStatusEnumeration
from .multilingual_string import MultilingualString
from .suitabilities_rel_structure import SuitabilitiesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityAssessmentVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "AccessibilityAssessment_VersionedChildStructure"

    mobility_impaired_access: LimitationStatusEnumeration | None = field(
        default=None,
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    limitations: AccessibilityLimitationsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suitabilities: SuitabilitiesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    comment: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
