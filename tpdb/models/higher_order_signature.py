from dataclasses import dataclass, field
from typing import List, Optional

from tpdb.models.func_declaration import FuncDeclaration
from tpdb.models.var_declaration import VarDeclaration


@dataclass
class HigherOrderSignature:
    """
    :ivar variable_type_info: type for free variables
    :ivar function_symbol_type_info: a higher-order symbol f with
        children types t1,...,tn,t has type: (t1,...,tn) -&gt; t
    """

    class Meta:
        name = "higherOrderSignature"

    variable_type_info: Optional["HigherOrderSignature.VariableTypeInfo"] = (
        field(
            default=None,
            metadata={
                "name": "variableTypeInfo",
                "type": "Element",
            },
        )
    )
    function_symbol_type_info: Optional[
        "HigherOrderSignature.FunctionSymbolTypeInfo"
    ] = field(
        default=None,
        metadata={
            "name": "functionSymbolTypeInfo",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class VariableTypeInfo:
        var_declaration: List[VarDeclaration] = field(
            default_factory=list,
            metadata={
                "name": "varDeclaration",
                "type": "Element",
            },
        )

    @dataclass
    class FunctionSymbolTypeInfo:
        func_declaration: List[FuncDeclaration] = field(
            default_factory=list,
            metadata={
                "name": "funcDeclaration",
                "type": "Element",
            },
        )
