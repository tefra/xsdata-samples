from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.company_info_type import (
    CompanyInfoType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.domestic_ultimate_info_type import (
    DomesticUltimateInfoType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.extended_record_type_duplicated_gunsnumbers import (
    ExtendedRecordTypeDuplicatedGunsnumbers,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.extended_record_type_party_roles import (
    ExtendedRecordTypePartyRoles,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.global_ultimate_info_type import (
    GlobalUltimateInfoType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.tree_below_type import (
    TreeBelowType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2"


@dataclass
class ExtendedRecordType:
    company_info: Optional[CompanyInfoType] = field(
        default=None,
        metadata={
            "name": "CompanyInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    global_ultimate_info: Optional[GlobalUltimateInfoType] = field(
        default=None,
        metadata={
            "name": "GlobalUltimateInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    domestic_ultimate_info: Optional[DomesticUltimateInfoType] = field(
        default=None,
        metadata={
            "name": "DomesticUltimateInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    tree_below_info: Optional[TreeBelowType] = field(
        default=None,
        metadata={
            "name": "TreeBelowInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    duplicated_gunsnumbers: Optional[
        ExtendedRecordTypeDuplicatedGunsnumbers
    ] = field(
        default=None,
        metadata={
            "name": "DuplicatedGUNSNumbers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    party_roles: Optional[ExtendedRecordTypePartyRoles] = field(
        default=None,
        metadata={
            "name": "PartyRoles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
