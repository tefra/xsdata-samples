from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainNumberVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TrainNumber_VersionStructure"

    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_advertisement: None | str = field(
        default=None,
        metadata={
            "name": "ForAdvertisement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_production: None | str = field(
        default=None,
        metadata={
            "name": "ForProduction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
