from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.ruleset_scheme_base_type import RulesetSchemeBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class RulesetSchemeType(RulesetSchemeBaseType):
    """
    RulesetSchemeType defines a collection of rulesets that are used in
    transformations.

    :ivar vtl_mapping_scheme: References a VTL mapping scheme which
        defines aliases for given SDMX artefacts that are used in the
        rulesets. Rulesets defined on value domains reference Codelists
        or Concept Schemes (the latter in VTL are considered as the
        Value Domains of the variables corresponding to the SDMX Measure
        Dimensions). The rulesets defined on variables reference
        Concepts (for which a definite representation is assumed).
        Therefore, a ruleset should only refer to Codelists, Concept
        Schemes, and Concepts.
    """

    vtl_mapping_scheme: Optional[str] = field(
        default=None,
        metadata={
            "name": "VtlMappingScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.transformation\.VtlMappingScheme=.+",
        },
    )
