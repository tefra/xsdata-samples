from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.models.installed_equipment_version_structure import InstalledEquipmentVersionStructure
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.queue_management_enumeration import QueueManagementEnumeration
from netex.models.ticket_type_enumeration import TicketTypeEnumeration
from netex.models.ticketing_facility_enumeration import TicketingFacilityEnumeration
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TicketingEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    class Meta:
        name = "TicketingEquipment_VersionStructure"

    vehicle_modes: List[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticket_machines: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketMachines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_machines: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfMachines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height_of_machine_interface: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightOfMachineInterface",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_facility_list: List[TicketingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticketing_service_facility_list: List[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticket_office: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketOffice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticket_counter: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TicketCounter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_tills: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfTills",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    queue_management: Optional[QueueManagementEnumeration] = field(
        default=None,
        metadata={
            "name": "QueueManagement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticket_types_available: List[TicketTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketTypesAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    scope_of_tickets_available: List[TicketingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ScopeOfTicketsAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    low_counter_access: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowCounterAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height_of_low_counter: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightOfLowCounter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    induction_loops: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InductionLoops",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_interface_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileInterfaceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audio_interface_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioInterfaceAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    disabled_priority: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisabledPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_suitable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairSuitable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
