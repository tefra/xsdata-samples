from dataclasses import dataclass
from netex.models.accessibility_assessment_ref_structure import AccessibilityAssessmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityAssessmentRef(AccessibilityAssessmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
