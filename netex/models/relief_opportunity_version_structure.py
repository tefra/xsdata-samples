from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlTime
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.block_ref import BlockRef
from netex.models.multilingual_string import MultilingualString
from netex.models.train_block_ref import TrainBlockRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReliefOpportunityVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ReliefOpportunity_VersionStructure"

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
    time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_block_ref: List[TrainBlockRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    block_ref: Optional[BlockRef] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
