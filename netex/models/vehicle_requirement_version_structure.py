from dataclasses import dataclass, field
from typing import Optional
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.multilingual_string import MultilingualString

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
        }
    )
