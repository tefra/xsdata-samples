from dataclasses import dataclass, field
from typing import List, Optional

from tpdb.models.name import Name
from tpdb.models.type_mod import TypeType
from tpdb.models.var import Var


@dataclass
class Rhs:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        name = "rhs"

    funapp: Optional["Rhs.Funapp"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    var: Optional[Var] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: Optional["Rhs.Lambda"] = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: Optional["Rhs.Application"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Funapp:
        name: Optional[Name] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        arg: List["Rhs.Funapp.Arg"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Arg:
            """
            :ivar funapp:
            :ivar var:
            :ivar lambda_value: the type is the type of the bound
                variable
            :ivar application: an application of a function (first term)
                on an argument (second term): (first second)
            """

            funapp: Optional["Rhs.Funapp"] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            var: Optional[Var] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            lambda_value: Optional["Rhs.Lambda"] = field(
                default=None,
                metadata={
                    "name": "lambda",
                    "type": "Element",
                },
            )
            application: Optional["Rhs.Application"] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

    @dataclass
    class Lambda:
        """
        :ivar var:
        :ivar type_value:
        :ivar funapp:
        :ivar lambda_value: the type is the type of the bound variable
        :ivar application: an application of a function (first term) on
            an argument (second term): (first second)
        """

        var: List[Var] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 2,
                "max_occurs": 2,
            },
        )
        type_value: Optional[TypeType] = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Element",
                "required": True,
            },
        )
        funapp: Optional["Rhs.Funapp"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        lambda_value: Optional["Rhs.Lambda"] = field(
            default=None,
            metadata={
                "name": "lambda",
                "type": "Element",
            },
        )
        application: Optional["Rhs.Application"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

    @dataclass
    class Application:
        """
        :ivar funapp:
        :ivar var:
        :ivar lambda_value: the type is the type of the bound variable
        :ivar application: an application of a function (first term) on
            an argument (second term): (first second)
        """

        funapp: List["Rhs.Funapp"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 2,
                "max_occurs": 2,
                "sequence": 1,
            },
        )
        var: List[Var] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 2,
                "max_occurs": 2,
                "sequence": 1,
            },
        )
        lambda_value: List["Rhs.Lambda"] = field(
            default_factory=list,
            metadata={
                "name": "lambda",
                "type": "Element",
                "min_occurs": 2,
                "max_occurs": 2,
                "sequence": 1,
            },
        )
        application: List["Rhs.Application"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 2,
                "max_occurs": 2,
                "sequence": 1,
            },
        )
