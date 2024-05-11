from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .type_of_driver_permit_ref import TypeOfDriverPermitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AcceptedDriverPermitVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "AcceptedDriverPermit_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_driver_permit_ref: Optional[TypeOfDriverPermitRef] = field(
        default=None,
        metadata={
            "name": "TypeOfDriverPermitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
