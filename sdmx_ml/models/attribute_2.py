from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.attribute_type_2 import AttributeType2

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class Attribute2(AttributeType2):
    """
    Attribute describes the definition of a data attribute, which is
    defined as a characteristic of an object or entity.
    """

    class Meta:
        name = "Attribute"
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
