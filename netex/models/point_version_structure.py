from dataclasses import dataclass, field

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

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    location: LocationStructure2 | None = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_number: str | None = field(
        default=None,
        metadata={
            "name": "PointNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    types: TypeOfPointRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    projections: ProjectionsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_memberships: GroupMembershipRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "groupMemberships",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
