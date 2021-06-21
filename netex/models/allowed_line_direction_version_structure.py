from dataclasses import dataclass, field
from typing import List
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .direction_ref import DirectionRef
from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef
from .presentation_structure import PresentationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllowedLineDirectionVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "AllowedLineDirection_VersionStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DirectionRef",
                    "type": DirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                    "required": True,
                },
                {
                    "name": "Presentation",
                    "type": PresentationStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
