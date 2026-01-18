from dataclasses import dataclass, field

from .country_ref import CountryRef
from .projection_version_structure import ProjectionVersionStructure
from .topographic_place_ref import TopographicPlaceRef
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicProjectionVersionStructure(ProjectionVersionStructure):
    class Meta:
        name = "TopographicProjection_VersionStructure"

    projected_object_ref: VersionOfObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "ProjectedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    country_ref_or_topographic_place_ref: (
        CountryRef | TopographicPlaceRef | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CountryRef",
                    "type": CountryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
