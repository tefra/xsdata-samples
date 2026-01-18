from __future__ import annotations

from dataclasses import dataclass, field

from .abstract_request_structure import AbstractRequestStructure
from .message_qualifier_structure import MessageQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractServiceRequestStructure(AbstractRequestStructure):
    message_identifier: None | MessageQualifierStructure = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
