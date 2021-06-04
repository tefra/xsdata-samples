from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.data_role_type_enumeration import DataRoleTypeEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.organisation_part_ref_structure import OrganisationPartRefStructure
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.responsibility_role_ref import ResponsibilityRoleRef
from netex.models.responsibility_set_ref import ResponsibilitySetRef
from netex.models.stakeholder_role_type_enumeration import StakeholderRoleTypeEnumeration
from netex.models.type_of_responsibility_role_ref import TypeOfResponsibilityRoleRef
from netex.models.version_of_object_ref_structure import VersionOfObjectRefStructure

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
    type_of_responsibility_role_ref: Optional[TypeOfResponsibilityRoleRef] = field(
        default=None,
        metadata={
            "name": "TypeOfResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_role_ref: Optional[ResponsibilityRoleRef] = field(
        default=None,
        metadata={
            "name": "ResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
