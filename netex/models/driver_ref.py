from __future__ import annotations

from dataclasses import dataclass

from .driver_ref_structure import DriverRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DriverRef(DriverRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
