from __future__ import annotations

from dataclasses import dataclass

from .frequency_of_use_ref_structure import FrequencyOfUseRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FrequencyOfUseRef(FrequencyOfUseRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
