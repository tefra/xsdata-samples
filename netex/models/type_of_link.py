from dataclasses import dataclass, field
from .type_of_link_value_structure import TypeOfLinkValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfLink(TypeOfLinkValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_classified_entity_class: str = field(
        init=False,
        default="Link",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        }
    )
