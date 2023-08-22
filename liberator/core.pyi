from os import PathLike
from typing import List
import ast
from typing import Set
import astunparse
import ubelt as ub
from _typeshed import Incomplete

__todo__: str


class LocalLogger:
    verbose: Incomplete
    logs: Incomplete
    tag: Incomplete
    indent: str

    def __init__(self, tag: str = ..., verbose: int = ...) -> None:
        ...

    def warn(self, msg) -> None:
        ...

    def error(self, msg) -> None:
        ...

    def info(self, msg) -> None:
        ...

    def debug(self, msg) -> None:
        ...

    @classmethod
    def coerce(cls, item, tag: str = ..., verbose: int = ...):
        ...


class Liberator(ub.NiceRepr):

    def __init__(lib,
                 tag: str = ...,
                 logger: Incomplete | None = ...,
                 verbose: int = ...) -> None:
        ...

    def error(lib, msg) -> None:
        ...

    def info(lib, msg) -> None:
        ...

    def debug(lib, msg) -> None:
        ...

    def warn(lib, msg) -> None:
        ...

    def __nice__(self):
        ...

    def current_sourcecode(self):
        ...

    def add_dynamic(lib, obj: object, eager: bool = True) -> None:
        ...

    def add_static(lib, name: str, modpath: PathLike) -> None:
        ...

    def close2(lib, visitors) -> None:
        ...

    def close(lib, visitor) -> None:
        ...

    def expand(lib, expand_names) -> None:
        ...

    def expand_module_attributes(lib, d: Definition) -> None:
        ...


class UnparserVariant(astunparse.Unparser):
    ...


def unparse(tree: ast.AST):
    ...


def source_closure(obj: type, expand_names: List[str] = ...) -> str:
    ...


def undefined_names(sourcecode: str) -> Set[str]:
    ...


class RewriteModuleAccess(ast.NodeTransformer):
    modname: Incomplete
    level: int
    accessed_attrs: Incomplete

    def __init__(self, modname) -> None:
        ...

    def visit_Import(self, node):
        ...

    def visit_ImportFrom(self, node):
        ...

    def visit_FunctionDef(self, node):
        ...

    def visit_ClassDef(self, node):
        ...

    def visit_Attribute(self, node):
        ...


class Definition(ub.NiceRepr):
    name: Incomplete
    node: Incomplete
    type: Incomplete
    absname: Incomplete
    modpath: Incomplete
    modname: Incomplete
    native_modname: Incomplete

    def __init__(self,
                 name,
                 node,
                 type: Incomplete | None = ...,
                 code: Incomplete | None = ...,
                 absname: Incomplete | None = ...,
                 modpath: Incomplete | None = ...,
                 modname: Incomplete | None = ...,
                 native_modname: Incomplete | None = ...) -> None:
        ...

    @property
    def code(self):
        ...

    def __nice__(self):
        ...


class NotAPythonFile(ValueError):
    ...


class AttributeAccessVisitor(ast.NodeVisitor):
    dotted_trie: Incomplete

    def __init__(self) -> None:
        ...

    def visit_Attribute(self, node) -> None:
        ...


class DefinitionVisitor(ast.NodeVisitor, ub.NiceRepr):

    def __init__(visitor,
                 modpath: Incomplete | None = ...,
                 modname: Incomplete | None = ...,
                 module: Incomplete | None = ...,
                 pt: Incomplete | None = ...,
                 logger: Incomplete | None = ...) -> None:
        ...

    def __nice__(self):
        ...

    @classmethod
    def parse(DefinitionVisitor,
              source: Incomplete | None = ...,
              modpath: Incomplete | None = ...,
              modname: Incomplete | None = ...,
              module: Incomplete | None = ...,
              logger: Incomplete | None = ...):
        ...

    def extract_definition(visitor, name):
        ...

    def visit_Import(visitor, node) -> None:
        ...

    def visit_ImportFrom(visitor, node) -> None:
        ...

    def visit_AnnAssign(visitor, node) -> None:
        ...

    def visit_Assign(visitor, node) -> None:
        ...

    def visit_FunctionDef(visitor, node) -> None:
        ...

    def visit_ClassDef(visitor, node) -> None:
        ...


class Closer(Liberator):
    ...
