from __future__ import annotations

from dataclasses import dataclass

from .control_centre_version_structure import ControlCentreVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControlCentre(ControlCentreVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
