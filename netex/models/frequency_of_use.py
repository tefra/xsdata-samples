from __future__ import annotations

from dataclasses import dataclass

from .frequency_of_use_version_structure import FrequencyOfUseVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FrequencyOfUse(FrequencyOfUseVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
