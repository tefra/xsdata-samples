from dataclasses import dataclass

from .schematic_map_ref_structure import SchematicMapRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SchematicMapRef(SchematicMapRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
