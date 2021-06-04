from dataclasses import dataclass, field
from typing import Optional
from netex.models.data_managed_object_view_structure import DataManagedObjectViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassingTimeViewStructure(DataManagedObjectViewStructure):
    class Meta:
        name = "PassingTime_ViewStructure"

    day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
