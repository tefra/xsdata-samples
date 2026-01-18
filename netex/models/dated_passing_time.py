from __future__ import annotations

from dataclasses import dataclass

from .dated_passing_time_versioned_child_structure import (
    DatedPassingTimeVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedPassingTime(DatedPassingTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
