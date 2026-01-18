from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_simple_component_type import (
    BaseSimpleComponentType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class NoteType(BaseSimpleComponentType):
    """
    <description xmlns="">Notes related to the entity</description>.

    :ivar text: <description xmlns="">Textual content of the
        Note</description>
    :ivar last_modified_date_time: <description xmlns="">Last Modified
        time of the notes</description>
    :ivar agent_id: <description xmlns="">Agent or user who updated or
        created the notes</description>
    """

    text: TextType | None = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        },
    )
    last_modified_date_time: DateTimeType | None = field(
        default=None,
        metadata={
            "name": "LastModifiedDateTime",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    agent_id: Idtype | None = field(
        default=None,
        metadata={
            "name": "AgentID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
