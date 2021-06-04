from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.type_of_organisation_ref import TypeOfOrganisationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfOrganisationRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfOrganisationRefs_RelStructure"

    type_of_organisation_ref: List[TypeOfOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
