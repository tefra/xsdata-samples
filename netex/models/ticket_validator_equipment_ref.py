from dataclasses import dataclass
from netex.models.ticket_validator_equipment_ref_structure import TicketValidatorEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TicketValidatorEquipmentRef(TicketValidatorEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
