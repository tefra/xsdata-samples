from __future__ import annotations

from dataclasses import dataclass, field

from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .transport_organisation_refs_rel_structure import (
    TransportOrganisationRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfOperatorsStructure(GroupOfEntitiesVersionStructure):
    use_to_exclude: None | bool = field(
        default=None,
        metadata={
            "name": "UseToExclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: None | TransportOrganisationRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
