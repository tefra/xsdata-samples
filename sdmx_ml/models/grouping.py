from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.grouping_type import GroupingType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class Grouping(GroupingType):
    """
    Grouping is an abstract element that serves as a substitution head for
    all structure groupings.

    Groupings contain a collection of component lists for a structure.
    Concrete instances of this must use a concrete instance of
    GroupingType.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"
        )
