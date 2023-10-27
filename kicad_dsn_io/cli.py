"""Console script for kicad_dsn_io."""
import sys
import click
import pcbnew


@click.command()
@click.argument("--board", required=True, help="PCBNEW PCB File")
@click.argument("-i", help="DSN file to import to board file")
@click.argument("-o", help="Output file name")
def main(board, i, o) -> None:
    """Console script for kicad_dsn_io."""
    b = pcbnew.LoadBoard(board)
    if i is None:
        if o is None:
            raise UserWarning("Needs either an import or export argument")
        pcbnew(board, o)

    else:
        pcbnew.ImportSpecctraSES(i)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
