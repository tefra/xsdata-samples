from dataclasses import dataclass

from .ticketing_equipment_ref_structure import TicketingEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TicketingEquipmentRef(TicketingEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
