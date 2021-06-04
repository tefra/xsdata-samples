from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.installed_equipment_version_structure import InstalledEquipmentVersionStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.ticket_validator_enumeration import TicketValidatorEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TicketValidatorEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    class Meta:
        name = "TicketValidatorEquipment_VersionStructure"

    ticket_validator_type: List[TicketValidatorEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketValidatorType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    audio_validation_feedback: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioValidationFeedback",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    visual_validation_feedback: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisualValidationFeedback",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_validation_feedback: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileValidationFeedback",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validation_guidance: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ValidationGuidance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
