from __future__ import annotations

from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.headers.v1.source_type import (
    SourceType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
)


@dataclass
class Source(SourceType):
    """
    <description xmlns="">The specification of the source country, locale,
    system of the message.</description>.
    """

    class Meta:
        namespace = "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
