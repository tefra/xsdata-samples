from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import CodeType
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import Idtype
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_simple_component_type import BaseSimpleComponentType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class StatusHistoryType:
    """<description xmlns="">A history of the lifecycle state transistions of a
    business object.

    Each transition records the date and time and should record the
    target lifecycle status.</description>
    """
    state_transition: List["StatusHistoryType.StateTransition"] = field(
        default_factory=list,
        metadata={
            "name": "StateTransition",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        }
    )

    @dataclass
    class StateTransition(BaseSimpleComponentType):
        """
        :ivar from_status_code: <description xmlns="">The source
            lifecycle state of the transition, i.e. the state from which
            the transition is moving, for example: from "Active" to
            "Cancelled".</description>
        :ivar to_status_code: <description xmlns="">The target lifecycle
            state of the transition, i.e. the state to which the
            transition is moving, for example: from "Active" to
            "Cancelled".</description>
        :ivar effective_date_time: <description xmlns="">The date and
            time of the transistion, i.e. the timestamp of when the
            target state was entered.</description>
        :ivar reasons:
        :ivar changed_by_user_id: <description xmlns="">A reference to
            the User [Account] who initiated the lifecycle state
            transition.</description>
        """
        from_status_code: Optional[CodeType] = field(
            default=None,
            metadata={
                "name": "FromStatusCode",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            }
        )
        to_status_code: Optional[CodeType] = field(
            default=None,
            metadata={
                "name": "ToStatusCode",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            }
        )
        effective_date_time: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "EffectiveDateTime",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            }
        )
        reasons: Optional["StatusHistoryType.StateTransition.Reasons"] = field(
            default=None,
            metadata={
                "name": "Reasons",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            }
        )
        changed_by_user_id: Optional[Idtype] = field(
            default=None,
            metadata={
                "name": "ChangedByUserID",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            }
        )

        @dataclass
        class Reasons:
            """
            :ivar reason_code: <description xmlns="">The code describing
                why the transition occured.</description>
            """
            reason_code: List["StatusHistoryType.StateTransition.Reasons.ReasonCode"] = field(
                default_factory=list,
                metadata={
                    "name": "ReasonCode",
                    "type": "Element",
                    "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class ReasonCode(CodeType):
                """
                :ivar list_hierarchy_id: An indication of the depth in a
                    classification hierarchy
                """
                list_hierarchy_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "listHierarchyID",
                        "type": "Attribute",
                    }
                )
