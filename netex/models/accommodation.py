from __future__ import annotations

from dataclasses import dataclass

from .accommodation_versioned_child_structure import (
    AccommodationVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Accommodation(AccommodationVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
