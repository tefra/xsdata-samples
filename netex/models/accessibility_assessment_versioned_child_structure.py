from dataclasses import dataclass, field
from typing import Optional
from netex.models.accessibility_limitations_rel_structure import AccessibilityLimitationsRelStructure
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.limitation_status_enumeration import LimitationStatusEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.suitabilities_rel_structure import SuitabilitiesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityAssessmentVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "AccessibilityAssessment_VersionedChildStructure"

    mobility_impaired_access: Optional[LimitationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    limitations: Optional[AccessibilityLimitationsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suitabilities: Optional[SuitabilitiesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    comment: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
