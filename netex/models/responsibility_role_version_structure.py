from dataclasses import dataclass, field

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .type_of_responsibility_role_ref import TypeOfResponsibilityRoleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilityRoleVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ResponsibilityRole_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_responsibility_role_ref: TypeOfResponsibilityRoleRef | None = (
        field(
            default=None,
            metadata={
                "name": "TypeOfResponsibilityRoleRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
