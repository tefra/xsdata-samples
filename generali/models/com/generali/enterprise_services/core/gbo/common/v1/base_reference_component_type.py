from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import CodeType
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import Idtype
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import TextType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import BaseComponentType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.time_period_type import TimePeriodType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseReferenceComponentType(BaseComponentType):
    """
    <description xmlns="">The base type for all components with an identifier
    and a lifecycle state that reference another business object.</description>

    :ivar ids: <description xmlns="">The set of Identifiers for the
        business object or component. These should be used to uniquely
        identifier instances of the business object or
        component.</description>
    :ivar name_text: <description xmlns="">The name of the instance of a
        business object or component.</description>
    :ivar desc_text: <description xmlns="">A free text description of a
        business object or component.</description>
    :ivar full_name: <description xmlns="">Full Name of the
        characteristic.</description>
    :ivar type_code: <description xmlns="">A classification of the
        business object or component. This identifies the sub-type of
        the instance of object or component.</description>
    :ivar categories: <description xmlns="">The set of classifications
        for the business object or component.</description>
    :ivar status_code: <description xmlns="">The lifecycle state of the
        business object or component. This field is used to track the
        specific state an instance of an object or component is in, e.g.
        the Customer Bill is Active or the Customer Request has been
        Cancelled.</description>
    :ivar version_id: <description xmlns="">A field that identifies the
        specific version of an instance of a business object or
        component. This field should be used in support of multi-agent
        environments to control the concurrency (locking) of the
        instance.</description>
    :ivar created_date_time: <description xmlns="">The date and time the
        business object or component was created. A date and time
        formatted in compliance with the ISO8601 standard must be
        used.</description>
    :ivar created_by_id: <description xmlns="">The unique ID of the User
        that created the instance of the business object or component.
        This should be used as a reference to the IDM system and the
        details about that User.</description>
    :ivar last_modified_date_time: <description xmlns="">The date and
        time the business object or component was last modified. A date
        and time formatted in compliance with the ISO8601 standard must
        be used.</description>
    :ivar last_modified_by_id: <description xmlns="">The unique ID of
        the User that last modified the instance of the business object
        or component. This should be used as a reference to the IDM
        system and the details about that User.</description>
    :ivar validity_period: <description xmlns="">A component that states
        the date and time from which this business object is effective
        (or valid) and the date and time to which it is effective. Again
        the ISO8601 standard must be used.</description>
    :ivar relationship_type_code: <description xmlns="">An attribute
        holding the relationship of the parent context with the
        referenced business object or component.</description>
    :ivar business_object_type_code: <description xmlns="">The type of
        the business object being referenced, i.e. Advanced Shipment
        Notification or Sales Order.</description>
    """
    ids: Optional["BaseReferenceComponentType.Ids"] = field(
        default=None,
        metadata={
            "name": "IDs",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )
    name_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "NameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    desc_text: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "DescText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    full_name: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "FullName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    type_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    categories: Optional["BaseReferenceComponentType.Categories"] = field(
        default=None,
        metadata={
            "name": "Categories",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    status_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    version_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    created_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreatedDateTime",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    created_by_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "CreatedByID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    last_modified_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastModifiedDateTime",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    last_modified_by_id: Optional[Idtype] = field(
        default=None,
        metadata={
            "name": "LastModifiedByID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    validity_period: Optional[TimePeriodType] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    relationship_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "relationshipTypeCode",
            "type": "Attribute",
        }
    )
    business_object_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "businessObjectTypeCode",
            "type": "Attribute",
        }
    )

    @dataclass
    class Ids:
        """
        :ivar id: <description xmlns="">The identifier of the business
            object or component. This should be used to identify
            instances of a business object or component. Where the
            component is being used to reference another business object
            then this is the "primary key" of the target object. Use the
            attributes @schemeName and @schemeAgencyName to identify
            type of Identifier.</description>
        """
        id: List[Idtype] = field(
            default_factory=list,
            metadata={
                "name": "ID",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Categories:
        """
        :ivar category_code: <description xmlns="">A classification
            applied to the business object or component. More than one
            classification scheme can be applied using the @listName
            attribute to identify the type of code list being used. The
            classification scheme can be used to group instances of the
            object or component.</description>
        """
        category_code: List["BaseReferenceComponentType.Categories.CategoryCode"] = field(
            default_factory=list,
            metadata={
                "name": "CategoryCode",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
                "min_occurs": 1,
            }
        )

        @dataclass
        class CategoryCode(CodeType):
            """
            :ivar list_hierarchy_id: An indication of the depth in a
                classification hierarchy
            """
            list_hierarchy_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "listHierarchyID",
                    "type": "Attribute",
                }
            )
