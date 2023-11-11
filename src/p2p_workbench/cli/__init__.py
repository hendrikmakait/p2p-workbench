# SPDX-FileCopyrightText: 2023-present Hendrik Makait <hendrik@coiled.io>
#
# SPDX-License-Identifier: MIT
import click

from p2p_workbench.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="P2P Workbench")
def p2p_workbench():
    click.echo("Hello world!")
