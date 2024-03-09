from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.local_data_type_entry import (
    LocalDataTypeEntry,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class LocalDataType:
    entry: List[LocalDataTypeEntry] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
