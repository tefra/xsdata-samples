from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .group_membership_refs_rel_structure import (
    GroupMembershipRefsRelStructure,
)
from .location_structure_2 import LocationStructure2
from .multilingual_string import MultilingualString
from .projections_rel_structure import ProjectionsRelStructure
from .type_of_point_refs_rel_structure import TypeOfPointRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Point_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    location: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PointNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    types: Optional[TypeOfPointRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    projections: Optional[ProjectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_memberships: Optional[GroupMembershipRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupMemberships",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
