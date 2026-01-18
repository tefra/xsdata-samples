from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

from .car_pooling_service_ref import CarPoolingServiceRef
from .chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from .journey_version_structure import JourneyVersionStructure
from .operating_day_ref import OperatingDayRef
from .single_journey_path_ref import SingleJourneyPathRef
from .target_passing_times_rel_structure import TargetPassingTimesRelStructure
from .taxi_service_ref import TaxiServiceRef
from .vehicle_meeting_point_assignments_rel_structure import (
    VehicleMeetingPointAssignmentsRelStructure,
)
from .vehicle_ref import VehicleRef
from .vehicle_rental_service_ref import VehicleRentalServiceRef
from .vehicle_sharing_service_ref import VehicleSharingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SingleJourneyVersionStructure(JourneyVersionStructure):
    class Meta:
        name = "SingleJourney_VersionStructure"

    common_vehicle_service_ref_or_vehicle_pooling_service_ref: (
        VehicleRentalServiceRef
        | VehicleSharingServiceRef
        | ChauffeuredVehicleServiceRef
        | TaxiServiceRef
        | CarPoolingServiceRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_ref: VehicleRef | None = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    single_journey_path_ref: SingleJourneyPathRef | None = field(
        default=None,
        metadata={
            "name": "SingleJourneyPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departure_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operating_day_ref: OperatingDayRef | None = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dated_passing_times: TargetPassingTimesRelStructure | None = field(
        default=None,
        metadata={
            "name": "datedPassingTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    meeting_point_assignments: (
        VehicleMeetingPointAssignmentsRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "meetingPointAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
