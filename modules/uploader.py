"""YouTube uploader helper.

Provides a single `upload_video` function. Imports from the Google
libraries are done lazily inside the function so importing this module
doesn't fail if the optional dependencies are not yet installed.
"""

from typing import List


def upload_video(video_path: str, title: str, description: str, tags: List[str]):
    """Upload a video to YouTube using OAuth2 credentials from
    `client_secret.json`.

    This function performs the OAuth flow in the console and then
    uploads the given file. It raises an informative ImportError if
    required packages are missing.
    """

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload
    except Exception as e:  # pragma: no cover
        raise ImportError(
            "Missing Google API libraries. Install with: ``pip install google-auth-oauthlib google-api-python-client``"
        ) from e

    scopes = ["https://www.googleapis.com/auth/youtube.upload"]

    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes)
    credentials = flow.run_console()

    youtube = build("youtube", "v3", credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": "27",
            },
            "status": {"privacyStatus": "private"},
        },
        media_body=MediaFileUpload(video_path),
    )

    response = request.execute()
    print("Upload complete:", response)
