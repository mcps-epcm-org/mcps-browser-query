import typer
from api_client import APIClient

def query_api(base_url: str, endpoint: str):
    """
    Change me.
    """
    client = APIClient(base_url)
    try:
        result = client.fetch_data(endpoint)
        typer.echo(result.json(indent=4))
    except requests.RequestException as e:
        typer.echo(f"Error en la consulta: {e}", err=True)

app = typer.Typer()
app.command()(query_api)
