from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.headers.v1.base_header_type import (
    BaseHeaderType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
)


@dataclass
class TrackingType(BaseHeaderType):
    """
    <description xmlns="">Holds in-flight tracking
    information.</description>.

    :ivar tracking_id: <description xmlns="">A identifier used to track
        a set of messages across a number of individual request/response
        interactions. This ID may exceed a process
        boundary.</description>
    :ivar conversation_id: <description xmlns="">A identifier used to
        track a set of messages across a number of individual
        request/response interactions within a process, identifies the
        process instance. This ID may not exceed a process
        boundary.</description>
    """

    tracking_id: None | str = field(
        default=None,
        metadata={
            "name": "TrackingID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
            "required": True,
        },
    )
    conversation_id: None | str = field(
        default=None,
        metadata={
            "name": "ConversationID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
            "required": True,
        },
    )
