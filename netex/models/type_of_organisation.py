from dataclasses import dataclass, field

from .type_of_organisation_value_structure import (
    TypeOfOrganisationValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfOrganisation(TypeOfOrganisationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_classified_entity_class: str = field(
        init=False,
        default="Organisation",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        },
    )
