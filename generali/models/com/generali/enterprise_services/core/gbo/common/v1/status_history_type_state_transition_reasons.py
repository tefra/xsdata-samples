from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.status_history_type_state_transition_reasons_reason_code import (
    StatusHistoryTypeStateTransitionReasonsReasonCode,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class StatusHistoryTypeStateTransitionReasons:
    """
    :ivar reason_code: <description xmlns="">The code describing why the
        transition occured.</description>
    """

    class Meta:
        global_type = False

    reason_code: List[
        StatusHistoryTypeStateTransitionReasonsReasonCode
    ] = field(
        default_factory=list,
        metadata={
            "name": "ReasonCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        },
    )
