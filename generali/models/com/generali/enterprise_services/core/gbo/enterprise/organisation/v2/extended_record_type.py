from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class ExtendedRecordType:
    company_info: None | CompanyInfoType = field(
        default=None,
        metadata={
            "name": "CompanyInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    global_ultimate_info: None | GlobalUltimateInfoType = field(
        default=None,
        metadata={
            "name": "GlobalUltimateInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    domestic_ultimate_info: None | DomesticUltimateInfoType = field(
        default=None,
        metadata={
            "name": "DomesticUltimateInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    tree_below_info: None | TreeBelowType = field(
        default=None,
        metadata={
            "name": "TreeBelowInfo",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    duplicated_gunsnumbers: None | ExtendedRecordTypeDuplicatedGunsnumbers = (
        field(
            default=None,
            metadata={
                "name": "DuplicatedGUNSNumbers",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            },
        )
    )
    party_roles: None | ExtendedRecordTypePartyRoles = field(
        default=None,
        metadata={
            "name": "PartyRoles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
