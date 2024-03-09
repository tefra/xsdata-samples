from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

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


@dataclass
class TicketingEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    class Meta:
        name = "TicketingEquipment_VersionStructure"

    vehicle_modes: List[AllModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    ticket_machines: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketMachines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_machines: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfMachines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_of_machine_interface: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightOfMachineInterface",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_facility_list: Optional[TicketingFacilityList] = field(
        default=None,
        metadata={
            "name": "TicketingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_service_facility_list: Optional[TicketingServiceFacilityList] = (
        field(
            default=None,
            metadata={
                "name": "TicketingServiceFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    ticket_office: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketOffice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticket_counter: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketCounter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_tills: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfTills",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    queue_management: Optional[QueueManagementEnumeration] = field(
        default=None,
        metadata={
            "name": "QueueManagement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    ticket_types_available: List[TicketTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketTypesAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    scope_of_tickets_available: List[ScopeOfTicketEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ScopeOfTicketsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    low_counter_access: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowCounterAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_of_low_counter: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightOfLowCounter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    induction_loops: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InductionLoops",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_interface_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileInterfaceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_interface_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioInterfaceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    disabled_priority: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisabledPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_suitable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairSuitable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
