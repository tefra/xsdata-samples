from dataclasses import dataclass, field
from typing import List
from .country_ref import CountryRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CountryRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "countryRefs_RelStructure"

    country_ref: List[CountryRef] = field(
        default_factory=list,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
