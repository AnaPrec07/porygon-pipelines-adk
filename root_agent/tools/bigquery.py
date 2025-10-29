from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from google.oauth2 import service_account
from google.auth.transport.requests import Request


def get_bigquery_toolset() -> BigQueryToolset:
    """Creates and returns a BigQueryToolset with blocked write mode."""

    # Define a tool configuration to block any write operations
    tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

    SCOPES = [
        "https://www.googleapis.com/auth/bigquery",
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/generative-language",
    ]

    # Retrieve service account credentials from secret manager.
    service_account_secret = "config/credentials/service_account.json"
    # get_secret(secret_id="credentials-sa")

    # Configure credentials for service account.
    credentials = service_account.Credentials.from_service_account_file(
        service_account_secret, scopes=SCOPES
    )

    # This is necessary to generate a token.
    credentials.refresh(Request())

    # Define a credentials config using service account JSON file
    credentials_config = BigQueryCredentialsConfig(credentials=credentials)

    # Instantiate a BigQuery toolset
    bigquery_toolset = BigQueryToolset(
        credentials_config=credentials_config, bigquery_tool_config=tool_config
    )
    return bigquery_toolset
