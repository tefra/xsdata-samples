from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from decimal import Decimal

from .all_modes_enumeration import AllModesEnumeration
from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)
from .payment_method_enumeration import PaymentMethodEnumeration
from .queue_management_enumeration import QueueManagementEnumeration
from .scope_of_ticket_enumeration import ScopeOfTicketEnumeration
from .ticket_type_enumeration import TicketTypeEnumeration
from .ticketing_facility_list import TicketingFacilityList
from .ticketing_service_facility_list import TicketingServiceFacilityList

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    class Meta:
        name = "TicketingEquipment_VersionStructure"

    vehicle_modes: Sequence[AllModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    ticket_machines: None | bool = field(
        default=None,
        metadata={
            "name": "TicketMachines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_machines: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfMachines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_of_machine_interface: None | Decimal = field(
        default=None,
        metadata={
            "name": "HeightOfMachineInterface",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_facility_list: None | TicketingFacilityList = field(
        default=None,
        metadata={
            "name": "TicketingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_service_facility_list: None | TicketingServiceFacilityList = (
        field(
            default=None,
            metadata={
                "name": "TicketingServiceFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    ticket_office: None | bool = field(
        default=None,
        metadata={
            "name": "TicketOffice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticket_counter: None | bool = field(
        default=None,
        metadata={
            "name": "TicketCounter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_tills: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfTills",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    queue_management: None | QueueManagementEnumeration = field(
        default=None,
        metadata={
            "name": "QueueManagement",
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
    ticket_types_available: Sequence[TicketTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketTypesAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    scope_of_tickets_available: Sequence[ScopeOfTicketEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ScopeOfTicketsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    low_counter_access: None | bool = field(
        default=None,
        metadata={
            "name": "LowCounterAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_of_low_counter: None | Decimal = field(
        default=None,
        metadata={
            "name": "HeightOfLowCounter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    induction_loops: None | bool = field(
        default=None,
        metadata={
            "name": "InductionLoops",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_interface_available: None | bool = field(
        default=None,
        metadata={
            "name": "TactileInterfaceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_interface_available: None | bool = field(
        default=None,
        metadata={
            "name": "AudioInterfaceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    disabled_priority: None | bool = field(
        default=None,
        metadata={
            "name": "DisabledPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_suitable: None | bool = field(
        default=None,
        metadata={
            "name": "WheelchairSuitable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
