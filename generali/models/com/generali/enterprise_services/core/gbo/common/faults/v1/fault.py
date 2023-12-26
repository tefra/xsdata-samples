from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbo.common.faults.v1.fault_type import (
    FaultType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/faults/v1"
)


@dataclass
class Fault(FaultType):
    """
    <description xmlns="">The fault object used to hold values for an
    error.</description>
    """

    class Meta:
        namespace = (
            "http://generali.com/enterprise-services/core/gbo/common/faults/v1"
        )
