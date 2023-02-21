from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_texts_rel_structure import VersionedChildStructure
from .data_role_type_enumeration import DataRoleTypeEnumeration
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
class ResponsibilityRoleAssignmentVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "ResponsibilityRoleAssignment_VersionedChildStructure"

    responsibility_set_ref: Optional[ResponsibilitySetRef] = field(
        default=None,
        metadata={
            "name": "ResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    data_role_type: List[DataRoleTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DataRoleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    stakeholder_role_type: List[StakeholderRoleTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "StakeholderRoleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    type_of_responsibility_role_ref_or_responsibility_role_ref: List[object] = field(
        default_factory=list,
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
            "max_occurs": 2,
        }
    )
    responsible_organisation_ref: Optional[OrganisationRefStructure] = field(
        default=None,
        metadata={
            "name": "ResponsibleOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsible_part_ref: Optional[OrganisationPartRefStructure] = field(
        default=None,
        metadata={
            "name": "ResponsiblePartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsible_area_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ResponsibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
