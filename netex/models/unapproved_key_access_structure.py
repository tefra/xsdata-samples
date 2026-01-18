from __future__ import annotations

from dataclasses import dataclass, field

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnapprovedKeyAccessStructure(ErrorCodeStructure):
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
