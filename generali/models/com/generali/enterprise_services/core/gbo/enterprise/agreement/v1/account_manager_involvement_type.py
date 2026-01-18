from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.account_manager_involvement_type_account_manager_type import (
    AccountManagerInvolvementTypeAccountManagerType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.multinational_fronting_office_role_type import (
    MultinationalFrontingOfficeRoleType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class AccountManagerInvolvementType:
    multinational_fronting_office_role: MultinationalFrontingOfficeRoleType = field(
        metadata={
            "name": "MultinationalFrontingOfficeRole",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
    account_manager_type: AccountManagerInvolvementTypeAccountManagerType = field(
        metadata={
            "name": "AccountManagerType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        }
    )
