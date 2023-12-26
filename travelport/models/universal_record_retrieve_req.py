from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordRetrieveReq(BaseReq1):
    """
    Request to retrieve a summary information for reservations under a Universal
    Record.

    Parameters
    ----------
    universal_record_locator_code
        Represents a valid Universal Recordlocator code
    provider_reservation_info
        Represents a valid Provider Reservation/PNR.
    view_only_ind
        True-Retrieves the PNR in UR Format, but doesn't create an actual UR
        in UAPI. False-Creates and Retrieves an actual UR. Default false.
    traveler_last_name
        Match Traveler Last Name.
    traveler_first_name
        Represents Traveler First Name for ACH PNR Retrieve.
    return_unmasked_data
        When set as True in the request and AAT settings are set to display
        Unmasked details in the host, then details will be shown in the
        response. Only supports credit card and debit card. Default value of
        ReturnUnmaskedData is false.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        },
    )
    provider_reservation_info: None | UniversalRecordRetrieveReq.ProviderReservationInfo = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
        },
    )
    view_only_ind: bool = field(
        default=False,
        metadata={
            "name": "ViewOnlyInd",
            "type": "Attribute",
        },
    )
    traveler_last_name: None | str = field(
        default=None,
        metadata={
            "name": "TravelerLastName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        },
    )
    traveler_first_name: None | str = field(
        default=None,
        metadata={
            "name": "TravelerFirstName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        },
    )
    return_unmasked_data: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnUnmaskedData",
            "type": "Attribute",
        },
    )

    @dataclass
    class ProviderReservationInfo:
        """
        Parameters
        ----------
        provider_code
        provider_locator_code
        supplier_code
            Represents Carrier Code for ACH PNR Retrieve.
        """

        provider_code: None | str = field(
            default=None,
            metadata={
                "name": "ProviderCode",
                "type": "Attribute",
                "required": True,
                "min_length": 2,
                "max_length": 5,
            },
        )
        provider_locator_code: None | str = field(
            default=None,
            metadata={
                "name": "ProviderLocatorCode",
                "type": "Attribute",
                "required": True,
                "max_length": 15,
            },
        )
        supplier_code: None | str = field(
            default=None,
            metadata={
                "name": "SupplierCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 5,
            },
        )
