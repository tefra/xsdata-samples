from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_applicable_segment import TypeApplicableSegment

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class ApplicableSegment(TypeApplicableSegment):
    """
    Applicable air segment.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
