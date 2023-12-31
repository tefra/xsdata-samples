from dataclasses import dataclass, field
from typing import Optional
from .common_version_frame_structure import CommonVersionFrameStructure
from .groups_of_single_journeys_rel_structure import (
    GroupsOfSingleJourneysRelStructure,
)
from .individual_travellers_in_frame_rel_structure import (
    IndividualTravellersInFrameRelStructure,
)
from .parking_log_entries_in_frame_rel_structure import (
    ParkingLogEntriesInFrameRelStructure,
)
from .single_journey_paths_rel_structure import SingleJourneyPathsRelStructure
from .single_journeys_rel_structure import SingleJourneysRelStructure
from .vehicle_access_credential_assignments_rel_structure import (
    VehicleAccessCredentialAssignmentsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityJourneyVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "MobilityJourney_VersionFrameStructure"

    single_journey_paths: Optional[SingleJourneyPathsRelStructure] = field(
        default=None,
        metadata={
            "name": "singleJourneyPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_single_journeys: Optional[
        GroupsOfSingleJourneysRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "groupsOfSingleJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    single_journeys: Optional[SingleJourneysRelStructure] = field(
        default=None,
        metadata={
            "name": "singleJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    individual_travellers: Optional[
        IndividualTravellersInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "individualTravellers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_access_credentials: Optional[
        VehicleAccessCredentialAssignmentsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "vehicleAccessCredentials",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_log_entries: Optional[
        ParkingLogEntriesInFrameRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "parkingLogEntries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
