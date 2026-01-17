from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.area import Area
from datexii.models.eu.datexii.v2.contact import Contact
from datexii.models.eu.datexii.v2.dimension import Dimension
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations
from datexii.models.eu.datexii.v2.group_of_parking_spaces_2 import (
    GroupOfParkingSpaces2,
)
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.occupancy_detection_type_enum import (
    OccupancyDetectionTypeEnum,
)
from datexii.models.eu.datexii.v2.parking_assignment import ParkingAssignment
from datexii.models.eu.datexii.v2.parking_record_equipment_or_service_facility_index_parking_equipment_or_service_facility import (
    ParkingRecordEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility,
)
from datexii.models.eu.datexii.v2.parking_route import ParkingRoute
from datexii.models.eu.datexii.v2.parking_space_2 import ParkingSpace2
from datexii.models.eu.datexii.v2.parking_thresholds import ParkingThresholds
from datexii.models.eu.datexii.v2.parking_vms import ParkingVMS
from datexii.models.eu.datexii.v2.permits_and_prohibitions import (
    PermitsAndProhibitions,
)
from datexii.models.eu.datexii.v2.rgbcolour import RGBColour
from datexii.models.eu.datexii.v2.tariffs_and_payment import TariffsAndPayment

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingRecord:
    """
    A container for static parking information.

    Must be specialised as a parking site or as a group of parking sites.

    :ivar parking_name: Name of the parking, i.e. name of the parking
        site or the group of parking sites.
    :ivar parking_alias: Alternative name for the parking site or the
        group of parking sites.
    :ivar parking_description: Additional description of the parking
        site or the group of parking sites.
    :ivar parking_record_version_time: Date/time that this version of
        the parking record was defined.
    :ivar parking_number_of_spaces: Number of parking spaces (attribute
        is used for a parking record as well as for a group of parking
        spaces).
    :ivar parking_principal_number_of_spaces: Number of parking spaces
        that are not assigned for a particular purpose.
    :ivar maximum_parking_duration: The maximum parking duration for a
        parking record, a parking space or a group of parking spaces
        (e.g. to avoid overnight parking).
    :ivar photo_url: Specifies a URL at which a photo of the object in
        concern can be found.
    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar parking_occupany_detection_type: Type of parking occupancy
        detection for a parking record, a parking space or a group of
        parking spaces, if any (balancing, single slot, ...  ).
    :ivar emergency_contact: Contact to be used in times of emergencies.
    :ivar owner: Contact details of the owner of the parking facility.
    :ivar responisble_authority: Contact details of the responsible
        authority of the parking facility or parking area.
    :ivar security_service: Contact details of one or more security
        services of the parking facility.
    :ivar operator: Contact details of the operator of the parking
        facility.
    :ivar service_partner: Contact details of a service partner of the
        parking record, i.e. the person or organisation that should be
        contacted to provide servicing or support services for equipment
        at the parking.
    :ivar parking_vms:
    :ivar parking_location: The location(s) or the extent of the
        parking. Examples could be an Area for parking area, a Point
        location for an urban parking facility or a Linear for on street
        parking.
    :ivar parking_route:
    :ivar parking_colour: A colour, which can be assigned to the
        parking. Often used with parking areas for a quick visual
        distinction.
    :ivar only_assigned_parking: Parking is only allowed for the
        assignment given in this class, i.e. other assignments are not
        allowed. By using this role, it is not allowed to use
        'assignedParkingAmongOthers' and 'prohibitedParking' for the
        same type of attributes.
    :ivar assigned_parking_among_others: Assignments for parking. Other
        assignments are allowed as well, i.e. the parking spaces are
        convenient for this kind of assignment.
    :ivar prohibited_parking: Parking is not allowed for the given
        assignment.
    :ivar tariffs_and_payment:
    :ivar parking_equipment_or_service_facility:
    :ivar parking_space: Properties of a single parking space. This
        aggregation may only be used with the "ParkingSpace"
        specialisation.
    :ivar group_of_parking_spaces: Properties for a group of parking
        spaces. Usually, all properties specified have to be the same
        for all spaces included. This aggregation may only be used with
        the "GroupOfParkingSpaces" specialisation.
    :ivar parking_thresholds:
    :ivar permits_and_prohibitions:
    :ivar emergency_assembly_point: Some geographic location(s) within
        or nearby the parking, where people have to meet in case of a
        fire, for example.
    :ivar entire_area: An underlaying area this parking record is
        located in or belongs to. Examples are a state, province, truck
        parking area etc. A name can be specified in the area structure.
    :ivar parking_record_dimension: Dimension either of the building or
        a virtual rectangle encapsulating the parking site(s). Use
        'dimensionUsableArea' to define the total space available for
        parking. Use 'dimensionHeight' only for a building, not for the
        restriction of vehicles.
    :ivar parking_record_extension:
    :ivar id:
    :ivar version:
    """

    parking_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_alias: list[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "parkingAlias",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "parkingRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_number_of_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingNumberOfSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_principal_number_of_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkingPrincipalNumberOfSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    maximum_parking_duration: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumParkingDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    photo_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "photoUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    url_link_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_occupany_detection_type: list[OccupancyDetectionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingOccupanyDetectionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    emergency_contact: list[Contact] = field(
        default_factory=list,
        metadata={
            "name": "emergencyContact",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    owner: list[Contact] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    responisble_authority: list[Contact] = field(
        default_factory=list,
        metadata={
            "name": "responisbleAuthority",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    security_service: list[Contact] = field(
        default_factory=list,
        metadata={
            "name": "securityService",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    operator: list[Contact] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    service_partner: list[Contact] = field(
        default_factory=list,
        metadata={
            "name": "servicePartner",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_vms: list[ParkingVMS] = field(
        default_factory=list,
        metadata={
            "name": "parkingVMS",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_location: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "parkingLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_route: list[ParkingRoute] = field(
        default_factory=list,
        metadata={
            "name": "parkingRoute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_colour: Optional[RGBColour] = field(
        default=None,
        metadata={
            "name": "parkingColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    only_assigned_parking: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "onlyAssignedParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    assigned_parking_among_others: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "assignedParkingAmongOthers",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    prohibited_parking: Optional[ParkingAssignment] = field(
        default=None,
        metadata={
            "name": "prohibitedParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    tariffs_and_payment: Optional[TariffsAndPayment] = field(
        default=None,
        metadata={
            "name": "tariffsAndPayment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_equipment_or_service_facility: list[
        ParkingRecordEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility
    ] = field(
        default_factory=list,
        metadata={
            "name": "parkingEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_space: list[ParkingSpace2] = field(
        default_factory=list,
        metadata={
            "name": "parkingSpace",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_parking_spaces: list[GroupOfParkingSpaces2] = field(
        default_factory=list,
        metadata={
            "name": "groupOfParkingSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_thresholds: Optional[ParkingThresholds] = field(
        default=None,
        metadata={
            "name": "parkingThresholds",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    permits_and_prohibitions: list[PermitsAndProhibitions] = field(
        default_factory=list,
        metadata={
            "name": "permitsAndProhibitions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    emergency_assembly_point: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "emergencyAssemblyPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    entire_area: Optional[Area] = field(
        default=None,
        metadata={
            "name": "entireArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_record_dimension: Optional[Dimension] = field(
        default=None,
        metadata={
            "name": "parkingRecordDimension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
