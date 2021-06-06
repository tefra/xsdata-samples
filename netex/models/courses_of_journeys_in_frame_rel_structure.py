from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .course_of_journeys import CourseOfJourneys

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CoursesOfJourneysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "coursesOfJourneysInFrame_RelStructure"

    course_of_journeys: List[CourseOfJourneys] = field(
        default_factory=list,
        metadata={
            "name": "CourseOfJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
