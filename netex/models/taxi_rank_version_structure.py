from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from .stop_place_version_structure import StopPlaceVersionStructure
from .taxi_stands_rel_structure import TaxiStandsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiRankVersionStructure(StopPlaceVersionStructure):
    class Meta:
        name = "TaxiRank_VersionStructure"

    maximum_standing_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumStandingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    taxi_stands: Optional[TaxiStandsRelStructure] = field(
        default=None,
        metadata={
            "name": "taxiStands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
