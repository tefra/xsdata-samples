from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agency_info_1 import AgencyInfo1
from travelport.models.name_1 import Name1
from travelport.models.type_product_info import TypeProductInfo
from travelport.models.type_reservation_ticketed import TypeReservationTicketed

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class ProviderReservationSearchResult:
    """
    Container for reservations that match the search criteria.

    Parameters
    ----------
    name
    product_info
    agency_info
    universal_record_locator_code
    created_date
        The date the resevation record was created
    earliest_travel_date
        The date on which th earliest travel can occur
    ticketed
        If the reservation is ticketed. Applies to an AIR reservation only
    provider_code
    provider_locator_code
    external_search_index
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    name: list[Name1] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    product_info: list[TypeProductInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProductInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    agency_info: None | AgencyInfo1 = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
        }
    )
    created_date: None | str = field(
        default=None,
        metadata={
            "name": "CreatedDate",
            "type": "Attribute",
        }
    )
    earliest_travel_date: None | str = field(
        default=None,
        metadata={
            "name": "EarliestTravelDate",
            "type": "Attribute",
        }
    )
    ticketed: None | TypeReservationTicketed = field(
        default=None,
        metadata={
            "name": "Ticketed",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
        }
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
        }
    )
    external_search_index: None | str = field(
        default=None,
        metadata={
            "name": "ExternalSearchIndex",
            "type": "Attribute",
        }
    )
