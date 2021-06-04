from dataclasses import dataclass, field
from typing import Optional
from netex.models.destination_display_views_rel_structure import DestinationDisplayViewsRelStructure
from netex.models.flexible_quay_version_structure import FlexibleQuayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleAreaVersionStructure(FlexibleQuayVersionStructure):
    class Meta:
        name = "FlexibleArea_VersionStructure"

    destinations: Optional[DestinationDisplayViewsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
