from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.user_defined_operator_scheme_base_type import (
    UserDefinedOperatorSchemeBaseType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class UserDefinedOperatorSchemeType(UserDefinedOperatorSchemeBaseType):
    """
    UserDefinedOperatorSchemeType defines a collection of user defined
    operators that are used in transformations.

    :ivar vtl_mapping_scheme: References a VTL mapping scheme which
        defines aliases for given SDMX artefacts that are used in the
        user defined operators. Although the VTL user defined operators
        are conceived to be defined on generic operands, so that the
        specific artefacts to be manipulated are passed as parameters at
        the invocation, it is also possible that they reference specific
        SDMX artefacts like Dataflows, Codelists and ConceptSchemes. In
        this case, the mapping schemes referenced here define the
        mappings to those artefacts.
    :ivar ruleset_scheme: References a ruleset scheme defining rulesets
        utilized in the user defined operators.
    """

    vtl_mapping_scheme: None | str = field(
        default=None,
        metadata={
            "name": "VtlMappingScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.transformation\.VtlMappingScheme=.+",
        },
    )
    ruleset_scheme: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RulesetScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.transformation\.RulesetScheme=.+",
        },
    )
