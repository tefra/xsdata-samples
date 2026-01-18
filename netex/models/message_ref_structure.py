from __future__ import annotations

from dataclasses import dataclass

from .message_qualifier_structure import MessageQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MessageRefStructure(MessageQualifierStructure):
    pass
