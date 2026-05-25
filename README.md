# ADB Data Pipeline

This repository contains a sample Azure Databricks (ADB) data pipeline with:

- sample notebook in `notebooks/sample_datapipeline.ipynb`
- sample job definition in `jobs/sample_adb_job.json`
- deployment script in `scripts/deploy_adb_workspace.py`
- CI workflow for linting, unit testing, and security scanning
- CD workflow for deployment to dev and prod with environment approvals
- workspace variable configuration in `workspace-config/adb_variables.yml`
- agent guidance in `adb-agent.instructions.md`

## Available workflows

- `.github/workflows/ci.yml`: CI pipeline for code quality, tests, and security scan
- `.github/workflows/cd.yml`: CD pipeline for packaging and deploying ADB workspace assets

## Setup

1. Install Python dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

2. Configure GitHub secrets:

- `AZURE_CREDENTIALS`
- `AZURE_KEY_VAULT_URI`
- `DEV_PAT`
- `PROD_PAT`
- `DATABRICKS_HOST_DEV`
- `DATABRICKS_HOST_PROD`
- `DATABRICKS_TOKEN_DEV`
- `DATABRICKS_TOKEN_PROD`

3. Set GitHub environments:

- `dev`
- `prod`

Use `prod` environment protection to require manual approval for production deploys.

## Deployment

The CD workflow deploys the ADB workspace and job definition using GitHub Actions and Azure Key Vault secrets.

```bash
gh workflow run cd.yml --field environment=dev
```

For a production release, use `prod` with manual approval and change request support.
