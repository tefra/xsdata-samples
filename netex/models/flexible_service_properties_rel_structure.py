from dataclasses import dataclass, field
from typing import List
from .flexible_service_properties import FlexibleServiceProperties
from .flexible_service_properties_ref import FlexibleServicePropertiesRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleServicePropertiesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "flexibleServiceProperties_RelStructure"

    flexible_service_properties_ref: List[FlexibleServicePropertiesRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleServicePropertiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_service_properties: List[FlexibleServiceProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleServiceProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
