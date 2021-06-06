from dataclasses import dataclass
from .course_of_journeys_ref_structure import CourseOfJourneysRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CourseOfJourneysRef(CourseOfJourneysRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
