from __future__ import annotations

from dataclasses import dataclass

from .meeting_restriction_version_structure import (
    MeetingRestrictionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MeetingRestriction(MeetingRestrictionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
