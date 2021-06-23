from dataclasses import dataclass, field
from typing import Optional
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

    flexible_line_ref: Optional[FlexibleLineRef] = field(
        default=None,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
