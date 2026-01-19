from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.vtl_definition_scheme_type import VtlDefinitionSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class RulesetSchemeBaseType(VtlDefinitionSchemeType):
    """
    RulesetSchemeBaseType is an abstract base type for the
    RulesetSchemeType.

    It restricts the item types to be only rulesets.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
