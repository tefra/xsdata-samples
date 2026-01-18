from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_simple_component_type import (
    BaseSimpleComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.status_history_type_state_transition_reasons import (
    StatusHistoryTypeStateTransitionReasons,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class StatusHistoryTypeStateTransition(BaseSimpleComponentType):
    """
    :ivar from_status_code: <description xmlns="">The source lifecycle
        state of the transition, i.e. the state from which the
        transition is moving, for example: from "Active" to
        "Cancelled".</description>
    :ivar to_status_code: <description xmlns="">The target lifecycle
        state of the transition, i.e. the state to which the transition
        is moving, for example: from "Active" to
        "Cancelled".</description>
    :ivar effective_date_time: <description xmlns="">The date and time
        of the transistion, i.e. the timestamp of when the target state
        was entered.</description>
    :ivar reasons:
    :ivar changed_by_user_id: <description xmlns="">A reference to the
        User [Account] who initiated the lifecycle state
        transition.</description>
    """

    class Meta:
        global_type = False

    from_status_code: CodeType | None = field(
        default=None,
        metadata={
            "name": "FromStatusCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    to_status_code: CodeType | None = field(
        default=None,
        metadata={
            "name": "ToStatusCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    effective_date_time: DateTimeType | None = field(
        default=None,
        metadata={
            "name": "EffectiveDateTime",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    reasons: StatusHistoryTypeStateTransitionReasons | None = field(
        default=None,
        metadata={
            "name": "Reasons",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    changed_by_user_id: Idtype | None = field(
        default=None,
        metadata={
            "name": "ChangedByUserID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
