from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.common.faults.v1.failure_type import (
    FailureType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/faults/v1"
)


@dataclass
class FaultTypeFailures:
    """
    :ivar failure: <description xmlns="">A component that describes
        individual failures within the fault. This component is used to
        support multiple causes to the fault, i.e. where the fault is
        generated from one or more API calls or one or more validation
        failures.</description>
    """

    class Meta:
        global_type = False

    failure: List[FailureType] = field(
        default_factory=list,
        metadata={
            "name": "Failure",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/faults/v1",
            "min_occurs": 1,
        },
    )
