from __future__ import annotations

from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass(kw_only=True)
class GenderCodeType(CodeType):
    """
    <description xmlns="">A codelist indicating the gender of an individual
    in the normal run of things or of a concept if applicable, i.e.

    Words can have gender in French and German.</description>.
    """
