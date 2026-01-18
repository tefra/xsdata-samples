from __future__ import annotations

from dataclasses import dataclass

from .duty_version_structure import DutyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Duty(DutyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
