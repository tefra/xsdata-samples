from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .booking_arrangements_structure import BookingArrangementsStructure
from .booking_policy_version_structure import BookingPolicyVersionStructure
from .per_basis_enumeration import PerBasisEnumeration
from .reservation_charge_type_enumeration import (
    ReservationChargeTypeEnumeration,
)
from .reservation_enumeration import ReservationEnumeration
from .seat_allocation_method_enumeration import SeatAllocationMethodEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReservingVersionStructure(BookingPolicyVersionStructure):
    class Meta:
        name = "Reserving_VersionStructure"

    reserving_requirements: Iterable[ReservationEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ReservingRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    minimum_number_to_reserve: None | int = field(
        default=None,
        metadata={
            "name": "MinimumNumberToReserve",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_to_reserve: None | int = field(
        default=None,
        metadata={
            "name": "MaximumNumberToReserve",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    must_reserve_whole_compartment: None | bool = field(
        default=None,
        metadata={
            "name": "MustReserveWholeCompartment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reservation_charge_type: None | ReservationChargeTypeEnumeration = field(
        default=None,
        metadata={
            "name": "ReservationChargeType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fee_basis: None | PerBasisEnumeration = field(
        default=None,
        metadata={
            "name": "FeeBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_free_connecting_reservations: None | bool = field(
        default=None,
        metadata={
            "name": "HasFreeConnectingReservations",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_free_connecting_reservations: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfFreeConnectingReservations",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_fee_refundable: None | bool = field(
        default=None,
        metadata={
            "name": "IsFeeRefundable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_arrangements: None | BookingArrangementsStructure = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    seat_allocation_method: None | SeatAllocationMethodEnumeration = field(
        default=None,
        metadata={
            "name": "SeatAllocationMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reservation_expiry_period: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "ReservationExpiryPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
