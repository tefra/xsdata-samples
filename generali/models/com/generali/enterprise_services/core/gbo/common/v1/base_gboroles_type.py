from __future__ import annotations

from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass(kw_only=True)
class BaseGborolesType(BaseComponentType):
    """
    <description xmlns="">The base type for the business object roles
    components.</description>.
    """

    class Meta:
        name = "BaseGBORolesType"
