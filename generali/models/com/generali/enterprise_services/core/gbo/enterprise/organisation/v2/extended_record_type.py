from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.company_info_type import CompanyInfoType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.domestic_ultimate_info_type import DomesticUltimateInfoType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.global_ultimate_info_type import GlobalUltimateInfoType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.tree_below_type import TreeBelowType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2"


@dataclass
class ExtendedRecordType:
    company_info: Optional[CompanyInfoType] = field(
        default=None,
        metadata={
            "name": "CompanyInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        }
    )
    global_ultimate_info: Optional[GlobalUltimateInfoType] = field(
        default=None,
        metadata={
            "name": "GlobalUltimateInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        }
    )
    domestic_ultimate_info: Optional[DomesticUltimateInfoType] = field(
        default=None,
        metadata={
            "name": "DomesticUltimateInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        }
    )
    tree_below_info: Optional[TreeBelowType] = field(
        default=None,
        metadata={
            "name": "TreeBelowInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        }
    )
    duplicated_gunsnumbers: Optional["ExtendedRecordType.DuplicatedGunsnumbers"] = field(
        default=None,
        metadata={
            "name": "DuplicatedGUNSNumbers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        }
    )
    party_roles: Optional["ExtendedRecordType.PartyRoles"] = field(
        default=None,
        metadata={
            "name": "PartyRoles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        }
    )

    @dataclass
    class DuplicatedGunsnumbers:
        duplicated_gunsnumber: List[str] = field(
            default_factory=list,
            metadata={
                "name": "DuplicatedGUNSNumber",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
                "length": 10,
                "pattern": r"G([0-9]{9})",
            }
        )

    @dataclass
    class PartyRoles:
        role: List[str] = field(
            default_factory=list,
            metadata={
                "name": "Role",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            }
        )
