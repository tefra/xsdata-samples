from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.individual_role_type import (
    IndividualRoleType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class MultinationalFrontingOfficeRoleType(IndividualRoleType):
    pass
