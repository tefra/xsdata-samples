from __future__ import annotations

from dataclasses import dataclass

from .accessibility_assessment_versioned_child_structure import (
    AccessibilityAssessmentVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessibilityAssessment(AccessibilityAssessmentVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
