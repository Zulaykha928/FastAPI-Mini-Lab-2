
import typer
import requests

app = typer.Typer()

@app.command()
def users():
    response = requests.get(
        "http://127.0.0.1:8000/users",
        timeout=10
    )

    if response.status_code == 200:
        for user in response.json():
            print(user["name"])
    else:
        print("Could not get users.")

if __name__ == "__main__":
    app()
