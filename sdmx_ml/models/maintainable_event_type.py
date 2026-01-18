from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.maintainable_query_type import MaintainableQueryType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True, kw_only=True)
class MaintainableEventType:
    """
    MaintainableEventType provides a reference to a maintainable object's
    event with either the URN of the specific object, or a set of
    potentially wild-carded reference fields.
    """

    urn_or_ref: None | str | MaintainableQueryType = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "URN",
                    "type": str,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Ref",
                    "type": MaintainableQueryType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
            ),
        },
    )
