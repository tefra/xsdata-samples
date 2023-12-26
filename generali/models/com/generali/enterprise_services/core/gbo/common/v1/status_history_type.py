from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.status_history_type_state_transition import (
    StatusHistoryTypeStateTransition,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class StatusHistoryType:
    """<description xmlns="">A history of the lifecycle state transistions of a
    business object.

    Each transition records the date and time and should record the
    target lifecycle status.</description>
    """

    state_transition: List[StatusHistoryTypeStateTransition] = field(
        default_factory=list,
        metadata={
            "name": "StateTransition",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        },
    )
