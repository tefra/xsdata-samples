from dataclasses import dataclass, field
from typing import Optional
from netex.models.access_space_ref_structure import AccessSpaceRefStructure
from netex.models.access_space_type_enumeration import AccessSpaceTypeEnumeration
from netex.models.passage_type_enumeration import PassageTypeEnumeration
from netex.models.stop_place_space_version_structure import StopPlaceSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessSpaceVersionStructure(StopPlaceSpaceVersionStructure):
    class Meta:
        name = "AccessSpace_VersionStructure"

    access_space_type: Optional[AccessSpaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessSpaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passage_type: Optional[PassageTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PassageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_access_space_ref: Optional[AccessSpaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentAccessSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
