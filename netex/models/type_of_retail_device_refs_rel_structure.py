from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_retail_device_ref import TypeOfRetailDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfRetailDeviceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfRetailDeviceRefs_RelStructure"

    type_of_retail_device_ref: Iterable[TypeOfRetailDeviceRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfRetailDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
