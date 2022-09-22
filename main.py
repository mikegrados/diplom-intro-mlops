import os
import typer
import pandas as pd
from uuid import uuid4
from datetime import datetime
from pathlib import Path


PATH = str(Path.cwd())
PATH_TO_DATA = f"{PATH}/data/"


app = typer.Typer(add_completion=False)


@app.command("create")
def create_list(name: str = typer.Option("Unnamed", "-n", "--name")):

    """Create a new todo list"""

    existing_lists = os.listdir(PATH_TO_DATA)

    if f"{name}.csv" in existing_lists:
        print(
            "There is already a todo list with this name. Try again with another name"
        )

    else:
        df = pd.DataFrame(columns=["id", "summary", "status", "owner"])
        df.to_csv(f"{PATH_TO_DATA}{name}.csv", index=False)
        print(f"Todo list {name} successfully created!")


@app.command("show")
def show_lists():

    """Shows all existing todo lists"""

    existing_lists = os.listdir(PATH_TO_DATA)
    for ls in existing_lists:
        print(ls)


@app.command("add")
def add_task(
    list_name: str = typer.Option("-n", "--name"),
    summary: str = typer.Option("-d", "--description"),
    owner: str = typer.Option(None, "-o", "--owner"),
):

    """Add a task to a given todo list"""

    new_row = {
        "id": datetime.now().strftime("%Y-%m-%d %H-%M-%S-") + str(uuid4()),
        "summary": summary if summary else None,
        "status": "todo",
        "owner": owner,
    }

    df = pd.read_csv(f"{PATH_TO_DATA}{list_name}.csv")
    df = df.append(new_row, ignore_index=True)
    df.to_csv(f"{PATH_TO_DATA}{list_name}.csv", index=False)


@app.command("update")
def update_task(
    list_name: str = typer.Option("-n", "--name"),
    id: str = typer.Option("-i", "--id"),
    field: str = typer.Option("-f", "--field"),
    change: str = typer.Option("-c", "--change"),
):

    """Update a task in a given todo list"""

    df = pd.read_csv(f"{PATH_TO_DATA}{list_name}.csv")
    df.loc[df["id"] == id, field] = change
    df.to_csv(f"{PATH_TO_DATA}{list_name}.csv", index=False)


if __name__ == "__main__":
    app()
