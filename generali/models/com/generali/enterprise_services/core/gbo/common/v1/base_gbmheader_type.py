from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.header_type import (
    HeaderType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseGbmheaderType:
    """
    <description xmlns="">The base type of the business
    message.</description>.
    """

    class Meta:
        name = "BaseGBMHeaderType"

    header: None | HeaderType = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        },
    )
