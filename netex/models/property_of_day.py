from __future__ import annotations

from dataclasses import dataclass

from .property_of_day_structure import PropertyOfDayStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PropertyOfDay(PropertyOfDayStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
