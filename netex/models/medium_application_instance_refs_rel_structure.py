from dataclasses import dataclass, field
from typing import Optional

from .medium_application_instance_ref import MediumApplicationInstanceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MediumApplicationInstanceRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "mediumApplicationInstanceRefs_RelStructure"

    medium_application_instance_ref: Optional[MediumApplicationInstanceRef] = (
        field(
            default=None,
            metadata={
                "name": "MediumApplicationInstanceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
        )
    )
