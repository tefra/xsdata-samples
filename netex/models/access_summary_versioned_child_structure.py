from dataclasses import dataclass, field

from .access_feature_enumeration import AccessFeatureEnumeration
from .entity_in_version_structure import VersionedChildStructure
from .transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessSummaryVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "AccessSummary_VersionedChildStructure"

    access_feature_type: AccessFeatureEnumeration | None = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    count: int | None = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    transition: TransitionEnumeration | None = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
