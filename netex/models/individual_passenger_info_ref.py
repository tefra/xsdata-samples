from dataclasses import dataclass
from .individual_passenger_info_ref_structure import (
    IndividualPassengerInfoRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class IndividualPassengerInfoRef(IndividualPassengerInfoRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
