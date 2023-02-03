# Credit to sphinx.ext.extlinks for being a good starter
# Copyright 2007-2020 by the Sphinx team
# Licensed under BSD.

import typing as t

import sphinx
from docutils import nodes, utils
from docutils.nodes import Node, system_message
from docutils.parsers.rst.states import Inliner
from sphinx.application import Sphinx
from sphinx.util.nodes import split_explicit_title
from sphinx.util.typing import RoleFunction


def make_link_role(resource_links: t.Dict[str, str]) -> RoleFunction:
    def role(
        typ: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Inliner,
        options: t.Dict = {},  # noqa: B006
        content: t.List[str] = [],  # noqa: B006
    ) -> t.Tuple[t.List[Node], t.List[system_message]]:
        text = utils.unescape(text)

        has_explicit_title, title, key = split_explicit_title(text)

        full_url = resource_links[key]

        if not has_explicit_title:
            title = full_url

        pnode = nodes.reference(title, title, internal=False, refuri=full_url)
        return [pnode], []

    return role


def add_link_role(app: Sphinx) -> None:
    app.add_role("resource", make_link_role(app.config.resource_links))


def setup(app: Sphinx) -> t.Dict[str, t.Any]:
    app.add_config_value("resource_links", {}, "env")
    app.connect("builder-inited", add_link_role)
    return {"version": sphinx.__display_version__, "parallel_read_safe": True}
