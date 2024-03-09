from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .booking_arrangements_structure import BookingArrangementsStructure
from .booking_charge_type_enumeration import BookingChargeTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceBookingArrangementsStructure(BookingArrangementsStructure):
    minimum_booking_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumBookingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_booking_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumBookingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deposit_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DepositRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_charge_type: Optional[BookingChargeTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "BookingChargeType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
