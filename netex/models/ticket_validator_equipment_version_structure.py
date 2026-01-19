from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .multilingual_string import MultilingualString
from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)
from .ticket_validator_enumeration import TicketValidatorEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketValidatorEquipmentVersionStructure(
    PassengerEquipmentVersionStructure
):
    class Meta:
        name = "TicketValidatorEquipment_VersionStructure"

    ticket_validator_type: Sequence[TicketValidatorEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketValidatorType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    audio_validation_feedback: None | bool = field(
        default=None,
        metadata={
            "name": "AudioValidationFeedback",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    visual_validation_feedback: None | bool = field(
        default=None,
        metadata={
            "name": "VisualValidationFeedback",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_validation_feedback: None | bool = field(
        default=None,
        metadata={
            "name": "TactileValidationFeedback",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validation_guidance: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ValidationGuidance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
