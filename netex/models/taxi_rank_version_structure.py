from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .stop_place_version_structure import StopPlaceVersionStructure
from .taxi_stands_rel_structure import TaxiStandsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiRankVersionStructure(StopPlaceVersionStructure):
    class Meta:
        name = "TaxiRank_VersionStructure"

    maximum_standing_duration: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MaximumStandingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    taxi_stands: None | TaxiStandsRelStructure = field(
        default=None,
        metadata={
            "name": "taxiStands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
