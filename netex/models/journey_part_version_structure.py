from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlTime
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .block_part_ref import BlockPartRef
from .journey_part_couple_ref import JourneyPartCoupleRef
from .journey_part_couple_ref_structure import JourneyPartCoupleRefStructure
from .journey_part_positions_rel_structure import JourneyPartPositionsRelStructure
from .multilingual_string import MultilingualString
from .purpose_of_journey_partition_ref import PurposeOfJourneyPartitionRef
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .service_facility_sets_rel_structure import ServiceFacilitySetsRelStructure
from .train_block_part_ref import TrainBlockPartRef
from .train_number_ref import TrainNumberRef
from .vehicle_journey_ref_structure import VehicleJourneyRefStructure

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
    choice: List[object] = field(
        default_factory=list,
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
                {
                    "name": "FromStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ToStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTimeDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                    "default": 0,
                },
                {
                    "name": "EndTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndTimeDayOffset",
                    "type": int,
                    "namespace": "http://www.netex.org.uk/netex",
                    "default": 0,
                },
                {
                    "name": "VehicleOrientation",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                    "default": True,
                },
                {
                    "name": "PurposeOfJourneyPartitionRef",
                    "type": PurposeOfJourneyPartitionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "facilities",
                    "type": ServiceFacilitySetsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "journeyPartPositions",
                    "type": JourneyPartPositionsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "min_occurs": 2,
            "max_occurs": 14,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
