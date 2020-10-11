from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Union
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class AttributedQnameType:
    """
    :ivar value:
    :ivar other_attributes:
    """
    class Meta:
        name = "AttributedQNameType"

    value: Optional[QName] = field(
        default=None,
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )


@dataclass
class AttributedUritype:
    """
    :ivar value:
    :ivar other_attributes:
    """
    class Meta:
        name = "AttributedURIType"

    value: Optional[str] = field(
        default=None,
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )


@dataclass
class AttributedUnsignedLongType:
    """
    :ivar value:
    :ivar other_attributes:
    """
    value: Optional[int] = field(
        default=None,
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )


class FaultCodesType(Enum):
    """
    :cvar TNS_INVALID_ADDRESSING_HEADER:
    :cvar TNS_INVALID_ADDRESS:
    :cvar TNS_INVALID_EPR:
    :cvar TNS_INVALID_CARDINALITY:
    :cvar TNS_MISSING_ADDRESS_IN_EPR:
    :cvar TNS_DUPLICATE_MESSAGE_ID:
    :cvar TNS_ACTION_MISMATCH:
    :cvar TNS_MESSAGE_ADDRESSING_HEADER_REQUIRED:
    :cvar TNS_DESTINATION_UNREACHABLE:
    :cvar TNS_ACTION_NOT_SUPPORTED:
    :cvar TNS_ENDPOINT_UNAVAILABLE:
    """
    TNS_INVALID_ADDRESSING_HEADER = QName("{http://www.w3.org/2005/08/addressing}InvalidAddressingHeader")
    TNS_INVALID_ADDRESS = QName("{http://www.w3.org/2005/08/addressing}InvalidAddress")
    TNS_INVALID_EPR = QName("{http://www.w3.org/2005/08/addressing}InvalidEPR")
    TNS_INVALID_CARDINALITY = QName("{http://www.w3.org/2005/08/addressing}InvalidCardinality")
    TNS_MISSING_ADDRESS_IN_EPR = QName("{http://www.w3.org/2005/08/addressing}MissingAddressInEPR")
    TNS_DUPLICATE_MESSAGE_ID = QName("{http://www.w3.org/2005/08/addressing}DuplicateMessageID")
    TNS_ACTION_MISMATCH = QName("{http://www.w3.org/2005/08/addressing}ActionMismatch")
    TNS_MESSAGE_ADDRESSING_HEADER_REQUIRED = QName("{http://www.w3.org/2005/08/addressing}MessageAddressingHeaderRequired")
    TNS_DESTINATION_UNREACHABLE = QName("{http://www.w3.org/2005/08/addressing}DestinationUnreachable")
    TNS_ACTION_NOT_SUPPORTED = QName("{http://www.w3.org/2005/08/addressing}ActionNotSupported")
    TNS_ENDPOINT_UNAVAILABLE = QName("{http://www.w3.org/2005/08/addressing}EndpointUnavailable")


@dataclass
class MetadataType:
    """
    :ivar any_element:
    :ivar other_attributes:
    """
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )


@dataclass
class ReferenceParametersType:
    """
    :ivar any_element:
    :ivar other_attributes:
    """
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )


class RelationshipType(Enum):
    """
    :cvar HTTP_WWW_W3_ORG_2005_08_ADDRESSING_REPLY:
    """
    HTTP_WWW_W3_ORG_2005_08_ADDRESSING_REPLY = "http://www.w3.org/2005/08/addressing/reply"


@dataclass
class Action(AttributedUritype):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class MessageId(AttributedUritype):
    class Meta:
        name = "MessageID"
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class Metadata(MetadataType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class ProblemHeaderQname(AttributedQnameType):
    class Meta:
        name = "ProblemHeaderQName"
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class ProblemIri(AttributedUritype):
    class Meta:
        name = "ProblemIRI"
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class ReferenceParameters(ReferenceParametersType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class RelatesToType:
    """
    :ivar value:
    :ivar relationship_type:
    :ivar other_attributes:
    """
    value: Optional[str] = field(
        default=None,
    )
    relationship_type: Union[RelationshipType, str] = field(
        default=RelationshipType.HTTP_WWW_W3_ORG_2005_08_ADDRESSING_REPLY,
        metadata=dict(
            name="RelationshipType",
            type="Attribute"
        )
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )


@dataclass
class RetryAfter(AttributedUnsignedLongType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class To(AttributedUritype):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class EndpointReferenceType:
    """
    :ivar address:
    :ivar reference_parameters:
    :ivar metadata:
    :ivar other_element:
    :ivar other_attributes:
    """
    address: Optional[AttributedUritype] = field(
        default=None,
        metadata=dict(
            name="Address",
            type="Element",
            namespace="http://www.w3.org/2005/08/addressing",
            required=True
        )
    )
    reference_parameters: Optional[ReferenceParameters] = field(
        default=None,
        metadata=dict(
            name="ReferenceParameters",
            type="Element",
            namespace="http://www.w3.org/2005/08/addressing"
        )
    )
    metadata: Optional[Metadata] = field(
        default=None,
        metadata=dict(
            name="Metadata",
            type="Element",
            namespace="http://www.w3.org/2005/08/addressing"
        )
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )


@dataclass
class ProblemActionType:
    """
    :ivar action:
    :ivar soap_action:
    :ivar other_attributes:
    """
    action: Optional[Action] = field(
        default=None,
        metadata=dict(
            name="Action",
            type="Element",
            namespace="http://www.w3.org/2005/08/addressing"
        )
    )
    soap_action: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SoapAction",
            type="Element",
            namespace="http://www.w3.org/2005/08/addressing"
        )
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )


@dataclass
class RelatesTo(RelatesToType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class EndpointReference(EndpointReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class FaultTo(EndpointReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class FromType(EndpointReferenceType):
    class Meta:
        name = "From"
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class ProblemAction(ProblemActionType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class ReplyTo(EndpointReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"
