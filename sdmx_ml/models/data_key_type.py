from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.region_type import RegionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class DataKeyType(RegionType):
    """
    DataKeyType is a region which defines a distinct full or partial data
    key.

    The key consists of a set of values, each referencing a dimension and
    providing a single value for that dimension. The purpose of the key is
    to define a subset of a data set (i.e. the observed value and data
    attribute) which have the dimension values provided in this definition.
    Any dimension not stated explicitly in this key is assumed to be wild
    carded, thus allowing for the definition of partial data keys.

    :ivar include: The include attribute has a fixed value of true for a
        distinct key, since such a key is always assumed to identify
        existing data or metadata.
    """

    include: bool = field(
        init=False,
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
