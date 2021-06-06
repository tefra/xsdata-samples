from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .block_parts_rel_structure import BlockPartsRelStructure
from .compound_train_ref import CompoundTrainRef
from .courses_of_journeys_rel_structure import CoursesOfJourneysRelStructure
from .day_type_refs_rel_structure import DayTypeRefsRelStructure
from .journey_refs_rel_structure import JourneyRefsRelStructure
from .multilingual_string import MultilingualString
from .point_ref_structure import PointRefStructure
from .private_code import PrivateCode
from .relief_opportunities_rel_structure import ReliefOpportunitiesRelStructure
from .train_ref import TrainRef
from .vehicle_service_part_ref import VehicleServicePartRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlockVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Block_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    preparation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
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
    finishing_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FinishingDuration",
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
    day_types: Optional[DayTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_service_part_ref: Optional[VehicleServicePartRef] = field(
        default=None,
        metadata={
            "name": "VehicleServicePartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_train_ref: List[CompoundTrainRef] = field(
        default_factory=list,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    train_ref: List[TrainRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    vehicle_type_ref: Optional[VehicleTypeRef] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journeys: Optional[JourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    courses_of_journeys: Optional[CoursesOfJourneysRelStructure] = field(
        default=None,
        metadata={
            "name": "coursesOfJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    block_parts: Optional[BlockPartsRelStructure] = field(
        default=None,
        metadata={
            "name": "blockParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_opportunities: Optional[ReliefOpportunitiesRelStructure] = field(
        default=None,
        metadata={
            "name": "reliefOpportunities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
