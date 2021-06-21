from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .block_parts_rel_structure import BlockPartsRelStructure
from .compound_train_ref import CompoundTrainRef
from .multilingual_string import MultilingualString
from .timing_point_in_journey_pattern_ref_structure import TimingPointInJourneyPatternRefStructure
from .train_ref import TrainRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompoundBlockStructure(DataManagedObjectStructure):
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
    choice: List[object] = field(
        default_factory=list,
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
                {
                    "name": "StartPointRef",
                    "type": TimingPointInJourneyPatternRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndPointRef",
                    "type": TimingPointInJourneyPatternRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "parts",
                    "type": BlockPartsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 4,
        }
    )
