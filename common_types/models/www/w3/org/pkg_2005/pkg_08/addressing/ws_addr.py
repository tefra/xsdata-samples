from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class AttributedQnameType:
    class Meta:
        name = "AttributedQNameType"

    value: QName | None = field(
        default=None,
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


@dataclass
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


@dataclass
class AttributedUnsignedLongType:
    value: int | None = field(
        default=None,
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


@dataclass
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


@dataclass
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
    address: AttributedUritype | None = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
            "required": True,
        },
    )
    reference_parameters: ReferenceParameters | None = field(
        default=None,
        metadata={
            "name": "ReferenceParameters",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
        },
    )
    metadata: Metadata | None = field(
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


@dataclass
class ProblemActionType:
    action: Action | None = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
        },
    )
    soap_action: str | None = field(
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
class From(EndpointReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class ProblemAction(ProblemActionType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"


@dataclass
class ReplyTo(EndpointReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"
