"""CLI to convert a JSON file to BSON."""
import json

import bson
import click

@click.command()
@click.argument('input_file')
@click.argument('output_file')
def tool(input_file, output_file):
    """CLI to evaluate maintainability."""
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)
    with open(output_file, 'wb') as bson_file:
        bson_file.write(bson.dumps(data))
    click.secho(f'Successfully converted {input_file} to BSON: {output_file}.')

if __name__ == '__main__':
    tool() # pylint: disable=no-value-for-parameter
