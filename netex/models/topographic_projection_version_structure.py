from dataclasses import dataclass, field
from typing import Optional
from netex.models.country_ref import CountryRef
from netex.models.projection_version_structure import ProjectionVersionStructure
from netex.models.topographic_place_ref import TopographicPlaceRef
from netex.models.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicProjectionVersionStructure(ProjectionVersionStructure):
    class Meta:
        name = "TopographicProjection_VersionStructure"

    projected_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
