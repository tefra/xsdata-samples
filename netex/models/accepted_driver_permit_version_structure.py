from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .type_of_driver_permit_ref import TypeOfDriverPermitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AcceptedDriverPermitVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "AcceptedDriverPermit_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_driver_permit_ref: TypeOfDriverPermitRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfDriverPermitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
