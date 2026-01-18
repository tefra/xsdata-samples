from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.base_dimension_type import BaseDimensionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class DimensionType(BaseDimensionType):
    """
    DimensionType describes the structure of an ordinary dimension, which
    is defined as a statistical concept used (most probably together with
    other statistical concepts) to identify a statistical series, such as a
    time series, e.g. a statistical concept indicating certain economic
    activity or a geographical reference area.

    The dimension takes its semantic, and in some cases it representation,
    from its concept identity. A dimension can be coded by referencing a
    code list from its coded local representation. It can also specify its
    text format, which is used as the representation of the dimension if a
    coded representation is not defined. Neither the coded or uncoded
    representation are necessary, since the dimension may take these from
    the referenced concept.
    """
