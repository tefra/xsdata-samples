from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_base_req import BookingBaseReq

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingDisplayReq(BookingBaseReq):
    """
    Retrieves the current contents of data in session , or PNR if it is specified.

    Parameters
    ----------
    provider_reservation_info
        Bring an existent PNR in session to work on it.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    provider_reservation_info: None | BookingDisplayReq.ProviderReservationInfo = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
        }
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
            }
        )
        provider_locator_code: None | str = field(
            default=None,
            metadata={
                "name": "ProviderLocatorCode",
                "type": "Attribute",
                "required": True,
                "max_length": 15,
            }
        )
        supplier_code: None | str = field(
            default=None,
            metadata={
                "name": "SupplierCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 5,
            }
        )
