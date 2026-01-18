from __future__ import annotations

from dataclasses import dataclass

from .onward_call_versioned_child_structure import (
    OnwardCallVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnwardCall(OnwardCallVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
