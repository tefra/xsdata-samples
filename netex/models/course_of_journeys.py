from __future__ import annotations

from dataclasses import dataclass

from .course_of_journeys_version_structure import (
    CourseOfJourneysVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CourseOfJourneys(CourseOfJourneysVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
