from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.arunk_type import ArunkType
from sabre.models.exchange_air_search_prefs_type import (
    ExchangeAirSearchPrefsType,
)
from sabre.models.exchange_fare_type import ExchangeFareType
from sabre.models.exchange_origin_destination_information_type import (
    ExchangeOriginDestinationInformationType,
)
from sabre.models.exchange_postype import ExchangePostype
from sabre.models.exchange_tpa_extensions_type import ExchangeTpaExtensionsType
from sabre.models.traveler_info_summary_type import TravelerInfoSummaryType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class ExchangeType:
    """
    Attributes:
        fare:
        pos:
        origin_destination_information:
        arunk:
        travel_preferences:
        traveler_info_summary:
        tpa_extensions:
        original_tkt_issue_date_time: Original ticket issue date and
            time
        exchanged_tkt_issue_date_time: Exchanged ticket issue date and
            time
        previous_exchange_date_time: Previous exchange date and time
        number_of_tax_boxes: Number of tax boxes
        bypass_advance_purchase_option: Bypass Advance Purchase Option
    """

    fare: ExchangeFareType = field(
        metadata={
            "name": "Fare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    pos: ExchangePostype = field(
        metadata={
            "name": "POS",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    origin_destination_information: list[
        ExchangeOriginDestinationInformationType
    ] = field(
        default_factory=list,
        metadata={
            "name": "OriginDestinationInformation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )
    arunk: list[ArunkType] = field(
        default_factory=list,
        metadata={
            "name": "Arunk",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    travel_preferences: None | ExchangeAirSearchPrefsType = field(
        default=None,
        metadata={
            "name": "TravelPreferences",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    traveler_info_summary: TravelerInfoSummaryType = field(
        metadata={
            "name": "TravelerInfoSummary",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    tpa_extensions: None | ExchangeTpaExtensionsType = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    original_tkt_issue_date_time: str = field(
        metadata={
            "name": "OriginalTktIssueDateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}(T[0-9]{2}:[0-9]{2}:[0-9]{2})?",
        }
    )
    exchanged_tkt_issue_date_time: None | str = field(
        default=None,
        metadata={
            "name": "ExchangedTktIssueDateTime",
            "type": "Attribute",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}(T[0-9]{2}:[0-9]{2}:[0-9]{2})?",
        },
    )
    previous_exchange_date_time: None | str = field(
        default=None,
        metadata={
            "name": "PreviousExchangeDateTime",
            "type": "Attribute",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}(T[0-9]{2}:[0-9]{2}:[0-9]{2})?",
        },
    )
    number_of_tax_boxes: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfTaxBoxes",
            "type": "Attribute",
        },
    )
    bypass_advance_purchase_option: None | str = field(
        default=None,
        metadata={
            "name": "BypassAdvancePurchaseOption",
            "type": "Attribute",
            "length": 1,
        },
    )
