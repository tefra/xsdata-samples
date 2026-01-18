from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ParametersIgnoredErrorStructure(ErrorCodeStructure):
    parameter_name: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "ParameterName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
