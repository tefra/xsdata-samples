from __future__ import annotations

from dataclasses import dataclass

from .parameters_ignored_error_structure import ParametersIgnoredErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ParametersIgnoredError(ParametersIgnoredErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
