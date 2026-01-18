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


@dataclass(kw_only=True)
class LambdaType:
    class Meta:
        name = "lambda.class"
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
    apply: None | Apply = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bind: None | Bind = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ci: None | Ci = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cn: None | Cn = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    csymbol: None | Csymbol = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cbytes: None | Cbytes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cerror: None | Cerror = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cs: None | Cs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    share: None | Share = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    piecewise: None | Piecewise = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    declare: None | Declare = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fn: None | Fn = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reln: None | Reln = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    interval: None | Interval = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    moment: None | Moment = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    log: None | Log = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ln: None | Ln = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    image: None | Image = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    codomain: None | Codomain = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    domain: None | Domain = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ident: None | Ident = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    inverse: None | Inverse = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: None | Lambda = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    compose: None | Compose = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    quotient: None | Quotient = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    divide: None | Divide = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    minus: None | Minus = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    power: None | Power = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rem: None | Rem = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    root: None | Root = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    factorial: None | Factorial = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abs: None | Abs = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conjugate: None | Conjugate = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arg: None | Arg = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    real: None | Real = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    imaginary: None | Imaginary = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    floor: None | Floor = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ceiling: None | Ceiling = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exp: None | Exp = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    min: None | Min = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    max: None | Max = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lcm: None | Lcm = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gcd: None | Gcd = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    times: None | Times = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    plus: None | Plus = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xor: None | Xor = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    or_value: None | Or = field(
        default=None,
        metadata={
            "name": "or",
            "type": "Element",
        },
    )
    and_value: None | And = field(
        default=None,
        metadata={
            "name": "and",
            "type": "Element",
        },
    )
    not_value: None | Not = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
        },
    )
    equivalent: None | Equivalent = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    implies: None | Implies = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exists: None | Exists = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    forall: None | Forall = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    leq: None | Leq = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    geq: None | Geq = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lt: None | Lt = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gt: None | Gt = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    eq: None | Eq = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tendsto: None | Tendsto = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    factorof: None | Factorof = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    approx: None | Approx = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    neq: None | Neq = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    int_value: None | Int = field(
        default=None,
        metadata={
            "name": "int",
            "type": "Element",
        },
    )
    diff: None | Diff = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    partialdiff: None | Partialdiff = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    laplacian: None | Laplacian = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    curl: None | Curl = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    grad: None | Grad = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    divergence: None | Divergence = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    list_value: None | List = field(
        default=None,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    set: None | Set = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cartesianproduct: None | Cartesianproduct = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    intersect: None | Intersect = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    union: None | UnionType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    setdiff: None | Setdiff = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notprsubset: None | Notprsubset = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notsubset: None | Notsubset = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notin: None | Notin = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    in_value: None | In = field(
        default=None,
        metadata={
            "name": "in",
            "type": "Element",
        },
    )
    prsubset: None | Prsubset = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subset: None | Subset = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    card: None | Card = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sum: None | Sum = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    product: None | Product = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    limit: None | Limit = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arctanh: None | Arctanh = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsinh: None | Arcsinh = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsech: None | Arcsech = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsec: None | Arcsec = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccsch: None | Arccsch = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccsc: None | Arccsc = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccoth: None | Arccoth = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccot: None | Arccot = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccosh: None | Arccosh = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arctan: None | Arctan = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccos: None | Arccos = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsin: None | Arcsin = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    coth: None | Coth = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    csch: None | Csch = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sech: None | Sech = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tanh: None | Tanh = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cosh: None | Cosh = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sinh: None | Sinh = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cot: None | Cot = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    csc: None | Csc = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sec: None | Sec = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tan: None | Tan = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cos: None | Cos = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sin: None | Sin = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mode: None | Mode = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    median: None | Median = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variance: None | Variance = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sdev: None | Sdev = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mean: None | Mean = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    matrixrow: None | Matrixrow = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    matrix: None | Matrix = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vector: None | Vector = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    transpose: None | Transpose = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    determinant: None | Determinant = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    selector: None | Selector = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    outerproduct: None | Outerproduct = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scalarproduct: None | Scalarproduct = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vectorproduct: None | Vectorproduct = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    emptyset: None | Emptyset = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    primes: None | Primes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    complexes: None | Complexes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    naturalnumbers: None | Naturalnumbers = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rationals: None | Rationals = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reals: None | Reals = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    integers: None | Integers = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    infinity: None | Infinity = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    eulergamma: None | Eulergamma = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pi: None | Pi = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    false: None | FalseType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    true: None | TrueType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notanumber: None | Notanumber = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    imaginaryi: None | Imaginaryi = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exponentiale: None | Exponentiale = field(
        default=None,
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
