from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .local_service_version_structure import LocalServiceVersionStructure
from .payment_method_enumeration import PaymentMethodEnumeration
from .ticket_type_enumeration import TicketTypeEnumeration
from .ticketing_service_facility_enumeration import (
    TicketingServiceFacilityEnumeration,
)
from .vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "TicketingService_VersionStructure"

    vehicle_modes: Sequence[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    ticketing_service_list: Sequence[TicketingServiceFacilityEnumeration] = (
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
    ticket_type_list: Sequence[Sequence[TicketTypeEnumeration]] = field(
        default_factory=list,
        metadata={
            "name": "TicketTypeList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    ticket_counter_service: None | bool = field(
        default=None,
        metadata={
            "name": "TicketCounterService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    online_purchase_for_collection: None | bool = field(
        default=None,
        metadata={
            "name": "OnlinePurchaseForCollection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    online_purchase_for_eticket: None | bool = field(
        default=None,
        metadata={
            "name": "OnlinePurchaseForETicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    online_purchase_for_self_print_ticket: None | bool = field(
        default=None,
        metadata={
            "name": "OnlinePurchaseForSelfPrintTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mobile_device_tickets: None | bool = field(
        default=None,
        metadata={
            "name": "MobileDeviceTickets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_methods: Sequence[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
