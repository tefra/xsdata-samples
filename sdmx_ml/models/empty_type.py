from dataclasses import dataclass

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class EmptyType:
    """
    EmptyType is an empty complex type for elements where the presence of the tag
    indicates all that is necessary.
    """
