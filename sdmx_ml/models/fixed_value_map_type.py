from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from sdmx_ml.models.annotable_type import AnnotableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class FixedValueMapType(AnnotableType):
    """
    FixedValueMapType defines the structure for providing a fixed value for
    a source or target component.

    :ivar source_or_target:
    :ivar value: The fixed value for the component.
    """

    source_or_target: FixedValueMapType.Source | FixedValueMapType.Target | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Source",
                    "type": ForwardRef("FixedValueMapType.Source"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Target",
                    "type": ForwardRef("FixedValueMapType.Target"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    value: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )

    @dataclass(frozen=True)
    class Source:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
            },
        )

    @dataclass(frozen=True)
    class Target:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
            },
        )
