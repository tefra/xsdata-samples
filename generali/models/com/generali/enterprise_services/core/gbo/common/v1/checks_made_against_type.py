from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import (
    BaseIdentifiedComponentType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class ChecksMadeAgainstType(BaseIdentifiedComponentType):
    """
    The object against which the set of checks have been made.
    """
