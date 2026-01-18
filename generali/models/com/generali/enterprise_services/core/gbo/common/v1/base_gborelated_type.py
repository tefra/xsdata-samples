from __future__ import annotations

from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_reference_component_type import (
    BaseReferenceComponentType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseGborelatedType(BaseReferenceComponentType):
    """
    <description xmlns="">The base type for the business object related
    components.</description>.
    """

    class Meta:
        name = "BaseGBORelatedType"
