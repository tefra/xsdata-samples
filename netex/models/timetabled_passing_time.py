from __future__ import annotations

from dataclasses import dataclass

from .timetabled_passing_time_versioned_child_structure import (
    TimetabledPassingTimeVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimetabledPassingTime(TimetabledPassingTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
