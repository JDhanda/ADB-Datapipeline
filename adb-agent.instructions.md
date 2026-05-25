# ADB Agent for Data Pipeline Notebooks and Jobs

This agent is designed to help maintain and extend Azure Databricks notebook-based data pipelines in this repository.

## Responsibilities

- create and validate ADB notebooks
- define Databricks job JSON and job clusters
- package notebook assets and deploy them to ADB workspaces
- manage dev/prod deployment workflows with environment approvals
- integrate GitHub Actions CI for linting, unit tests, and security scans
- integrate CD to Azure Key Vault and Databricks token-based deployment

## How to use

- edit notebooks in `notebooks/`
- add job definitions to `jobs/`
- update deployment settings in `workspace-config/adb_variables.yml`
- use `scripts/deploy_adb_workspace.py` to package and deploy the workspace

## Recommended workflow

1. update notebook logic
2. update or add job definition
3. run local unit tests:

```bash
python -m pytest tests
```

4. push code and allow CI to run
5. deploy to dev with GitHub Actions
6. promote to prod through the protected `prod` environment approval
