from __future__ import annotations

from dataclasses import dataclass

from .additional_driver_option_ref_structure import (
    AdditionalDriverOptionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AdditionalDriverOptionRef(AdditionalDriverOptionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
