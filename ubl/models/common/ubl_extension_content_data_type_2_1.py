from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
)


@dataclass(frozen=True)
class ExtensionContentType:
    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
