from __future__ import annotations

from dataclasses import dataclass

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_component_type import (
    BaseComponentType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class ThingActorType(BaseComponentType):
    """
    A type defining the details of a thing, examples of thing include
    servers, vehicles, aircraft, etc.
    """
