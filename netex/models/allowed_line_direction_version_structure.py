from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.direction_ref import DirectionRef
from netex.models.flexible_line_ref import FlexibleLineRef
from netex.models.line_ref import LineRef
from netex.models.presentation_structure import PresentationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllowedLineDirectionVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "AllowedLineDirection_VersionStructure"

    flexible_line_ref: List[FlexibleLineRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
