from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseGbodetailsType(BaseComponentType):
    """
    <description xmlns="">The base type for the business object details
    components.</description>
    """

    class Meta:
        name = "BaseGBODetailsType"
