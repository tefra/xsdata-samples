from __future__ import annotations

from dataclasses import dataclass, field

from .medium_application_instance_ref import MediumApplicationInstanceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MediumApplicationInstanceRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "mediumApplicationInstanceRefs_RelStructure"

    medium_application_instance_ref: MediumApplicationInstanceRef = field(
        metadata={
            "name": "MediumApplicationInstanceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
