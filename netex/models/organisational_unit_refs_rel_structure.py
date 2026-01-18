from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .organisational_unit_ref import OrganisationalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationalUnitRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "organisationalUnitRefs_RelStructure"

    organisational_unit_ref: Iterable[OrganisationalUnitRef] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
