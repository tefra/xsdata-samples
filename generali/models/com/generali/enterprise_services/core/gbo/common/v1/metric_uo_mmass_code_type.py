from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class MetricUoMmassCodeType(CodeType):
    """
    A codelist restricting the values to metric (SI) mass.
    """

    class Meta:
        name = "MetricUoMMassCodeType"
