from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .course_of_journeys import CourseOfJourneys
from .course_of_journeys_ref import CourseOfJourneysRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CoursesOfJourneysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "coursesOfJourneys_RelStructure"

    course_of_journeys_ref: List[CourseOfJourneysRef] = field(
        default_factory=list,
        metadata={
            "name": "CourseOfJourneysRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    course_of_journeys: List[CourseOfJourneys] = field(
        default_factory=list,
        metadata={
            "name": "CourseOfJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )