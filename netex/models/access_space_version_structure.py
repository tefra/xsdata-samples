from dataclasses import dataclass, field

from .access_space_ref_structure import AccessSpaceRefStructure
from .access_space_type_enumeration import AccessSpaceTypeEnumeration
from .passage_type_enumeration import PassageTypeEnumeration
from .stop_place_space_version_structure import StopPlaceSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessSpaceVersionStructure(StopPlaceSpaceVersionStructure):
    class Meta:
        name = "AccessSpace_VersionStructure"

    access_space_type: AccessSpaceTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "AccessSpaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passage_type: PassageTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "PassageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_access_space_ref: AccessSpaceRefStructure | None = field(
        default=None,
        metadata={
            "name": "ParentAccessSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
