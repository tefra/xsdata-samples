from dataclasses import dataclass, field
from .type_of_link_sequence_value_structure import TypeOfLinkSequenceValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfLinkSequence(TypeOfLinkSequenceValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_of_classified_entity_class: str = field(
        init=False,
        default="LinkSequence",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        }
    )
