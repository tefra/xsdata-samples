from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .course_of_journeys import CourseOfJourneys
from .course_of_journeys_ref import CourseOfJourneysRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CoursesOfJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "coursesOfJourneys_RelStructure"

    course_of_journeys_ref_or_course_of_journeys: Sequence[
        CourseOfJourneysRef | CourseOfJourneys
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CourseOfJourneysRef",
                    "type": CourseOfJourneysRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CourseOfJourneys",
                    "type": CourseOfJourneys,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
