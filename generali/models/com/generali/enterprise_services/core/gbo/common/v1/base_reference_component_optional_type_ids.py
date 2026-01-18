from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseReferenceComponentOptionalTypeIds:
    """
    :ivar id: <description xmlns="">The identifier of the business
        object or component. This should be used to identify instances
        of a business object or component. Where the component is being
        used to reference another business object then this is the
        "primary key" of the target object. Use the attributes
        @schemeName and @schemeAgencyName to identify type of
        Identifier.</description>
    """

    class Meta:
        global_type = False

    id: list[Idtype] = field(
        default_factory=list,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        },
    )
