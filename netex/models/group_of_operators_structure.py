from dataclasses import dataclass, field
from typing import Optional
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .transport_organisation_refs_rel_structure import (
    TransportOrganisationRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfOperatorsStructure(GroupOfEntitiesVersionStructure):
    use_to_exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseToExclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[TransportOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
