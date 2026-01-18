from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_reference_component_optional_type_categories_category_code import (
    BaseReferenceComponentOptionalTypeCategoriesCategoryCode,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseReferenceComponentOptionalTypeCategories:
    """
    :ivar category_code: <description xmlns="">A classification applied
        to the business object or component. More than one
        classification scheme can be applied using the @listName
        attribute to identify the type of code list being used. The
        classification scheme can be used to group instances of the
        object or component.</description>
    """

    class Meta:
        global_type = False

    category_code: list[
        BaseReferenceComponentOptionalTypeCategoriesCategoryCode
    ] = field(
        default_factory=list,
        metadata={
            "name": "CategoryCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        },
    )
