from __future__ import annotations

from dataclasses import dataclass

from .meeting_point_service_version_structure import (
    MeetingPointServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MeetingPointService(MeetingPointServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
