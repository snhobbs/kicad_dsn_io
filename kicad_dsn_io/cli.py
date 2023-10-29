"""Console script for kicad_dsn_io."""
import sys
import click
import pcbnew


@click.option("--board", required=True, help="PCBNEW PCB File")
@click.option("--i", help="SES file to import to board file")
@click.option("--o", help="Output file name (DSN or kicad_pcb)")
@click.command()
def main(board, i, o) -> None:
    """Console script for kicad_dsn_io."""
    if i is None:
        if o is None:
            raise UserWarning("Needs either an import or export argument")
        b = pcbnew.LoadBoard(board)
        resp = pcbnew.ExportSpecctraDSN(b, o)
        assert(resp)
        print(f"Exported {o} from {board}")
    else:
        b = pcbnew.LoadBoard(board)
        resp = pcbnew.ImportSpecctraSES(b, i)
        assert(resp)
        b.Save(o)
        print(f"Imported {i} into {board}")
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
