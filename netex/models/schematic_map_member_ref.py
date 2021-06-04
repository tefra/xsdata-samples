from dataclasses import dataclass
from netex.models.schematic_map_member_ref_structure import SchematicMapMemberRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SchematicMapMemberRef(SchematicMapMemberRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
