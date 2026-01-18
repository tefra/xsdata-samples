from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.opening_status_enum import OpeningStatusEnum
from datexii.models.eu.datexii.v2.operation_status_enum import (
    OperationStatusEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingEquipmentOrServiceFacilityStatus:
    """
    The number of E&amp;S can be overridden here (for example during
    restoration).

    Furthermore, the current availability of E&amp;S can be given (for
    example number of free electric charging stations). The E&amp;S are
    identified from the static model by an index.

    :ivar number_of_equipment_or_service_facility_override: Overrides
        the static value 'numberOfEquipmentOrServiceFacility' (for
        example because of long- or midterm closures, such as
        renovation).
    :ivar number_of_subitems_override: Overrides the static value
        'numberOfSubitems' (for example because of long- or midterm
        closures, such as renovation).
    :ivar vacant_equipment_or_service_facility_subitems: Sets the number
        of currently vacant elements of either equipment (e.g. free
        toilets) or service facility sub items (e.g. free restaurant
        places).
    :ivar service_facility_opening_status: Specifies whether this
        service facility is open or not.
    :ivar equipment_operation_status: Specifies whether this equipment
        is available / is in operation or not.
    :ivar parking_equipment_or_service_facility_status_extension:
    """

    number_of_equipment_or_service_facility_override: None | int = field(
        default=None,
        metadata={
            "name": "numberOfEquipmentOrServiceFacilityOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    number_of_subitems_override: None | int = field(
        default=None,
        metadata={
            "name": "numberOfSubitemsOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vacant_equipment_or_service_facility_subitems: None | int = field(
        default=None,
        metadata={
            "name": "vacantEquipmentOrServiceFacilitySubitems",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    service_facility_opening_status: None | OpeningStatusEnum = field(
        default=None,
        metadata={
            "name": "serviceFacilityOpeningStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    equipment_operation_status: None | OperationStatusEnum = field(
        default=None,
        metadata={
            "name": "equipmentOperationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_equipment_or_service_facility_status_extension: (
        None | ExtensionType
    ) = field(
        default=None,
        metadata={
            "name": "parkingEquipmentOrServiceFacilityStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
