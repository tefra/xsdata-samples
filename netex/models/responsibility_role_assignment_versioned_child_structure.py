from collections.abc import Iterable
from dataclasses import dataclass, field

from .data_role_type_enumeration import DataRoleTypeEnumeration
from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString
from .organisation_part_ref_structure import OrganisationPartRefStructure
from .organisation_ref_structure import OrganisationRefStructure
from .responsibility_role_ref import ResponsibilityRoleRef
from .responsibility_set_ref import ResponsibilitySetRef
from .stakeholder_role_type_enumeration import StakeholderRoleTypeEnumeration
from .type_of_responsibility_role_ref import TypeOfResponsibilityRoleRef
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilityRoleAssignmentVersionedChildStructure(
    VersionedChildStructure
):
    class Meta:
        name = "ResponsibilityRoleAssignment_VersionedChildStructure"

    responsibility_set_ref: ResponsibilitySetRef | None = field(
        default=None,
        metadata={
            "name": "ResponsibilitySetRef",
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
    data_role_type: Iterable[DataRoleTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DataRoleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    stakeholder_role_type: Iterable[StakeholderRoleTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "StakeholderRoleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    type_of_responsibility_role_ref_or_responsibility_role_ref: (
        TypeOfResponsibilityRoleRef | ResponsibilityRoleRef | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfResponsibilityRoleRef",
                    "type": TypeOfResponsibilityRoleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResponsibilityRoleRef",
                    "type": ResponsibilityRoleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    responsible_organisation_ref: OrganisationRefStructure | None = field(
        default=None,
        metadata={
            "name": "ResponsibleOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    responsible_part_ref: OrganisationPartRefStructure | None = field(
        default=None,
        metadata={
            "name": "ResponsiblePartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    responsible_area_ref: VersionOfObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "ResponsibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
