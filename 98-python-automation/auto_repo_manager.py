import os
import subprocess
from datetime import datetime
from pathlib import Path

from config import PROJECTS_DIR, AUTO_COMMIT


def get_projects(directory):
    """
    Detect python projects inside the repository.
    A project is defined as a folder containing a .py file.
    """

    projects = []

    for folder in os.listdir(directory):
        path = os.path.join(directory, folder)

        if os.path.isdir(path):

            py_files = [
                f for f in os.listdir(path)
                if f.endswith(".py")
            ]

            if py_files:
                last_modified = datetime.fromtimestamp(
                    os.path.getmtime(path)
                ).strftime("%Y-%m-%d")

                projects.append({
                    "name": folder,
                    "files": py_files,
                    "last_modified": last_modified
                })

    return sorted(projects, key=lambda x: x["name"])


def generate_readme(projects, output_file="PROJECT_INDEX.md"):
    """
    Generate a README index listing all projects.
    """

    content = [
        "# 100 Python Projects Challenge\n",
        "Automatically generated project index.\n\n",
        "## Projects\n"
    ]

    for project in projects:

        content.append(
            f"### {project['name']}\n"
            f"- Python files: {', '.join(project['files'])}\n"
            f"- Last updated: {project['last_modified']}\n\n"
        )

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(content)

    print(f"README generated: {output_file}")


def auto_commit():
    """
    Automatically commit and push changes.
    """

    try:
        subprocess.run(["git", "add", "."], check=True)

        subprocess.run(
            ["git", "commit", "-m", "Auto update project index"],
            check=True
        )

        subprocess.run(["git", "push"], check=True)

        print("Changes committed and pushed.")

    except subprocess.CalledProcessError:
        print("No changes to commit.")


def main():

    print("Scanning projects...")

    projects = get_projects(PROJECTS_DIR)

    print(f"Found {len(projects)} projects.")

    generate_readme(projects)

    if AUTO_COMMIT:
        auto_commit()


if __name__ == "__main__":
    main()