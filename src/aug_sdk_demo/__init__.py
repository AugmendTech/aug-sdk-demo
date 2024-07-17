import sys
import os
import dotenv

from aug_sdk.video import AugmendVideoClient

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m aug-sdk-demo <video-filename>")
        return 1
    video_file = sys.argv[1]
    if not os.path.exists(video_file):
        print(f"Could not find file: {video_file}")
        return 1
    dotenv.load_dotenv()
    api_key = os.environ.get("AUGMEND_API_KEY")
    root_host = os.environ.get("ROOT_HOST", "https://augmend.com")
    video_client = AugmendVideoClient(api_key=api_key, root_host=root_host, log_callback=print)

    wid = video_client.upload_video(video_file)
    print(f"Workspace ID is: {wid}")
    for doc_type in ["steps", "synopsis", "title"]:
        print(f"Document type: {doc_type}")
        doc = video_client.get_document(wid, doc_type)
        print(f"Type of doc is: {type(doc)}")
        print(doc)
    return 0