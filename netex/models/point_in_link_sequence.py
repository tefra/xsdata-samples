from __future__ import annotations

from dataclasses import dataclass

from .point_in_link_sequence_versioned_child_structure import (
    PointInLinkSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointInLinkSequence(PointInLinkSequenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
