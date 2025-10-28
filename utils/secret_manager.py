from google.cloud import secretmanager


def get_secret(
    secret_id: str, project_id: str = "porygon-pipelines", version_id: str = "latest"
) -> str:
    """
    Retrieve a secret from Google Cloud Secret Manager.

    Args:
        project_id (str): The GCP project ID
        secret_id (str): The name of the secret
        version_id (str): The version of the secret (default: "latest")

    Returns:
        str: The secret value as a string

    Raises:
        Exception: If the secret cannot be retrieved
    """
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
