# OpenShift Virtualization Quick Start Resource 

Quick Starts for OpenShift Virtualization (Red Hat OpenShift Opinionated KubeVirt)

### Example build from local source
```sh
./cradle \
  --image-tag='4.7'
  --image-name='localhost/rhcos-openstack' \
  --image-url="${localImagePath}" \
  --cradle-image='scratch' \
```

### Example build from remote source
```sh
./cradle \
  --image-tag='4.7'
  --image-name='localhost/rhcos-openstack' \
  --image-url="${remoteImageUrl}" \
  --cradle-image='registry.access.redhat.com/ubi8/ubi' \
```

### Example Variables:
```sh
export localImagePath="/tmp/rhcos-openstack.x86_64.qcow2"
export remoteImageUrl="http://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/latest/rhcos-openstack.x86_64.qcow2.gz" 
```
---------------------------------------------------------------------
### Glossary
```sh
root@konductor ~$ ./cradle --help
usage: cradle [-h] [--image-name registry.com/namespace/image-name] [--image-tag IMAGE_TAG] [--build-path BUILD_PATH]
              (--image-url https://FQDN/URI/image.qcow2.gz | --image-file /global/path/to/image.qcow2)

KubeVirt Image Cradle Builder to generate OpenShift Virtualization compatible qcow2 import images

optional arguments:
  -h, --help                                          Show this help message
  --cradle-image registry.access.redhat.com/ubi8/ubi  Name of cradle image
  --image-name   registry.com/namespace/image-name    Name of cradle image
  --image-tag    IMAGE_TAG                            Image tag
  --build-path   BUILD_PATH                           Container build context global path
  --image-url    https://FQDN/URI/image.qcow2.gz      Qcow image url
  --image-file   /global/path/to/image.qcow2          Qcow image path
```
