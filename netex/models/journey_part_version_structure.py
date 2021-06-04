from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlTime
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.block_part_ref import BlockPartRef
from netex.models.journey_part_couple_ref import JourneyPartCoupleRef
from netex.models.journey_part_couple_ref_structure import JourneyPartCoupleRefStructure
from netex.models.journey_part_positions_rel_structure import JourneyPartPositionsRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.purpose_of_journey_partition_ref import PurposeOfJourneyPartitionRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.service_facility_sets_rel_structure import ServiceFacilitySetsRelStructure
from netex.models.train_block_part_ref import TrainBlockPartRef
from netex.models.train_number_ref import TrainNumberRef
from netex.models.vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPartVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "JourneyPart_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_journey_ref: Optional[VehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    main_part_ref: Optional[JourneyPartCoupleRefStructure] = field(
        default=None,
        metadata={
            "name": "MainPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    journey_part_couple_ref: Optional[JourneyPartCoupleRef] = field(
        default=None,
        metadata={
            "name": "JourneyPartCoupleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_number_ref: Optional[TrainNumberRef] = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_block_part_ref: List[TrainBlockPartRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
        }
    )
    block_part_ref: Optional[BlockPartRef] = field(
        default=None,
        metadata={
            "name": "BlockPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    start_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    end_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EndTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_orientation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VehicleOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purpose_of_journey_partition_ref: Optional[PurposeOfJourneyPartitionRef] = field(
        default=None,
        metadata={
            "name": "PurposeOfJourneyPartitionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facilities: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_positions: Optional[JourneyPartPositionsRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyPartPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
