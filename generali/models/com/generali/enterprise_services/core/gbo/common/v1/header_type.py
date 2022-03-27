from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.header_type_properties import HeaderTypeProperties
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.header_type_target_systems import HeaderTypeTargetSystems

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class HeaderType:
    """The header is mandatory for all messages and provides information that a
    service may need in order to communicate or process the message.

    It contains non-business fields which assist in the handling of the
    message, such as a ConversationID, for auditing/tracking.

    :ivar source_system: The identifier of the system that generated the
        message.
    :ivar target_systems: The identifier of the target system(s).
    :ivar conversation_id: Identifies a conversation or flow of a
        message through a series of services. This allows the life of a
        request to be tracked from the point it is received in the
        integration layer, through to its eventual destination. This is
        used to enable visibility of multiple message hops in a single
        integration flow. Correlation of individual messages for
        interaction purposes (for example Request-Reply), should be
        achieved using the wsa:RelatesTo element instead.
    :ivar message_id: The Identifier of the transmission.
    :ivar properties: The identifier of the target system(s).
    :ivar creation_date_time: The date and time that this message was
        generated.
    :ivar event:
    """
    source_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceSystem",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    target_systems: Optional[HeaderTypeTargetSystems] = field(
        default=None,
        metadata={
            "name": "TargetSystems",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    conversation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConversationID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    message_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    properties: Optional[HeaderTypeProperties] = field(
        default=None,
        metadata={
            "name": "Properties",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    creation_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreationDateTime",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    event: Optional[str] = field(
        default=None,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
