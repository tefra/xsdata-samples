from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.member_selection_type import MemberSelectionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class CubeRegionKeyType(MemberSelectionType):
    """
    CubeRegionKeyType is a type for providing a set of values for a
    dimension for the purpose of defining a data cube region.

    A set of distinct value can be provided, or if this dimension is
    represented as time, and time range can be specified.
    """
