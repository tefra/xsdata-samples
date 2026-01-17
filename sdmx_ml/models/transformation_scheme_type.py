from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.transformation_scheme_base_type import (
    TransformationSchemeBaseType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class TransformationSchemeType(TransformationSchemeBaseType):
    """
    TransformationSchemeType describes the structure of a transformation
    scheme.

    A transformation scheme contains a set of transformations to be
    executed together (in the same run). It can contain any number of
    transformations that produce any number of results.

    :ivar vtl_mapping_scheme: References a VTL mapping scheme which
        defines aliases for given SDMX artefacts that are used in the
        transformations as well as the mapping methods used when
        converting between SDMX and VTL data structures. All aliases
        must be defined in the referenced scheme. This also must be used
        if the basic mapping methods are not used.
    :ivar name_personalisation_scheme: References a name personalisation
        scheme, which defines the overriding of some standard VTL names
        (to be assigned to some measures and/or attributes of the data
        structure) with some corresponding personalised names. This must
        be used if transformations within a transformation scheme
        personalise standard names. All personalisations must be defined
        in the referenced scheme.
    :ivar custom_type_scheme: References a custom type scheme which
        defines custom conversions of VTL scalar types to SDMX data
        types. This must be used if custom type conversions are used in
        the transformations defined in a transformation scheme. All
        custom conversions must be defined in the referenced scheme.
    :ivar ruleset_scheme: References a ruleset scheme that defines one
        or more previously defined rulesets which can be invoked by VTL
        operators. If a transformation defined in a transformation
        scheme refers to a ruleset, the scheme in which the ruleset is
        defined must be referenced here.
    :ivar user_defined_operator_scheme: References a user defined
        operator scheme that defines one or more user defined operators
        used by the transformations defined in a transformation scheme.
        If a transformation in a transformation scheme refers to a user
        defined operator, the scheme in which the user defined operator
        is defined must be referenced here.
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
    name_personalisation_scheme: Optional[str] = field(
        default=None,
        metadata={
            "name": "NamePersonalisationScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.transformation\.NamePersonalisationScheme=.+",
        },
    )
    custom_type_scheme: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomTypeScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.transformation\.CustomTypeScheme=.+",
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
    user_defined_operator_scheme: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "UserDefinedOperatorScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.transformation\.UserDefinedOperatorScheme=.+",
        },
    )
