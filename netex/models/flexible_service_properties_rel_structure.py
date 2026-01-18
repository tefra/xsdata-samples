from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .flexible_service_properties import FlexibleServiceProperties
from .flexible_service_properties_ref import FlexibleServicePropertiesRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleServicePropertiesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "flexibleServiceProperties_RelStructure"

    flexible_service_properties_ref_or_flexible_service_properties: Iterable[
        FlexibleServicePropertiesRef | FlexibleServiceProperties
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleServicePropertiesRef",
                    "type": FlexibleServicePropertiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleServiceProperties",
                    "type": FlexibleServiceProperties,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
