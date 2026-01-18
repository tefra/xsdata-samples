from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.text_type import (
    TextType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type_ids import (
    BaseIdentifiedComponentTypeIds,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class BaseIdentifiedComponentType(BaseComponentType):
    """
    <description xmlns="">The base type for all business objects and
    components with an identifier and a lifecycle state.</description>.

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
    :ivar creation_date: <description xmlns="">The date and time the
        business object or component was created. A date and time
        formatted in compliance with the ISO8601 standard must be
        used.</description>
    :ivar created_by_id: <description xmlns="">The unique ID of the User
        that created the instance of the business object or component.
        This should be used as a reference to the IDM system and the
        details about that User.</description>
    :ivar date_last_update: <description xmlns="">The date and time the
        business object or component was last modified. A date and time
        formatted in compliance with the ISO8601 standard must be
        used.</description>
    :ivar last_modified_by_id: <description xmlns="">The unique ID of
        the User that last modified the instance of the business object
        or component. This should be used as a reference to the IDM
        system and the details about that User.</description>
    :ivar notes:
    """

    ids: None | BaseIdentifiedComponentTypeIds = field(
        default=None,
        metadata={
            "name": "IDs",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    name_text: None | TextType = field(
        default=None,
        metadata={
            "name": "NameText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    desc_text: None | TextType = field(
        default=None,
        metadata={
            "name": "DescText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    full_name: None | TextType = field(
        default=None,
        metadata={
            "name": "FullName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    status_code: None | CodeType = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    version_id: None | Idtype = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    creation_date: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "CreationDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    created_by_id: None | Idtype = field(
        default=None,
        metadata={
            "name": "CreatedByID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    date_last_update: None | DateTimeType = field(
        default=None,
        metadata={
            "name": "DateLastUpdate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    last_modified_by_id: None | Idtype = field(
        default=None,
        metadata={
            "name": "LastModifiedByID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    notes: None | TextType = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
