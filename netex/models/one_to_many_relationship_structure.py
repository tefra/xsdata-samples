from dataclasses import dataclass, field
from netex.models.modification_set_enumeration import ModificationSetEnumeration
from netex.models.relationship_structure import RelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OneToManyRelationshipStructure(RelationshipStructure):
    class Meta:
        name = "oneToManyRelationshipStructure"

    modification_set: ModificationSetEnumeration = field(
        default=ModificationSetEnumeration.ALL,
        metadata={
            "name": "modificationSet",
            "type": "Attribute",
        }
    )
