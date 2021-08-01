from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.individual_charge import IndividualCharge
from datexii.models.eu.datexii.v2.overall_period import OverallPeriod
from datexii.models.eu.datexii.v2.parking_permit import ParkingPermit
from datexii.models.eu.datexii.v2.parking_record_versioned_reference import ParkingRecordVersionedReference
from datexii.models.eu.datexii.v2.vehicle import Vehicle

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingVehicle:
    """
    Information about one individual parking vehicle.

    :ivar parking_record_reference: A reference to a static parking
        record object, i.e. a parking site or a group of parking sites.
    :ivar parking_space_reference: Points to the parking space, on which
        the vehicle is located. The reference is only unique in
        combination with 'parkingRecordReference'.
    :ivar group_of_parking_spaces_reference: Points to one or more
        groups of parking spaces, to which the parking space of the
        vehicle belongs. The reference is only unique in combination
        with 'parkingRecordReference'.
    :ivar parking_permit:
    :ivar vehicle:
    :ivar individual_charge:
    :ivar parking_period:
    :ivar parking_vehicle_extension:
    :ivar id:
    :ivar version:
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
    parking_space_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "parkingSpaceReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    group_of_parking_spaces_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "groupOfParkingSpacesReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    parking_permit: List[ParkingPermit] = field(
        default_factory=list,
        metadata={
            "name": "parkingPermit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vehicle: Optional[Vehicle] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    individual_charge: Optional[IndividualCharge] = field(
        default=None,
        metadata={
            "name": "individualCharge",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_period: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "parkingPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_vehicle_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingVehicleExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
