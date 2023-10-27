"""Console script for kicad_dsn_io."""
import sys
import click
import pcbnew


@click.option("--board", required=True, help="PCBNEW PCB File")
@click.option("--i", help="DSN file to import to board file")
@click.option("--o", help="Output file name")
@click.command()
def main(board, i, o) -> None:
    """Console script for kicad_dsn_io."""
    if i is None:
        if o is None:
            raise UserWarning("Needs either an import or export argument")
        b = pcbnew.LoadBoard(board)
        pcbnew.ExportSpecctraDSN(o)

    else:
        b = pcbnew.LoadBoard(board)
        pcbnew.ImportSpecctraSES(i)
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
