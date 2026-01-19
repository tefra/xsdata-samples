from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from sdmx_ml.models.identifiable_type import IdentifiableType
from sdmx_ml.models.resolve_period_type import ResolvePeriodType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DateMapType(IdentifiableType):
    """
    :ivar source:
    :ivar target:
    :ivar
        frequency_dimension_or_mapped_frequencies_or_target_frequency_id:
    :ivar resolve_period: Indicates the point in time to resolve to when
        mapping from low frequency periods to higher frequency periods.
    """

    source: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    target: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    frequency_dimension_or_mapped_frequencies_or_target_frequency_id: tuple[
        DateMapType.FrequencyDimension
        | DateMapType.MappedFrequencies
        | DateMapType.TargetFrequencyId,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FrequencyDimension",
                    "type": ForwardRef("DateMapType.FrequencyDimension"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "MappedFrequencies",
                    "type": ForwardRef("DateMapType.MappedFrequencies"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "TargetFrequencyID",
                    "type": ForwardRef("DateMapType.TargetFrequencyId"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
            ),
        },
    )
    resolve_period: None | ResolvePeriodType = field(
        default=None,
        metadata={
            "name": "resolvePeriod",
            "type": "Attribute",
        },
    )

    @dataclass(frozen=True, kw_only=True)
    class FrequencyDimension:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
            },
        )

    @dataclass(frozen=True, kw_only=True)
    class MappedFrequencies:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
            },
        )

    @dataclass(frozen=True, kw_only=True)
    class TargetFrequencyId:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
            },
        )
