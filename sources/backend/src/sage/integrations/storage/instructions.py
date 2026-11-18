from google.cloud import storage

from sage.config import get_app_config


def read_instructions() -> str:
    config = get_app_config()
    client = storage.Client(project=config.project_id)
    bucket = client.bucket(f"{config.resource_prefix}-instructions")
    return bucket.blob("istruzioni.md").download_as_text(
        encoding="utf-8", timeout=10
    )