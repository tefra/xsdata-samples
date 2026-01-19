from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.ruleset_scheme_type import RulesetSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class RulesetSchemesType:
    """
    RulesetSchemesType describes the structure of the ruleset schemes
    container.

    It contains one or more ruleset scheme, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar ruleset_scheme: RulesetScheme provides the details of a
        ruleset scheme, in which rulesets are described.
    """

    ruleset_scheme: tuple[RulesetSchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RulesetScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
