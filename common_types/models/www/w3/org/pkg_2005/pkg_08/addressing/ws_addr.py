from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class AttributedQnameType:
    class Meta:
        name = "AttributedQNameType"

    value: QName = field(
        metadata={
            "required": True,
        }
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class AttributedUritype:
    class Meta:
        name = "AttributedURIType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class AttributedUnsignedLongType:
    value: int = field(
        metadata={
            "required": True,
        }
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class MetadataType:
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class ReferenceParametersType:
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


class RelationshipType(Enum):
    HTTP_WWW_W3_ORG_2005_08_ADDRESSING_REPLY = (
        "http://www.w3.org/2005/08/addressing/reply"
    )


@dataclass(kw_only=True)
class Action(AttributedUritype):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class MessageId(AttributedUritype):
    class Meta:
        name = "MessageID"
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class Metadata(MetadataType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class ProblemHeaderQname(AttributedQnameType):
    class Meta:
        name = "ProblemHeaderQName"
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class ProblemIri(AttributedUritype):
    class Meta:
        name = "ProblemIRI"
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class ReferenceParameters(ReferenceParametersType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class RelatesToType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    relationship_type: RelationshipType | str = field(
        default=RelationshipType.HTTP_WWW_W3_ORG_2005_08_ADDRESSING_REPLY,
        metadata={
            "name": "RelationshipType",
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class RetryAfter(AttributedUnsignedLongType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class To(AttributedUritype):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class EndpointReferenceType:
    address: AttributedUritype = field(
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
            "required": True,
        }
    )
    reference_parameters: None | ReferenceParameters = field(
        default=None,
        metadata={
            "name": "ReferenceParameters",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
        },
    )
    metadata: None | Metadata = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class ProblemActionType:
    action: None | Action = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
        },
    )
    soap_action: None | str = field(
        default=None,
        metadata={
            "name": "SoapAction",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class RelatesTo(RelatesToType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class EndpointReference(EndpointReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class FaultTo(EndpointReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class From(EndpointReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class ProblemAction(ProblemActionType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class ReplyTo(EndpointReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"
