from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.data_key_type import DataKeyType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DataKeySetType:
    """
    DataKeySetType defines a collection of full or partial data keys
    (dimension values).

    :ivar key: Key contains a set of dimension values which identify a
        full set of data.
    :ivar is_included: The isIncluded attribute indicates whether the
        keys defined in this key set are inclusive or exclusive to the
        constraint.
    """

    key: tuple[DataKeyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
    is_included: bool = field(
        metadata={
            "name": "isIncluded",
            "type": "Attribute",
            "required": True,
        }
    )
