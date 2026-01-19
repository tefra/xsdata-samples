from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .retail_device_ref import RetailDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDeviceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "retailDeviceRefs_RelStructure"

    retail_device_ref: Sequence[RetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
