from dataclasses import dataclass, field
from typing import Optional, Tuple, Type, Union

from sdmx_ml.models.annotable_type import AnnotableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class FixedValueMapType(AnnotableType):
    """
    FixedValueMapType defines the structure for providing a fixed value for a
    source or target component.

    :ivar source_or_target:
    :ivar value: The fixed value for the component.
    """

    source_or_target: Optional[
        Union["FixedValueMapType.Source", "FixedValueMapType.Target"]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Source",
                    "type": Type["FixedValueMapType.Source"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Target",
                    "type": Type["FixedValueMapType.Target"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    value: Tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )

    @dataclass(frozen=True)
    class Source:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
            },
        )

    @dataclass(frozen=True)
    class Target:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
            },
        )
