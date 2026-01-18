from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainNumberVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TrainNumber_VersionStructure"

    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_advertisement: str | None = field(
        default=None,
        metadata={
            "name": "ForAdvertisement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_production: str | None = field(
        default=None,
        metadata={
            "name": "ForProduction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
