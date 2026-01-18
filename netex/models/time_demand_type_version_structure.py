from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import DataManagedObjectStructure
from .journey_headways_rel_structure import JourneyHeadwaysRelStructure
from .journey_layovers_rel_structure import JourneyLayoversRelStructure
from .journey_run_times_rel_structure import JourneyRunTimesRelStructure
from .journey_wait_times_rel_structure import JourneyWaitTimesRelStructure
from .multilingual_string import MultilingualString
from .presentation_structure import PresentationStructure
from .private_code import PrivateCode
from .type_of_time_demand_type_ref import TypeOfTimeDemandTypeRef
from .vehicle_type_preferences_rel_structure import (
    VehicleTypePreferencesRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeDemandTypeVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TimeDemandType_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: None | PrivateCode = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_time_demand_type_ref: None | TypeOfTimeDemandTypeRef = field(
        default=None,
        metadata={
            "name": "TypeOfTimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation: None | PresentationStructure = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    run_times: None | JourneyRunTimesRelStructure = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wait_times: None | JourneyWaitTimesRelStructure = field(
        default=None,
        metadata={
            "name": "waitTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    layovers: None | JourneyLayoversRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    headways: None | JourneyHeadwaysRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_preferences: None | VehicleTypePreferencesRelStructure = field(
        default=None,
        metadata={
            "name": "vehiclePreferences",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
