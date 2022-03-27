from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import CodeType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseReferenceComponentTypeCategoriesCategoryCode(CodeType):
    """
    :ivar list_hierarchy_id: An indication of the depth in a
        classification hierarchy
    """
    class Meta:
        global_type = False

    list_hierarchy_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "listHierarchyID",
            "type": "Attribute",
        }
    )
