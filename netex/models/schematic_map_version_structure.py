from dataclasses import dataclass, field
from typing import Optional
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .schematic_map_members_rel_structure import (
    SchematicMapMembersRelStructure,
)
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SchematicMapVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "SchematicMap_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    image_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImageUri",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    depicted_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DepictedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[SchematicMapMembersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
