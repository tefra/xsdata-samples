from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.price_request_information_type import (
    PriceRequestInformationType,
)
from sabre.models.traveler_info_summary_tpa_extensions_type import (
    TravelerInfoSummaryTpaExtensionsType,
)
from sabre.models.traveler_information_type import TravelerInformationType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class TravelerInfoSummaryType:
    """
    Specifies passenger numbers and types.

    Attributes:
        seats_requested: The sum of all seats required by all passenger
            groups.
        air_traveler_avail: Specifies passenger numbers and types.
        price_request_information: Identify pricing source, if
            negotiated fares are requested and if it is a reprice
            request.
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        specific_ptc_indicator: If true, this request is for a specific
            PTC and only fares applicable to that PTC will be checked
            and returned. It is the same as XOFares flag in Intellisell
            request.
    """

    seats_requested: list[int] = field(
        default_factory=list,
        metadata={
            "name": "SeatsRequested",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 4,
        },
    )
    air_traveler_avail: list[TravelerInformationType] = field(
        default_factory=list,
        metadata={
            "name": "AirTravelerAvail",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 4,
        },
    )
    price_request_information: None | PriceRequestInformationType = field(
        default=None,
        metadata={
            "name": "PriceRequestInformation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    tpa_extensions: None | TravelerInfoSummaryTpaExtensionsType = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    specific_ptc_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "SpecificPTC_Indicator",
            "type": "Attribute",
        },
    )
