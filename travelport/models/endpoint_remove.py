from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_editable_endpoint import TypeEditableEndpoint

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class EndpointRemove(TypeEditableEndpoint):
    """
    Removes an endpoint from an action in a particular field or field group.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"
