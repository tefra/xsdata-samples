from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_source_type_4 import BookingSourceType4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class BookingSource4:
    """
    Parameters
    ----------
    code
        Alternate booking source code or number.
    type_value
        Type of booking source sent in the Code attribute. Possible values
        are “PseudoCityCode”,” ArcNumber”,” IataNumber”, “CustomerId” and
        “BookingSourceOverrride”. “BookingSourceOverrride” is only
        applicable in VehicleCreateReservationReq. 1P/1J.
    """

    class Meta:
        name = "BookingSource"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        },
    )
    type_value: None | BookingSourceType4 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
