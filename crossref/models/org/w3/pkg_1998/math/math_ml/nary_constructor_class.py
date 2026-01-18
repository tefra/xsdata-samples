from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.w3.pkg_1998.math.math_ml.abs import Abs
from crossref.models.org.w3.pkg_1998.math.math_ml.and_mod import And
from crossref.models.org.w3.pkg_1998.math.math_ml.approx import Approx
from crossref.models.org.w3.pkg_1998.math.math_ml.arccos import Arccos
from crossref.models.org.w3.pkg_1998.math.math_ml.arccosh import Arccosh
from crossref.models.org.w3.pkg_1998.math.math_ml.arccot import Arccot
from crossref.models.org.w3.pkg_1998.math.math_ml.arccoth import Arccoth
from crossref.models.org.w3.pkg_1998.math.math_ml.arccsc import Arccsc
from crossref.models.org.w3.pkg_1998.math.math_ml.arccsch import Arccsch
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsec import Arcsec
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsech import Arcsech
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsin import Arcsin
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsinh import Arcsinh
from crossref.models.org.w3.pkg_1998.math.math_ml.arctan import Arctan
from crossref.models.org.w3.pkg_1998.math.math_ml.arctanh import Arctanh
from crossref.models.org.w3.pkg_1998.math.math_ml.arg import Arg
from crossref.models.org.w3.pkg_1998.math.math_ml.card import Card
from crossref.models.org.w3.pkg_1998.math.math_ml.cartesianproduct import (
    Cartesianproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.cbytes import Cbytes
from crossref.models.org.w3.pkg_1998.math.math_ml.ceiling import Ceiling
from crossref.models.org.w3.pkg_1998.math.math_ml.cerror import (
    Apply,
    Bind,
    Bvar,
    Cerror,
    Ci,
    Cn,
    Condition,
    Csymbol,
    Declare,
    Domainofapplication,
    Fn,
    List,
    Lowlimit,
    Piecewise,
    Reln,
    Set,
    Uplimit,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.codomain import Codomain
from crossref.models.org.w3.pkg_1998.math.math_ml.complexes import Complexes
from crossref.models.org.w3.pkg_1998.math.math_ml.compose import Compose
from crossref.models.org.w3.pkg_1998.math.math_ml.conjugate import Conjugate
from crossref.models.org.w3.pkg_1998.math.math_ml.cos import Cos
from crossref.models.org.w3.pkg_1998.math.math_ml.cosh import Cosh
from crossref.models.org.w3.pkg_1998.math.math_ml.cot import Cot
from crossref.models.org.w3.pkg_1998.math.math_ml.coth import Coth
from crossref.models.org.w3.pkg_1998.math.math_ml.cs import Cs
from crossref.models.org.w3.pkg_1998.math.math_ml.csc import Csc
from crossref.models.org.w3.pkg_1998.math.math_ml.csch import Csch
from crossref.models.org.w3.pkg_1998.math.math_ml.curl import Curl
from crossref.models.org.w3.pkg_1998.math.math_ml.determinant import (
    Determinant,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.diff import Diff
from crossref.models.org.w3.pkg_1998.math.math_ml.divergence import Divergence
from crossref.models.org.w3.pkg_1998.math.math_ml.divide import Divide
from crossref.models.org.w3.pkg_1998.math.math_ml.domain import Domain
from crossref.models.org.w3.pkg_1998.math.math_ml.emptyset import Emptyset
from crossref.models.org.w3.pkg_1998.math.math_ml.eq import Eq
from crossref.models.org.w3.pkg_1998.math.math_ml.equivalent import Equivalent
from crossref.models.org.w3.pkg_1998.math.math_ml.eulergamma import Eulergamma
from crossref.models.org.w3.pkg_1998.math.math_ml.exists import Exists
from crossref.models.org.w3.pkg_1998.math.math_ml.exp import Exp
from crossref.models.org.w3.pkg_1998.math.math_ml.exponentiale import (
    Exponentiale,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.factorial import Factorial
from crossref.models.org.w3.pkg_1998.math.math_ml.factorof import Factorof
from crossref.models.org.w3.pkg_1998.math.math_ml.false import FalseType
from crossref.models.org.w3.pkg_1998.math.math_ml.floor import Floor
from crossref.models.org.w3.pkg_1998.math.math_ml.forall import Forall
from crossref.models.org.w3.pkg_1998.math.math_ml.gcd import Gcd
from crossref.models.org.w3.pkg_1998.math.math_ml.geq import Geq
from crossref.models.org.w3.pkg_1998.math.math_ml.grad import Grad
from crossref.models.org.w3.pkg_1998.math.math_ml.gt import Gt
from crossref.models.org.w3.pkg_1998.math.math_ml.ident import Ident
from crossref.models.org.w3.pkg_1998.math.math_ml.image import Image
from crossref.models.org.w3.pkg_1998.math.math_ml.imaginary import Imaginary
from crossref.models.org.w3.pkg_1998.math.math_ml.imaginaryi import Imaginaryi
from crossref.models.org.w3.pkg_1998.math.math_ml.implies import Implies
from crossref.models.org.w3.pkg_1998.math.math_ml.in_mod import In
from crossref.models.org.w3.pkg_1998.math.math_ml.infinity import Infinity
from crossref.models.org.w3.pkg_1998.math.math_ml.int_mod import Int
from crossref.models.org.w3.pkg_1998.math.math_ml.integers import Integers
from crossref.models.org.w3.pkg_1998.math.math_ml.intersect import Intersect
from crossref.models.org.w3.pkg_1998.math.math_ml.interval import Interval
from crossref.models.org.w3.pkg_1998.math.math_ml.inverse import Inverse
from crossref.models.org.w3.pkg_1998.math.math_ml.lambda_mod import Lambda
from crossref.models.org.w3.pkg_1998.math.math_ml.laplacian import Laplacian
from crossref.models.org.w3.pkg_1998.math.math_ml.lcm import Lcm
from crossref.models.org.w3.pkg_1998.math.math_ml.leq import Leq
from crossref.models.org.w3.pkg_1998.math.math_ml.limit import Limit
from crossref.models.org.w3.pkg_1998.math.math_ml.ln import Ln
from crossref.models.org.w3.pkg_1998.math.math_ml.log import Log
from crossref.models.org.w3.pkg_1998.math.math_ml.lt import Lt
from crossref.models.org.w3.pkg_1998.math.math_ml.matrix import Matrix
from crossref.models.org.w3.pkg_1998.math.math_ml.matrixrow import Matrixrow
from crossref.models.org.w3.pkg_1998.math.math_ml.max import Max
from crossref.models.org.w3.pkg_1998.math.math_ml.mean import Mean
from crossref.models.org.w3.pkg_1998.math.math_ml.median import Median
from crossref.models.org.w3.pkg_1998.math.math_ml.min import Min
from crossref.models.org.w3.pkg_1998.math.math_ml.minus import Minus
from crossref.models.org.w3.pkg_1998.math.math_ml.mode import Mode
from crossref.models.org.w3.pkg_1998.math.math_ml.moment import Moment
from crossref.models.org.w3.pkg_1998.math.math_ml.naturalnumbers import (
    Naturalnumbers,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.neq import Neq
from crossref.models.org.w3.pkg_1998.math.math_ml.not_mod import Not
from crossref.models.org.w3.pkg_1998.math.math_ml.notanumber import Notanumber
from crossref.models.org.w3.pkg_1998.math.math_ml.notin import Notin
from crossref.models.org.w3.pkg_1998.math.math_ml.notprsubset import (
    Notprsubset,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.notsubset import Notsubset
from crossref.models.org.w3.pkg_1998.math.math_ml.or_mod import Or
from crossref.models.org.w3.pkg_1998.math.math_ml.outerproduct import (
    Outerproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.partialdiff import (
    Partialdiff,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.pi import Pi
from crossref.models.org.w3.pkg_1998.math.math_ml.plus import Plus
from crossref.models.org.w3.pkg_1998.math.math_ml.power import Power
from crossref.models.org.w3.pkg_1998.math.math_ml.primes import Primes
from crossref.models.org.w3.pkg_1998.math.math_ml.product import Product
from crossref.models.org.w3.pkg_1998.math.math_ml.prsubset import Prsubset
from crossref.models.org.w3.pkg_1998.math.math_ml.quotient import Quotient
from crossref.models.org.w3.pkg_1998.math.math_ml.rationals import Rationals
from crossref.models.org.w3.pkg_1998.math.math_ml.real import Real
from crossref.models.org.w3.pkg_1998.math.math_ml.reals import Reals
from crossref.models.org.w3.pkg_1998.math.math_ml.rem import Rem
from crossref.models.org.w3.pkg_1998.math.math_ml.root import Root
from crossref.models.org.w3.pkg_1998.math.math_ml.scalarproduct import (
    Scalarproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.sdev import Sdev
from crossref.models.org.w3.pkg_1998.math.math_ml.sec import Sec
from crossref.models.org.w3.pkg_1998.math.math_ml.sech import Sech
from crossref.models.org.w3.pkg_1998.math.math_ml.selector import Selector
from crossref.models.org.w3.pkg_1998.math.math_ml.setdiff import Setdiff
from crossref.models.org.w3.pkg_1998.math.math_ml.share import Share
from crossref.models.org.w3.pkg_1998.math.math_ml.sin import Sin
from crossref.models.org.w3.pkg_1998.math.math_ml.sinh import Sinh
from crossref.models.org.w3.pkg_1998.math.math_ml.subset import Subset
from crossref.models.org.w3.pkg_1998.math.math_ml.sum import Sum
from crossref.models.org.w3.pkg_1998.math.math_ml.tan import Tan
from crossref.models.org.w3.pkg_1998.math.math_ml.tanh import Tanh
from crossref.models.org.w3.pkg_1998.math.math_ml.tendsto import Tendsto
from crossref.models.org.w3.pkg_1998.math.math_ml.times import Times
from crossref.models.org.w3.pkg_1998.math.math_ml.transpose import Transpose
from crossref.models.org.w3.pkg_1998.math.math_ml.true import TrueType
from crossref.models.org.w3.pkg_1998.math.math_ml.union import UnionType
from crossref.models.org.w3.pkg_1998.math.math_ml.variance import Variance
from crossref.models.org.w3.pkg_1998.math.math_ml.vector import Vector
from crossref.models.org.w3.pkg_1998.math.math_ml.vectorproduct import (
    Vectorproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.xor import Xor

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class NaryConstructorType:
    class Meta:
        name = "nary-constructor.class"
        namespace = "http://www.w3.org/1998/Math/MathML"

    bvar: list[Bvar] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    domainofapplication: list[Domainofapplication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    condition: list[Condition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lowlimit: list[Lowlimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    uplimit: list[Uplimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    apply: list[Apply] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    bind: list[Bind] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ci: list[Ci] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cn: list[Cn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    csymbol: list[Csymbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cbytes: list[Cbytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cerror: list[Cerror] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cs: list[Cs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    share: list[Share] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    piecewise: list[Piecewise] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    declare: list[Declare] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fn: list[Fn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    reln: list[Reln] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    interval: list[Interval] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    moment: list[Moment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    log: list[Log] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ln: list[Ln] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    image: list[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    codomain: list[Codomain] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    domain: list[Domain] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ident: list[Ident] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    inverse: list[Inverse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: list[Lambda] = field(
        default_factory=list,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    compose: list[Compose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    quotient: list[Quotient] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    divide: list[Divide] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    minus: list[Minus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    power: list[Power] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rem: list[Rem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    root: list[Root] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    factorial: list[Factorial] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abs: list[Abs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    conjugate: list[Conjugate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arg: list[Arg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    real: list[Real] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    imaginary: list[Imaginary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    floor: list[Floor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ceiling: list[Ceiling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    exp: list[Exp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    min: list[Min] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    max: list[Max] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lcm: list[Lcm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    gcd: list[Gcd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    times: list[Times] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    plus: list[Plus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    xor: list[Xor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    or_value: list[Or] = field(
        default_factory=list,
        metadata={
            "name": "or",
            "type": "Element",
        },
    )
    and_value: list[And] = field(
        default_factory=list,
        metadata={
            "name": "and",
            "type": "Element",
        },
    )
    not_value: list[Not] = field(
        default_factory=list,
        metadata={
            "name": "not",
            "type": "Element",
        },
    )
    equivalent: list[Equivalent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    implies: list[Implies] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    exists: list[Exists] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    forall: list[Forall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    leq: list[Leq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    geq: list[Geq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lt: list[Lt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    gt: list[Gt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    eq: list[Eq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tendsto: list[Tendsto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    factorof: list[Factorof] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    approx: list[Approx] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    neq: list[Neq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    int_value: list[Int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
        },
    )
    diff: list[Diff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    partialdiff: list[Partialdiff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    laplacian: list[Laplacian] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    curl: list[Curl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    grad: list[Grad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    divergence: list[Divergence] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    set: list[Set] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cartesianproduct: list[Cartesianproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    intersect: list[Intersect] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    union: list[UnionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    setdiff: list[Setdiff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notprsubset: list[Notprsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notsubset: list[Notsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notin: list[Notin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    in_value: list[In] = field(
        default_factory=list,
        metadata={
            "name": "in",
            "type": "Element",
        },
    )
    prsubset: list[Prsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    subset: list[Subset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    card: list[Card] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sum: list[Sum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    product: list[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    limit: list[Limit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arctanh: list[Arctanh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsinh: list[Arcsinh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsech: list[Arcsech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsec: list[Arcsec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccsch: list[Arccsch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccsc: list[Arccsc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccoth: list[Arccoth] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccot: list[Arccot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccosh: list[Arccosh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arctan: list[Arctan] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccos: list[Arccos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsin: list[Arcsin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    coth: list[Coth] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    csch: list[Csch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sech: list[Sech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tanh: list[Tanh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cosh: list[Cosh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sinh: list[Sinh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cot: list[Cot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    csc: list[Csc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tan: list[Tan] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cos: list[Cos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sin: list[Sin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mode: list[Mode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    median: list[Median] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    variance: list[Variance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sdev: list[Sdev] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mean: list[Mean] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    matrixrow: list[Matrixrow] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    matrix: list[Matrix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    vector: list[Vector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    transpose: list[Transpose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    determinant: list[Determinant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    selector: list[Selector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    outerproduct: list[Outerproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    scalarproduct: list[Scalarproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    vectorproduct: list[Vectorproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    emptyset: list[Emptyset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    primes: list[Primes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    complexes: list[Complexes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    naturalnumbers: list[Naturalnumbers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rationals: list[Rationals] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    reals: list[Reals] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    integers: list[Integers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    infinity: list[Infinity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    eulergamma: list[Eulergamma] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    pi: list[Pi] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    false: list[FalseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    true: list[TrueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notanumber: list[Notanumber] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    imaginaryi: list[Imaginaryi] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    exponentiale: list[Exponentiale] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    encoding: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    definition_url: None | str = field(
        default=None,
        metadata={
            "name": "definitionURL",
            "type": "Attribute",
        },
    )
