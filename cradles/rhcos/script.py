#!/usr/bin/env python3

import os
import sys
import gzip
import tempfile
import argparse
import subprocess
import urllib.request

from io import StringIO
from io import BytesIO
from pathlib import Path
from tempfile import NamedTemporaryFile

run_path = os.path.realpath(__file__)
rhcos_archive_openstack = "rhcos-openstack.x86_64.qcow2.gz"
rhcos_download_url = "http://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/latest"
podman_build_args = "podman build -t rhcos:4.7"


def main():
    DownloadRHCOS(rhcos_download_url, rhcos_archive_openstack)
    PodmanBuildCradle(podman_build_args, run_path)


def PodmanBuildCradle(podman_build_args, run_path):
    print( ">> Building Cradle from: " + run_path )
    subprocess.run(podman_build_args + run_path, shell=True, check=True)


def DownloadRHCOS(rhcos_download_url, rhcos_archive_openstack):
    download_url = urllib.request.urlopen(rhcos_download_url + rhcos_archive_openstack)
    rhcos_image = rhcos_archive_openstack[:-3]
    print("Downloading RHCOS from: " + download_url)
    try:
        with urlopen(download_url) as archive_file:
            with gzip.GzipFile(fileobj=archive_file) as archive:
                archive_content = uncompressed.read()

            with open(out_file, 'wb') as image:
                image.write(archive_content)
                return 0
        
    except Exception as e:
        print(e)
        return 1



if __name__ == "__main__":
    main()
