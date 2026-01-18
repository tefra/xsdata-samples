from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlTime

from .block_part_ref import BlockPartRef
from .entity_in_version_structure import DataManagedObjectStructure
from .journey_part_couple_ref import JourneyPartCoupleRef
from .journey_part_positions_rel_structure import (
    JourneyPartPositionsRelStructure,
)
from .journey_part_ref_structure import JourneyPartRefStructure
from .multilingual_string import MultilingualString
from .purpose_of_journey_partition_ref import PurposeOfJourneyPartitionRef
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .service_facility_sets_rel_structure import (
    ServiceFacilitySetsRelStructure,
)
from .train_block_part_ref import TrainBlockPartRef
from .train_number_ref import TrainNumberRef
from .vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "JourneyPart_VersionStructure"

    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_journey_ref: VehicleJourneyRefStructure | None = field(
        default=None,
        metadata={
            "name": "ParentJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    main_part_ref: JourneyPartRefStructure | None = field(
        default=None,
        metadata={
            "name": "MainPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_part_couple_ref: JourneyPartCoupleRef | None = field(
        default=None,
        metadata={
            "name": "JourneyPartCoupleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_number_ref: TrainNumberRef | None = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    block_part_ref: TrainBlockPartRef | BlockPartRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainBlockPartRef",
                    "type": TrainBlockPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockPartRef",
                    "type": BlockPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    from_stop_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_stop_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    start_time_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "StartTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    end_time_day_offset: int | None = field(
        default=None,
        metadata={
            "name": "EndTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_orientation: bool | None = field(
        default=None,
        metadata={
            "name": "VehicleOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    purpose_of_journey_partition_ref: PurposeOfJourneyPartitionRef | None = field(
        default=None,
        metadata={
            "name": "PurposeOfJourneyPartitionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: ServiceFacilitySetsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_part_positions: JourneyPartPositionsRelStructure | None = field(
        default=None,
        metadata={
            "name": "journeyPartPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
