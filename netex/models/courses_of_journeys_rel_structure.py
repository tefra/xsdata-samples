from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .course_of_journeys import CourseOfJourneys
from .course_of_journeys_ref import CourseOfJourneysRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CoursesOfJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "coursesOfJourneys_RelStructure"

    course_of_journeys_ref_or_course_of_journeys: Iterable[
        Union[CourseOfJourneysRef, CourseOfJourneys]
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
