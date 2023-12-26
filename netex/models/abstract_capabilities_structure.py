from dataclasses import dataclass, field
from typing import Optional
from .capability_general_interaction_structure import (
    CapabilityGeneralInteractionStructure,
)
from .transport_description_structure import TransportDescriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractCapabilitiesStructure:
    general_interaction: Optional[
        CapabilityGeneralInteractionStructure
    ] = field(
        default=None,
        metadata={
            "name": "GeneralInteraction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    transport_description: Optional[TransportDescriptionStructure] = field(
        default=None,
        metadata={
            "name": "TransportDescription",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
