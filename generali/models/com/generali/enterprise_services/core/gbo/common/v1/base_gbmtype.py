from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass(kw_only=True)
class BaseGbmtype:
    """
    <description xmlns="">The base type of the business
    message.</description>.
    """

    class Meta:
        name = "BaseGBMType"
