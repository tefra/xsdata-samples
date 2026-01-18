from dataclasses import dataclass, field

from .accessibility_assessment_versioned_child_structure import (
    AccessibilityAssessmentVersionedChildStructure,
)
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessZoneVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "AccessZone_VersionStructure"

    accessibility_assessment: (
        AccessibilityAssessmentVersionedChildStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    all_areas_wheelchair_accessible: bool | None = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
