from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .booking_arrangements_structure import BookingArrangementsStructure
from .booking_charge_type_enumeration import BookingChargeTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceBookingArrangementsStructure(BookingArrangementsStructure):
    minimum_booking_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MinimumBookingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_booking_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MaximumBookingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deposit_required: bool | None = field(
        default=None,
        metadata={
            "name": "DepositRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_charge_type: BookingChargeTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "BookingChargeType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
