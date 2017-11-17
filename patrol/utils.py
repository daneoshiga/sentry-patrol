import click
import decimal
import json


def json_encode_decimal(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    raise TypeError(repr(obj) + " is not JSON serializable")


def print_json(data):
    return click.echo(json.dumps(data, default=json_encode_decimal, indent=2))
