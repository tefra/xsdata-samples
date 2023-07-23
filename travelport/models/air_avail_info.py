from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_code_info import BookingCodeInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirAvailInfo:
    """Matches class of service information with availability counts.

    Only provided on search results.

    Parameters
    ----------
    booking_code_info
    fare_token_info
        Associates Fare with HostToken
    provider_code
    host_token_ref
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    booking_code_info: list[BookingCodeInfo] = field(
        default_factory=list,
        metadata={
            "name": "BookingCodeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_token_info: list[AirAvailInfo.FareTokenInfo] = field(
        default_factory=list,
        metadata={
            "name": "FareTokenInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    host_token_ref: None | str = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        }
    )

    @dataclass
    class FareTokenInfo:
        fare_info_ref: None | str = field(
            default=None,
            metadata={
                "name": "FareInfoRef",
                "type": "Attribute",
                "required": True,
            }
        )
        host_token_ref: None | str = field(
            default=None,
            metadata={
                "name": "HostTokenRef",
                "type": "Attribute",
                "required": True,
            }
        )
