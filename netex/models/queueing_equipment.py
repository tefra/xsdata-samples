from __future__ import annotations

from dataclasses import dataclass

from .queueing_equipment_version_structure import (
    QueueingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QueueingEquipment(QueueingEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
