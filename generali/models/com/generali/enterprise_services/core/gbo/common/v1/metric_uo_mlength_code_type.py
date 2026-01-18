from __future__ import annotations

from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class MetricUoMlengthCodeType(CodeType):
    """
    A codelist restricting the values to metric (SI) lengths.
    """

    class Meta:
        name = "MetricUoMLengthCodeType"
