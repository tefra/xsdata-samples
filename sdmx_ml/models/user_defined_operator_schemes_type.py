from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.user_defined_operator_scheme_type import (
    UserDefinedOperatorSchemeType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class UserDefinedOperatorSchemesType:
    """
    UserDefinedOperatorSchemesType describes the structure of the user
    defined operator schemes container.

    It contains one or more user defined operator scheme, which can be
    explicitly detailed or referenced from an external structure document
    or registry service.

    :ivar user_defined_operator_scheme: UserDefinedOperatorScheme
        provides the details of a user defined operator scheme, in which
        user defined operators are described.
    """

    user_defined_operator_scheme: tuple[UserDefinedOperatorSchemeType, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "UserDefinedOperatorScheme",
                "type": "Element",
                "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                "min_occurs": 1,
            },
        )
    )
