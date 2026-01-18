from dataclasses import dataclass, field

from .booking_arrangements_structure import BookingArrangementsStructure
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CancellingVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Cancelling_VersionStructure"

    booking_arrangements: BookingArrangementsStructure | None = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cancellation_allowed: bool | None = field(
        default=None,
        metadata={
            "name": "CancellationAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_deposit_refundable: bool | None = field(
        default=None,
        metadata={
            "name": "BookingDepositRefundable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
