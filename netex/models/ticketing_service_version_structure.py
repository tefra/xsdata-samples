from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .local_service_version_structure import LocalServiceVersionStructure
from .payment_method_enumeration import PaymentMethodEnumeration
from .ticket_type_enumeration import TicketTypeEnumeration
from .ticketing_service_facility_enumeration import (
    TicketingServiceFacilityEnumeration,
)
from .vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TicketingServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "TicketingService_VersionStructure"

    vehicle_modes: Iterable[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    ticketing_service_list: Iterable[TicketingServiceFacilityEnumeration] = (
        field(
            default_factory=list,
            metadata={
                "name": "TicketingServiceList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "tokens": True,
            },
        )
    )
    ticket_type_list: Iterable[Iterable[TicketTypeEnumeration]] = field(
        default_factory=list,
        metadata={
            "name": "TicketTypeList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    ticket_counter_service: bool | None = field(
        default=None,
        metadata={
            "name": "TicketCounterService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    online_purchase_for_collection: bool | None = field(
        default=None,
        metadata={
            "name": "OnlinePurchaseForCollection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    online_purchase_for_eticket: bool | None = field(
        default=None,
        metadata={
            "name": "OnlinePurchaseForETicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    online_purchase_for_self_print_ticket: bool | None = field(
        default=None,
        metadata={
            "name": "OnlinePurchaseForSelfPrintTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mobile_device_tickets: bool | None = field(
        default=None,
        metadata={
            "name": "MobileDeviceTickets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_methods: Iterable[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
