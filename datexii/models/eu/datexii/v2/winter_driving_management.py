from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.network_management import NetworkManagement
from datexii.models.eu.datexii.v2.winter_equipment_management_type_enum import WinterEquipmentManagementTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class WinterDrivingManagement(NetworkManagement):
    """
    Winter driving management action that is instigated by the network/road
    operator.

    :ivar winter_equipment_management_type: Type of winter equipment
        management action instigated by operator.
    :ivar winter_driving_management_extension:
    """
    winter_equipment_management_type: Optional[WinterEquipmentManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "winterEquipmentManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    winter_driving_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "winterDrivingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
