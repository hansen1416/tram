import os

from oss2_uploader import folder_uploader_sync

folder_uploader_sync(
    os.path.join(".", "data"),
    "tram-hlz",
    "oss-ap-southeast-1.aliyuncs.com",
)
