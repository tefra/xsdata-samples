from __future__ import annotations

from dataclasses import dataclass

from .mode_restriction_assessment_ref_structure import (
    ModeRestrictionAssessmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModeRestrictionAssessmentRef(ModeRestrictionAssessmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
