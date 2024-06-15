from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.higher_order_signature_function_symbol_type_info import (
    HigherOrderSignatureFunctionSymbolTypeInfo,
)
from tpdb.models.higher_order_signature_variable_type_info import (
    HigherOrderSignatureVariableTypeInfo,
)


@dataclass
class HigherOrderSignature:
    """
    :ivar variable_type_info: type for free variables
    :ivar function_symbol_type_info: a higher-order symbol f with
        children types t1,...,tn,t has type: (t1,...,tn) -&gt; t
    """

    class Meta:
        name = "higherOrderSignature"

    variable_type_info: Optional[HigherOrderSignatureVariableTypeInfo] = field(
        default=None,
        metadata={
            "name": "variableTypeInfo",
            "type": "Element",
        },
    )
    function_symbol_type_info: Optional[
        HigherOrderSignatureFunctionSymbolTypeInfo
    ] = field(
        default=None,
        metadata={
            "name": "functionSymbolTypeInfo",
            "type": "Element",
            "required": True,
        },
    )
