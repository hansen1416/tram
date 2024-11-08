import os
import os
import sys
import pathlib
from typing import List

import tqdm
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider


def folder_uploader_sync(folder_path, bucket_name, oss_endpoint):

    folder_path = os.path.abspath(folder_path)

    if not os.path.exists(folder_path):
        print(f"{folder_path} does not exist")
        sys.exit(1)

    path_delimiter = os.path.sep
    all_oos_path = []

    # get all files in the folder recursively
    all_files: List[str] = [
        str(f) for f in pathlib.Path(folder_path).rglob("*") if f.is_file()
    ]

    for filepath in all_files:

        # remove the prefix `folder_path` from the file path
        sub_path = filepath[len(folder_path) + 1 :]

        all_oos_path.append("/".join(sub_path.split(path_delimiter)))

    # create a bucket
    auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
    bucket = oss2.Bucket(auth, oss_endpoint, bucket_name, connect_timeout=30)

    print(f"Total files to upload: {len(all_files)}")

    # upload all files
    for i, filepath in enumerate(tqdm.tqdm(all_files, desc="Uploading files")):
        if not os.path.isfile(filepath):
            continue

        target_path = all_oos_path[i]

        # check if the file already exists in oss
        if bucket.object_exists(target_path):
            # print(f"{self.process_idx}: {target_path} already exists in oss")
            continue

        bucket.put_object_from_file(
            target_path,
            filepath,
        )


folder_uploader_sync(
    os.path.join(".", "data"),
    "tram-hlz",
    "oss-ap-southeast-1.aliyuncs.com",
)
