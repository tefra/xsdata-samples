from dataclasses import dataclass
from .mode_restriction_assessment_version_structure import (
    ModeRestrictionAssessmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModeRestrictionAssessment(ModeRestrictionAssessmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
