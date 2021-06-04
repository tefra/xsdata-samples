from dataclasses import dataclass
from netex.models.relationship_ref_structure import RelationshipRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RelationshipRef(RelationshipRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
