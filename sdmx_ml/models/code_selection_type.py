from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.member_value_type import MemberValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CodeSelectionType:
    """
    CodeSelectionType defines the structure for code selection to be used as
    inclusive or exclusive extensions.

    :ivar member_value: An explicit or wildcard selection of a code(s)
        from the codelist selected for inclusion/exclusion. If a
        wildcard expression is used, it is evaluated to determine codes
        selected for inclusion/exclusion. Otherwise, each member value
        is a distinct code. If the extended list is hierarchical, this
        can indicate whether child codes are to be included.
    """

    member_value: Tuple[MemberValueType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MemberValue",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
