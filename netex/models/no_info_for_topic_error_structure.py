from __future__ import annotations

from dataclasses import dataclass

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NoInfoForTopicErrorStructure(ErrorCodeStructure):
    pass
