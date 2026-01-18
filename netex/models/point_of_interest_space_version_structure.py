from __future__ import annotations

from dataclasses import dataclass, field

from .passage_type_enumeration import PassageTypeEnumeration
from .point_of_interest_component_version_structure import (
    PointOfInterestComponentVersionStructure,
)
from .point_of_interest_entrances_rel_structure import (
    PointOfInterestEntrancesRelStructure,
)
from .point_of_interest_space_ref_structure import (
    PointOfInterestSpaceRefStructure,
)
from .point_of_interest_space_type_enumeration import (
    PointOfInterestSpaceTypeEnumeration,
)
from .point_of_interest_space_version_structure_access_space_type import (
    PointOfInterestSpaceVersionStructureAccessSpaceType,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestSpaceVersionStructure(
    PointOfInterestComponentVersionStructure
):
    class Meta:
        name = "PointOfInterestSpace_VersionStructure"

    access_space_type: (
        None | PointOfInterestSpaceVersionStructureAccessSpaceType
    ) = field(
        default=None,
        metadata={
            "name": "AccessSpaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_of_interest_space_type: (
        None | PointOfInterestSpaceTypeEnumeration
    ) = field(
        default=None,
        metadata={
            "name": "PointOfInterestSpaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passage_type: None | PassageTypeEnumeration = field(
        default=None,
        metadata={
            "name": "PassageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_point_of_interest_space_ref: (
        None | PointOfInterestSpaceRefStructure
    ) = field(
        default=None,
        metadata={
            "name": "ParentPointOfInterestSpaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrances: None | PointOfInterestEntrancesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
