from __future__ import annotations

from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .service_access_code_ref import ServiceAccessCodeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceAccessCodeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "serviceAccessCodeRefs_RelStructure"

    service_access_code_ref: ServiceAccessCodeRef = field(
        metadata={
            "name": "ServiceAccessCodeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
