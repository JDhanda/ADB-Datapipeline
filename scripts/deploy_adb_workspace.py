import os
import sys
import json
import subprocess
from pathlib import Path

CONFIG_FILE = Path(__file__).resolve().parent.parent / "workspace-config" / "adb_variables.yml"

ENV_SETTINGS = {
    "dev": {
        "host": os.getenv("DATABRICKS_HOST_DEV"),
        "token": os.getenv("DATABRICKS_TOKEN_DEV"),
    },
    "prod": {
        "host": os.getenv("DATABRICKS_HOST_PROD"),
        "token": os.getenv("DATABRICKS_TOKEN_PROD"),
    },
}


def deploy(environment: str) -> int:
    env = ENV_SETTINGS.get(environment)
    if not env or not env["host"] or not env["token"]:
        print("ERROR: Missing Databricks host or token for environment:", environment)
        return 1

    notebook_source = Path(__file__).resolve().parent.parent / "notebooks" / "sample_datapipeline.ipynb"
    workspace_dir = f"/Repos/adb-user/ADB-Datapipeline/notebooks"
    print(f"Deploying notebook to {environment} workspace: {workspace_dir}")

    cmd = [
        "databricks",
        "workspace",
        "import",
        str(notebook_source),
        f"{workspace_dir}/sample_datapipeline.ipynb",
        "--format=JUPYTER",
        "--overwrite",
    ]

    env_vars = os.environ.copy()
    env_vars["DATABRICKS_HOST"] = env["host"]
    env_vars["DATABRICKS_TOKEN"] = env["token"]

    print("Running Databricks import command...")
    result = subprocess.run(cmd, env=env_vars)
    if result.returncode != 0:
        print("Notebook deployment failed.")
        return result.returncode

    job_payload = {
        "name": "sample-data-pipeline-notebook-job",
        "existing_cluster_id": "ADB_CLUSTER_ID_PLACEHOLDER",
        "notebook_task": {
            "notebook_path": "/Repos/adb-user/ADB-Datapipeline/notebooks/sample_datapipeline",
        },
        "max_retries": 1,
        "timeout_seconds": 3600,
    }

    print("Creating or updating Databricks job...")
    job_json = Path(__file__).resolve().parent.parent / "jobs" / "sample_adb_job.json"
    job_json.write_text(json.dumps(job_payload, indent=2))
    print(f"Wrote job definition to {job_json}")

    # Example placeholder: actual API integration would be here.
    print("Deployment complete. Review the saved job definition and deploy with Databricks CLI or API.")
    return 0


def main() -> int:
    environment = os.getenv("TARGET_ENV", "dev")
    return deploy(environment)


if __name__ == "__main__":
    raise SystemExit(main())
