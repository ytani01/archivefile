#
# (c) 2025 Yoichi Tanibayashi
#
import click
from pyclickutils import click_common_opts, get_logger

from . import ArchiveFiles, __version__


class HelpOnErrorCommand(click.Command):
    def parse_args(self, ctx, args):
        try:
            return super().parse_args(ctx, args)
        except (
            click.exceptions.BadOptionUsage,
            click.exceptions.NoSuchOption,
            click.exceptions.BadParameter,
            click.FileError,
        ) as e:
            click.echo(f"Error: {e}\n", err=True)
            click.echo(ctx.get_help(), err=True)
            ctx.exit(2)


@click.command(cls=HelpOnErrorCommand, no_args_is_help=True)
@click.argument("src_files", type=click.Path(), nargs=-1)
@click.option(
    "--stat", "-s", type=str, default="done", show_default=True, help="status"
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    default=False,
    show_default=True,
    help="verbose flag",
)
@click.option(
    "--dstdir",
    "-d",
    type=str,
    default="./archives",
    show_default=True,
    help="destination directory",
)
@click_common_opts(click, __version__, use_d=False, use_v=False)
def main(ctx, src_files, stat, dstdir, verbose, debug):
    """指定されたファイルをアーカイブディレクトリに移動し、リネーム。"""
    log = get_logger(__name__, debug)
    log.debug("command name = %a", ctx.command.name)
    log.debug(
        "src_files=%s, stat = %a, dstdir = %s, verbose=%s",
        src_files,
        stat,
        dstdir,
        verbose,
    )

    if not src_files:
        print(ctx.get_help())
        return

    app = ArchiveFiles(src_files, stat, dstdir, verbose, debug=debug)

    try:
        app.archive_files()
    finally:
        log.debug("finish")


if __name__ == "__main__":
    main()
