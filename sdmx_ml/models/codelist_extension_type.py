from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from sdmx_ml.models.code_selection_type import CodeSelectionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CodelistExtensionType:
    """CodelistExtensionType defines the structure of a codelist to be extended by
    the codelist defining the extension.

    It provides a reference to the extended codelist and selection
    criteria to indicate the codes to be included in the extending
    codelist.

    :ivar codelist:
    :ivar inclusive_code_selection_or_exclusive_code_selection:
    :ivar prefix: A reference to a codelist may contain a prefix. If a
        prefix is provided, this prefix will be applied to all the codes
        in the codelist before they are imported into the extended
        codelist.
    """

    codelist: Optional[str] = field(
        default=None,
        metadata={
            "name": "Codelist",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.codelist\.Codelist=.+",
        },
    )
    inclusive_code_selection_or_exclusive_code_selection: Optional[
        Union[
            "CodelistExtensionType.InclusiveCodeSelection",
            "CodelistExtensionType.ExclusiveCodeSelection",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "InclusiveCodeSelection",
                    "type": ForwardRef(
                        "CodelistExtensionType.InclusiveCodeSelection"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "ExclusiveCodeSelection",
                    "type": ForwardRef(
                        "CodelistExtensionType.ExclusiveCodeSelection"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(frozen=True)
    class InclusiveCodeSelection(CodeSelectionType):
        pass

    @dataclass(frozen=True)
    class ExclusiveCodeSelection(CodeSelectionType):
        pass
