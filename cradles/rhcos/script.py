#!/usr/bin/env python3

import os
import sys
import gzip
import tempfile
import argparse
import subprocess
import urllib.request
#from io import StringIO
#from io import BytesIO
#from pathlib import Path
#from tempfile import NamedTemporaryFile


# Define Mandatory & Optional CLI Flags
parser = argparse.ArgumentParser(
    description='KubeVirt Image Cradle Builder to generate OpenShift Virtualization compatible qcow2 import images')
parser.add_argument(
    "--image-name",
    default="localhost/cradle",
    help="Name of cradle image",
    metavar="registry.com/namespace/image-name",
    required=True)
parser.add_argument(
    "--image-tag",
    default="latest",
    help="Image tag",
    metavar="IMAGE_TAG",
    required=False)
parser.add_argument(
    "--build-path",
    default=(os.getcwd()),
    help="Container build context global path",
    required=False)


group = parser.add_mutually_exclusive_group(
    required=True)
group.add_argument(
    "--image-url",
    help="qcow image url",
    metavar="https://FQDN/URI/image.qcow2.gz",
    default="",
    required=False)
group.add_argument(
    "--image-file",
    help="qcow image path",
    metavar="/global/path/to/image.qcow2",
    default="",
    required=False)


# Parse cli arguments
args                     = parser.parse_args()


# Base Variables
cradle_tag               = args.image_tag
cradle_name              = args.image_name
build_path               = args.build_path
container_build_cmd      = "podman build"
qcow2_image_staging_path = ( build_path + "/rootfs/disk/image.qcow2" )


# Stage Qcow2 Image File
def StageImageFile(args, build_path):
    print( ">> Staging Image: " + args.image_file )

# Download Image from URL
def DownloadImageFile(args, build_path):
    download_url = (args.image_url)
    print( ">> Downloading Image: " + args.image_url )
    try:
        with urllib.request.urlopen(download_url) as image_gzip:
            with gzip.GzipFile(fileobj=image_gzip) as archive:
                archive_content = archive.read()
            with open(qcow2_image_staging_path, 'wb') as image:
                image.write(archive_content)
                return 0
    except Exception as e:
        print(e)
        return 1


# Build Disk Image Cradle Container
def PodmanBuildCradle(container_build_cmd, cradle_name, cradle_tag, build_path):
    subprocess.run(
        container_build_cmd + " -t " + cradle_name + ":" + cradle_tag + " " + build_path,
        shell=True, check=True
    )


def main():
    print( ">> Automated KubeVirt Qcow2 Image Cradle Container Builder" )
    print( ">> Building Cradle from directory: " + build_path )
    if args.image_url != "":
      DownloadImageFile(args, build_path)
    if args.image_file != "":
      StageImageFile(args, build_path)
    PodmanBuildCradle(container_build_cmd, cradle_name, cradle_tag, build_path)


if __name__ == "__main__":
    main()
