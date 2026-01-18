from __future__ import annotations

from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass(kw_only=True)
class TelephoneNumberIdentificationCodeType(TextType):
    """
    <description xmlns=""> <description>The definition Identification Code
    or Destination Code part of a Telephone Number.</description>
    </description>.
    """
