from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.organisation_role_type import (
    OrganisationRoleType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class InsuredRoleType(OrganisationRoleType):
    pass
