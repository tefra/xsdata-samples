from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SimpleDataSourceType:
    """SimpleDataSourceType describes a simple data source.

    The URL of the data is contained in the content.

    :ivar value:
    :ivar type_value: TYPE is a fixed attribute that is used to ensure
        only one simple data source may be provided, when it is
        referenced in a uniqueness constraint.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: str = field(
        init=False,
        default="SIMPLE",
        metadata={
            "name": "TYPE",
            "type": "Attribute",
        },
    )
