from dataclasses import dataclass, field
from typing import Optional
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleRequirementVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehicleRequirement_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
