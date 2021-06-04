from dataclasses import dataclass, field
from typing import Optional
from netex.models.passage_type_enumeration import PassageTypeEnumeration
from netex.models.point_of_interest_component_version_structure import PointOfInterestComponentVersionStructure
from netex.models.point_of_interest_entrances_rel_structure import PointOfInterestEntrancesRelStructure
from netex.models.point_of_interest_space_descriptor_group_access_space_type import PointOfInterestSpaceDescriptorGroupAccessSpaceType
from netex.models.point_of_interest_space_ref_structure import PointOfInterestSpaceRefStructure
from netex.models.point_of_interest_space_type_enumeration import PointOfInterestSpaceTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestSpaceVersionStructure(PointOfInterestComponentVersionStructure):
    class Meta:
        name = "PointOfInterestSpace_VersionStructure"

    access_space_type: Optional[PointOfInterestSpaceDescriptorGroupAccessSpaceType] = field(
        default=None,
        metadata={
            "name": "AccessSpaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_space_type: Optional[PointOfInterestSpaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PointOfInterestSpaceType",
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
    parent_point_of_interest_space_ref: Optional[PointOfInterestSpaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentPointOfInterestSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrances: Optional[PointOfInterestEntrancesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
