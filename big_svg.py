from io import BufferedWriter
import click
from pathlib import Path
import re
import logging
import humanfriendly

logging.basicConfig(level=logging.DEBUG)


def add_garbage(file: BufferedWriter, total_bytes: int) -> None:
    one_mb_of_data = b"*" * 1024 * 1024
    written = 0
    file.write(b"\n<!-- ")
    while written < total_bytes:
        file.write(one_mb_of_data)
        written += len(one_mb_of_data)
    file.write(b" -->\n")


@click.command()
@click.option("--input-name", type=str, prompt="Input File Name.")
@click.option("--output-name", type=str, prompt="Output File Name.")
@click.option("--size", type=str, prompt="Desried target size.")
def main(input_name: str, output_name, size: str) -> None:
    original_xml = Path(input_name).read_text()
    parsed_size = humanfriendly.parse_size(size)
    split = re.split(r"(<path.*)", original_xml, flags=re.I | re.M | re.A, maxsplit=1)
    if len(split) != 3:
        logging.error("Can't read the svg file")
        return
    with Path(output_name).open("wb") as output_file:
        output_file.write(split[0].encode())
        add_garbage(output_file, parsed_size)
        output_file.write(split[1].encode())
        output_file.write(split[2].encode())
    logging.info(f"{size} of garbage was written to {output_name}.")


if __name__ == "__main__":
    main()
