from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

from .block_ref import BlockRef
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .train_block_ref import TrainBlockRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefOpportunityVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ReliefOpportunity_VersionStructure"

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
    time: XmlTime = field(
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    day_offset: None | int = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    block_ref: None | TrainBlockRef | BlockRef = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainBlockRef",
                    "type": TrainBlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockRef",
                    "type": BlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
