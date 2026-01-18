from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.fault import Fault
from datexii.models.eu.datexii.v2.measurement_equipment_fault_enum import (
    MeasurementEquipmentFaultEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MeasurementEquipmentFault(Fault):
    """
    Details of a fault which is being reported for the related measurement
    equipment.

    :ivar measurement_equipment_fault: The type of fault which is being
        reported for the specified measurement equipment.
    :ivar measurement_equipment_fault_extension:
    """

    measurement_equipment_fault: MeasurementEquipmentFaultEnum | None = field(
        default=None,
        metadata={
            "name": "measurementEquipmentFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    measurement_equipment_fault_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "measurementEquipmentFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
