from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.equipment_or_system_fault_type_enum import (
    EquipmentOrSystemFaultTypeEnum,
)
from datexii.models.eu.datexii.v2.equipment_or_system_type_enum import (
    EquipmentOrSystemTypeEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.traffic_element import TrafficElement

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class EquipmentOrSystemFault(TrafficElement):
    """
    Equipment or system which is faulty, malfunctioning or not in a fully
    operational state that may be of interest or concern to road operators
    and road users.

    :ivar equipment_or_system_fault_type: Failure, malfunction or non
        operational condition of equipment or system.
    :ivar faulty_equipment_or_system_type: The type of equipment or
        system which is faulty, malfunctioning or not in a fully
        operational state.
    :ivar equipment_or_system_fault_extension:
    """

    equipment_or_system_fault_type: EquipmentOrSystemFaultTypeEnum = field(
        metadata={
            "name": "equipmentOrSystemFaultType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    faulty_equipment_or_system_type: EquipmentOrSystemTypeEnum = field(
        metadata={
            "name": "faultyEquipmentOrSystemType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    equipment_or_system_fault_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "equipmentOrSystemFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
