from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import BaseIdentifiedComponentType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseGbotype(BaseIdentifiedComponentType):
    """
    <description xmlns="">The base type of the business object.</description>
    """
    class Meta:
        name = "BaseGBOType"
