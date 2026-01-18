from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration, XmlTime

from .block_parts_rel_structure import BlockPartsRelStructure
from .compound_train_ref import CompoundTrainRef
from .courses_of_journeys_rel_structure import CoursesOfJourneysRelStructure
from .day_type_refs_rel_structure import DayTypeRefsRelStructure
from .entity_in_version_structure import DataManagedObjectStructure
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

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: PrivateCode | None = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preparation_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
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
    finishing_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "FinishingDuration",
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
    day_types: DayTypeRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_service_part_ref: VehicleServicePartRef | None = field(
        default=None,
        metadata={
            "name": "VehicleServicePartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_type_ref: CompoundTrainRef | TrainRef | VehicleTypeRef | None = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "CompoundTrainRef",
                        "type": CompoundTrainRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "TrainRef",
                        "type": TrainRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "VehicleTypeRef",
                        "type": VehicleTypeRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
    start_point_ref: PointRefStructure | None = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_point_ref: PointRefStructure | None = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journeys: JourneyRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    courses_of_journeys: CoursesOfJourneysRelStructure | None = field(
        default=None,
        metadata={
            "name": "coursesOfJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    block_parts: BlockPartsRelStructure | None = field(
        default=None,
        metadata={
            "name": "blockParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    relief_opportunities: ReliefOpportunitiesRelStructure | None = field(
        default=None,
        metadata={
            "name": "reliefOpportunities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
