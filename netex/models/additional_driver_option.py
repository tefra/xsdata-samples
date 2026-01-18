from __future__ import annotations

from dataclasses import dataclass

from .additional_driver_option_version_structure import (
    AdditionalDriverOptionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AdditionalDriverOption(AdditionalDriverOptionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
