from dataclasses import dataclass, field
from typing import Optional, Union

from .assistance_availability_enumeration import (
    AssistanceAvailabilityEnumeration,
)
from .authority_ref import AuthorityRef
from .booking_arrangements_structure import BookingArrangementsStructure
from .contact_structure import ContactStructure
from .flexible_line_ref import FlexibleLineRef
from .flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from .line_ref import LineRef
from .local_service_version_structure import LocalServiceVersionStructure
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .operator_ref import OperatorRef
from .personal_mode_of_operation_ref import PersonalModeOfOperationRef
from .scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from .vehicle_mode import VehicleMode
from .vehicle_pooling_ref import VehiclePoolingRef
from .vehicle_rental_ref import VehicleRentalRef
from .vehicle_sharing_ref import VehicleSharingRef
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AssistanceBookingServiceVersionStructure(LocalServiceVersionStructure):
    class Meta:
        name = "AssistanceBookingService_VersionStructure"

    assistance_availability: Optional[AssistanceAvailabilityEnumeration] = (
        field(
            default=None,
            metadata={
                "name": "AssistanceAvailability",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    wheelchair_booking_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairBookingRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_contact: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "BookingContact",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_arrangements: Optional[BookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_mode: Optional[VehicleMode] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref: Optional[
        Union[
            PersonalModeOfOperationRef,
            VehiclePoolingRef,
            VehicleSharingRef,
            VehicleRentalRef,
            FlexibleModeOfOperationRef,
            ScheduledModeOfOperationRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperationRef",
                    "type": PersonalModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingRef",
                    "type": VehiclePoolingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingRef",
                    "type": VehicleSharingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalRef",
                    "type": VehicleRentalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleModeOfOperationRef",
                    "type": FlexibleModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledModeOfOperationRef",
                    "type": ScheduledModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    transport_organisation_ref: Optional[Union[AuthorityRef, OperatorRef]] = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "AuthorityRef",
                        "type": AuthorityRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "OperatorRef",
                        "type": OperatorRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
    line_ref: Optional[Union[FlexibleLineRef, LineRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    booked_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "BookedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
