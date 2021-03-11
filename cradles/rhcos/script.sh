#!/bin/bash -x

RHCOS_URL="http://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/latest"
RHCOS_ARCHIVE="rhcos-openstack.x86_64.qcow2.gz"
RHCOS_QCOW="rhcos-openstack.x86_64.qcow2"
DOCKERFILE="Dockerfile"


mkdir -p rootfs/disk 
curl -L "${RHCOS_URL}/${RHCOS_ARCHIVE}" | gunzip -c > rootfs/disk/rhcos.qcow2

cat <<EOF >${DOCKERFILE}
FROM scratch
ADD ./rootfs /
EOF

buildah bud -t rhcos:4.7 ./
#podman build -t localhost/rhcos:4.7 -f ${DOCKERFILE}
#rm -rf rootfs/disk/*
