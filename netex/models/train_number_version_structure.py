from dataclasses import dataclass, field
from typing import Optional
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainNumberVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TrainNumber_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_advertisement: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForAdvertisement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_production: Optional[str] = field(
        default=None,
        metadata={
            "name": "ForProduction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
