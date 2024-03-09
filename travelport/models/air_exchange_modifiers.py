from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.contract_code import ContractCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeModifiers:
    """
    Provides controls and switches for the Exchange process.

    Parameters
    ----------
    contract_codes
    booking_date
    ticketing_date
    account_code
    ticket_designator
    allow_penalty_fares
    private_fares_only
    universal_record_locator_code
        Which UniversalRecord should this new reservation be applied to. If
        blank, then a new one is created.
    provider_locator_code
        Which Provider reservation does this reservation get added to.
    provider_code
        To be used with ProviderLocatorCode, which host the reservation
        being added to belongs to.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    contract_codes: None | AirExchangeModifiers.ContractCodes = field(
        default=None,
        metadata={
            "name": "ContractCodes",
            "type": "Element",
        },
    )
    booking_date: None | str = field(
        default=None,
        metadata={
            "name": "BookingDate",
            "type": "Attribute",
        },
    )
    ticketing_date: None | str = field(
        default=None,
        metadata={
            "name": "TicketingDate",
            "type": "Attribute",
        },
    )
    account_code: None | str = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        },
    )
    ticket_designator: None | str = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        },
    )
    allow_penalty_fares: bool = field(
        default=True,
        metadata={
            "name": "AllowPenaltyFares",
            "type": "Attribute",
        },
    )
    private_fares_only: bool = field(
        default=False,
        metadata={
            "name": "PrivateFaresOnly",
            "type": "Attribute",
        },
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
        },
    )

    @dataclass
    class ContractCodes:
        contract_code: list[ContractCode] = field(
            default_factory=list,
            metadata={
                "name": "ContractCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
