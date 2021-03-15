# OpenShift Virtualization Quick Start Resource 
Quick Starts for OpenShift Virtualization (Red Hat OpenShift Opinionated KubeVirt)

### Example build from local source
```sh
./cradle --image-file ${localImagePath} --image-name 'localhost/rhcos-openstack' --image-tag '4.7'
```

### Example build from remote source
```sh
./cradle --image-url ${remoteImageUrl} --image-name 'localhost/rhcos-openstack' --image-tag '4.7'
```

### Example Variables:
```
export localImagePath="/tmp/rhcos-openstack.x86_64.qcow2"
export remoteImageUrl="http://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/latest/latest/rhcos-openstack.x86_64.qcow2.gz" 
```
