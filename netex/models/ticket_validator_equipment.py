from dataclasses import dataclass
from .ticket_validator_equipment_version_structure import TicketValidatorEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TicketValidatorEquipment(TicketValidatorEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
