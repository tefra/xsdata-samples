from dataclasses import dataclass

from .schematic_map_version_structure import SchematicMapVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SchematicMap(SchematicMapVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
