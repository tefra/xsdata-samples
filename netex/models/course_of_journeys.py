from dataclasses import dataclass
from .course_of_journeys_version_structure import (
    CourseOfJourneysVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CourseOfJourneys(CourseOfJourneysVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
