from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.parking_access_status import ParkingAccessStatus
from datexii.models.eu.datexii.v2.parking_conditions_enum import ParkingConditionsEnum
from datexii.models.eu.datexii.v2.parking_fault_enum import ParkingFaultEnum
from datexii.models.eu.datexii.v2.parking_occupancy import ParkingOccupancy
from datexii.models.eu.datexii.v2.parking_record_status_equipment_or_service_facility_index_parking_equipment_or_service_facility_status import ParkingRecordStatusEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacilityStatus
from datexii.models.eu.datexii.v2.parking_record_status_group_index_group_of_parking_spaces_status import ParkingRecordStatusGroupIndexGroupOfParkingSpacesStatus
from datexii.models.eu.datexii.v2.parking_record_status_parking_space_index_parking_space_status import ParkingRecordStatusParkingSpaceIndexParkingSpaceStatus
from datexii.models.eu.datexii.v2.parking_record_status_scenario_index_parking_usage_scenario_status import ParkingRecordStatusScenarioIndexParkingUsageScenarioStatus
from datexii.models.eu.datexii.v2.parking_record_versioned_reference import ParkingRecordVersionedReference
from datexii.models.eu.datexii.v2.parking_route_status import ParkingRouteStatus
from datexii.models.eu.datexii.v2.parking_status_validity import ParkingStatusValidity
from datexii.models.eu.datexii.v2.parking_thresholds import ParkingThresholds
from datexii.models.eu.datexii.v2.winter_equipment_management_type_enum import WinterEquipmentManagementTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingRecordStatus:
    """Contains the current status of one parking record defined in the static
    model (i.e. parking site or group of parking sites) or historical or forecasted
    data for one parking.

    Only for the second case, 'parkingStatusTime' must be specified.

    :ivar parking_record_reference: A reference to a static parking
        record object, i.e. a parking site or a group of parking sites.
    :ivar parking_status_origin_time: The time when the information in
        this message was generated. Unless 'ParkingStatusValidity' is
        used, this is also the time the information in this message
        refers to.
    :ivar parking_status_description: Additional textual information
        about the parking status. Can also be used as an alternative in
        case the enumeration values for 'parkingSiteStatus' or
        'groupOfParkingSitesStatus' do not fit.
    :ivar parking_queueing_time: The current queuing time (duration) for
        entering the parking site.
    :ivar parking_conditions: Defines if normal parking conditions are
        suspended or special parking conditions are in force.
    :ivar blurred_availability: When true, all information about
        availability (free spaces etc.) is blurred (usually because of
        business competition).
    :ivar parking_fault: A fault indicator for the parking site.
    :ivar winter_equipment_management_type: Type of winter equipment
        management action instigated by operator.
    :ivar parking_space_status:
    :ivar parking_occupancy:
    :ivar group_of_parking_spaces_status:
    :ivar parking_status_validity:
    :ivar override_parking_thresholds: Possibility to override the
        thresholds for the parking, which are in principle defined in
        the static part of the model (ParkingStatusPublication).
    :ivar parking_equipment_or_service_facility_status:
    :ivar parking_usage_scenario_status:
    :ivar parking_access_status:
    :ivar parking_route_status:
    :ivar parking_record_status_extension:
    """
    parking_record_reference: Optional[ParkingRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "parkingRecordReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_status_origin_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "parkingStatusOriginTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_status_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingStatusDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_queueing_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "parkingQueueingTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_conditions: Optional[ParkingConditionsEnum] = field(
        default=None,
        metadata={
            "name": "parkingConditions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    blurred_availability: List[bool] = field(
        default_factory=list,
        metadata={
            "name": "blurredAvailability",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_fault: List[ParkingFaultEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    winter_equipment_management_type: List[WinterEquipmentManagementTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "winterEquipmentManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_space_status: List[ParkingRecordStatusParkingSpaceIndexParkingSpaceStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingSpaceStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_occupancy: Optional[ParkingOccupancy] = field(
        default=None,
        metadata={
            "name": "parkingOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    group_of_parking_spaces_status: List[ParkingRecordStatusGroupIndexGroupOfParkingSpacesStatus] = field(
        default_factory=list,
        metadata={
            "name": "groupOfParkingSpacesStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_status_validity: Optional[ParkingStatusValidity] = field(
        default=None,
        metadata={
            "name": "parkingStatusValidity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    override_parking_thresholds: Optional[ParkingThresholds] = field(
        default=None,
        metadata={
            "name": "overrideParkingThresholds",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_equipment_or_service_facility_status: List[ParkingRecordStatusEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacilityStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingEquipmentOrServiceFacilityStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_usage_scenario_status: List[ParkingRecordStatusScenarioIndexParkingUsageScenarioStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingUsageScenarioStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_access_status: List[ParkingAccessStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingAccessStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_route_status: List[ParkingRouteStatus] = field(
        default_factory=list,
        metadata={
            "name": "parkingRouteStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_record_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingRecordStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
