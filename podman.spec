Name:          podman
Version:       0.10.1
Release:       6
Summary:       A daemonless container engine for managing Containers
Epoch:         1
License:       ASL 2.0
URL:           https://podman.io/
Source0:       https://github.com/containers/libpod/archive/e4a155328fb88590fafd3d4e845f9bca49133f62/libpod-e4a1553.tar.gz
BuildRequires: golang btrfs-progs-devel glib2-devel glibc-devel glibc-static
BuildRequires: git go-md2man gpgme-devel libassuan-devel libgpg-error-devel libseccomp-devel
BuildRequires: libselinux-devel ostree-devel pkgconfig make
Requires:      docker-runc containers-common containernetworking-plugins >= 0.7.3-2 iptables nftables conmon
Recommends:    container-selinux >= 2:2.71 slirp4netns

Provides: bundled(golang(github.com/Azure/go-ansiterm)) = 19f72df4d05d31cbe1c56bfc8045c96babff6c7e
Provides: bundled(golang(github.com/blang/semver)) = v3.5.0
Provides: bundled(golang(github.com/boltdb/bolt)) = master
Provides: bundled(golang(github.com/buger/goterm)) = 2f8dfbc7dbbff5dd1d391ed91482c24df243b2d3
Provides: bundled(golang(github.com/BurntSushi/toml)) = v0.2.0
Provides: bundled(golang(github.com/containerd/cgroups)) = 77e628511d924b13a77cebdc73b757a47f6d751b
Provides: bundled(golang(github.com/containerd/continuity)) = master
Provides: bundled(golang(github.com/containernetworking/plugins)) = 1562a1e60ed101aacc5e08ed9dbeba8e9f3d4ec1
Provides: bundled(golang(github.com/containers/image)) = 134f99bed228d6297dc01d152804f6f09f185418
Provides: bundled(golang(github.com/containers/psgo)) = 5dde6da0bc8831b35243a847625bcf18183bd1ee
Provides: bundled(golang(github.com/containers/storage)) = 17c7d1fee5603ccf6dd97edc14162fc1510e7e23
Provides: bundled(golang(github.com/coreos/go-systemd)) = v14
Provides: bundled(golang(github.com/cri-o/ocicni)) = master
Provides: bundled(golang(github.com/cyphar/filepath-securejoin)) = v0.2.1
Provides: bundled(golang(github.com/davecgh/go-spew)) = v1.1.0
Provides: bundled(golang(github.com/docker/distribution)) = 7a8efe719e55bbfaff7bc5718cdf0ed51ca821df
Provides: bundled(golang(github.com/docker/docker)) = 86f080cff0914e9694068ed78d503701667c4c00
Provides: bundled(golang(github.com/docker/docker-credential-helpers)) = d68f9aeca33f5fd3f08eeae5e9d175edf4e731d1
Provides: bundled(golang(github.com/docker/go-connections)) = 3ede32e2033de7505e6500d6c868c2b9ed9f169d
Provides: bundled(golang(github.com/docker/go-units)) = v0.3.2
Provides: bundled(golang(github.com/docker/libtrust)) = aabc10ec26b754e797f9028f4589c5b7bd90dc20
Provides: bundled(golang(github.com/docker/spdystream)) = ed496381df8283605c435b86d4fdd6f4f20b8c6e
Provides: bundled(golang(github.com/fatih/camelcase)) = f6a740d52f961c60348ebb109adde9f4635d7540
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = 7d7316ed6e1ed2de075aab8dfc76de5d158d66e1
Provides: bundled(golang(github.com/fsouza/go-dockerclient)) = master
Provides: bundled(golang(github.com/ghodss/yaml)) = 04f313413ffd65ce25f2541bfd2b2ceec5c0908c
Provides: bundled(golang(github.com/godbus/dbus)) = a389bdde4dd695d414e47b755e95e72b7826432c
Provides: bundled(golang(github.com/gogo/protobuf)) = c0656edd0d9eab7c66d1eb0c568f9039345796f7
Provides: bundled(golang(github.com/golang/glog)) = 23def4e6c14b4da8ac2ed8007337bc5eb5007998
Provides: bundled(golang(github.com/golang/groupcache)) = b710c8433bd175204919eb38776e944233235d03
Provides: bundled(golang(github.com/golang/protobuf)) = 4bd1920723d7b7c925de087aa32e2187708897f7
Provides: bundled(golang(github.com/googleapis/gnostic)) = 0c5108395e2debce0d731cf0287ddf7242066aba
Provides: bundled(golang(github.com/google/gofuzz)) = 44d81051d367757e1c7c6a5a86423ece9afcf63c
Provides: bundled(golang(github.com/gorilla/context)) = v1.1
Provides: bundled(golang(github.com/gorilla/mux)) = v1.3.0
Provides: bundled(golang(github.com/hashicorp/errwrap)) = 7554cd9344cec97297fa6649b055a8c98c2a1e55
Provides: bundled(golang(github.com/hashicorp/golang-lru)) = 0a025b7e63adc15a622f29b0b2c4c3848243bbf6
Provides: bundled(golang(github.com/hashicorp/go-multierror)) = 83588e72410abfbe4df460eeb6f30841ae47d4c4
Provides: bundled(golang(github.com/imdario/mergo)) = 0.2.2
Provides: bundled(golang(github.com/json-iterator/go)) = 1.0.0
Provides: bundled(golang(github.com/kr/pty)) = v1.0.0
Provides: bundled(golang(github.com/mailru/easyjson)) = 03f2033d19d5860aef995fe360ac7d395cd8ce65
Provides: bundled(golang(github.com/mattn/go-runewidth)) = v0.0.1
Provides: bundled(golang(github.com/Microsoft/go-winio)) = 78439966b38d69bf38227fbf57ac8a6fee70f69a
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = 43f9725307998e09f2e3816c2c0c36dc98f0c982
Provides: bundled(golang(github.com/mistifyio/go-zfs)) = v2.1.1
Provides: bundled(golang(github.com/mrunalp/fileutils)) = master
Provides: bundled(golang(github.com/mtrmac/gpgme)) = b2432428689ca58c2b8e8dea9449d3295cf96fc9
Provides: bundled(golang(github.com/Nvveen/Gotty)) = master
Provides: bundled(golang(github.com/opencontainers/image-spec)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/runc)) = b4e2ecb452d9ee4381137cc0a7e6715b96bed6de
Provides: bundled(golang(github.com/opencontainers/runtime-spec)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/runtime-tools)) = master
Provides: bundled(golang(github.com/opencontainers/selinux)) = b6fa367ed7f534f9ba25391cc2d467085dbb445a
Provides: bundled(golang(github.com/openshift/imagebuilder)) = master
Provides: bundled(golang(github.com/ostreedev/ostree-go)) = master
Provides: bundled(golang(github.com/pkg/errors)) = v0.8.0
Provides: bundled(golang(github.com/pmezard/go-difflib)) = 792786c7400a136282c1664665ae0a8db921c6c2
Provides: bundled(golang(github.com/pquerna/ffjson)) = d49c2bc1aa135aad0c6f4fc2056623ec78f5d5ac
Provides: bundled(golang(github.com/projectatomic/buildah)) = 745bf7e56bda740ce7cfc55318da08529e5ed519
Provides: bundled(golang(github.com/seccomp/containers-golang)) = master
Provides: bundled(golang(github.com/seccomp/libseccomp-golang)) = v0.9.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.0.0
Provides: bundled(golang(github.com/spf13/pflag)) = 9ff6c6923cfffbcd502984b8e0c80539a94968b7
Provides: bundled(golang(github.com/stretchr/testify)) = 4d4bfba8f1d1027c4fdbe371823030df51419987
Provides: bundled(golang(github.com/syndtr/gocapability)) = e7cb7fa329f456b3855136a2642b197bad7366ba
Provides: bundled(golang(github.com/tchap/go-patricia)) = v2.2.6
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.4
Provides: bundled(golang(github.com/ulule/deepcopier)) = master
Provides: bundled(golang(github.com/urfave/cli)) = 934abfb2f102315b5794e15ebc7949e4ca253920
Provides: bundled(golang(github.com/varlink/go)) = master
Provides: bundled(golang(github.com/vbatts/tar-split)) = v0.10.2
Provides: bundled(golang(github.com/vishvananda/netlink)) = master
Provides: bundled(golang(github.com/vishvananda/netns)) = master
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = master
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = master
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = master
Provides: bundled(golang(golang.org/x/crypto)) = 81e90905daefcd6fd217b62423c0908922eadb30
Provides: bundled(golang(golang.org/x/net)) = c427ad74c6d7a814201695e9ffde0c5d400a7674
Provides: bundled(golang(golang.org/x/sys)) = master
Provides: bundled(golang(golang.org/x/text)) = f72d8390a633d5dfb0cc84043294db9f6c935756
Provides: bundled(golang(golang.org/x/time)) = f51c12702a4d776e4c1fa9b0fabab841babae631
Provides: bundled(golang(google.golang.org/grpc)) = v1.0.4
Provides: bundled(golang(gopkg.in/cheggaaa/pb.v1)) = v1.0.7
Provides: bundled(golang(gopkg.in/inf.v0)) = v0.9.0
Provides: bundled(golang(gopkg.in/mgo.v2)) = v2
Provides: bundled(golang(gopkg.in/square/go-jose.v2)) = v2.1.3
Provides: bundled(golang(gopkg.in/yaml.v2)) = v2
Provides: bundled(golang(k8s.io/api)) = 5ce4aa0bf2f097f6021127b3d879eeda82026be8
Provides: bundled(golang(k8s.io/apiextensions-apiserver)) = 1b31e26d82f1ec2e945c560790e98f34bb5f2e63
Provides: bundled(golang(k8s.io/apimachinery)) = 616b23029fa3dc3e0ccefd47963f5651a6543d94
Provides: bundled(golang(k8s.io/apiserver)) = 4d1163080139f1f9094baf8a3a6099e85e1867f6
Provides: bundled(golang(k8s.io/client-go)) = 7cd1d3291b7d9b1e2d54d4b69eb65995eaf8888e
Provides: bundled(golang(k8s.io/kube-openapi)) = 275e2ce91dec4c05a4094a7b1daee5560b555ac9
Provides: bundled(golang(k8s.io/utils)) = 258e2a2fa64568210fbd6267cf1d8fd87c3cb86e

Patch1:   0001-podman-patch-for-local-search.patch 

%description
Podman manages the entire container ecosystem which includes pods,
containers, container images, and container volumes using the libpod library. 

%package -n     python3-podman
Summary:        Python 3 bindings and client for podman
BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools python3-varlink
Requires:       python3-setuptools python3-varlink python3-dateutil python3-humanize python3-psutil
Provides:       python3-%{name} = %{version}-%{release}

%description -n python3-podman
The python3-podman package containers a module that allows you to connect to a Podman socket activated systemdservice on the same host or a remote host using a ssh tunnel.

%package -n     python3-pypodman
Summary:        Python 3 tool for podman
BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools python3-varlink
Requires:       python3-setuptools python3-varlink python3-dateutil python3-psutil

%description -n python3-pypodman
Python 3 tool for podman.

%package        docker
Summary:        Docker CLI emulator for podman
BuildArch:      noarch
Requires:       %{name} = %{epoch}:%{version}-%{release}
Conflicts:      docker docker-latest docker-ce docker-ee moby-engine

%description docker
This package installs a script named docker, which emulates the Docker CLI through podman command.

%package help
Summary:        Help document for the podman package
Conflicts:      docker docker-latest docker-ce docker-ee moby-engine

%description help
Help document for the podman package

%prep
%autosetup -Sgit -n libpod-e4a155328fb88590fafd3d4e845f9bca49133f62 -p1
sed -i '/\/bin\/env/d' completions/bash/%{name}
sed -i 's/0.0.0/%{version}/' contrib/python/%{name}/setup.py
sed -i 's/0.0.0/%{version}/' contrib/python/py%{name}/setup.py
mv pkg/hooks/README.md pkg/hooks/README-hooks.md

%build
mkdir _build
cd _build
mkdir -p src/github.com/containers
ln -s ../../../../ src/github.com/containers/libpod
cd -
ln -s vendor src
export GOPATH=$(pwd)/_build:$(pwd):$(pwd):%{gopath}
export BUILDTAGS="varlink selinux seccomp $(hack/btrfs_installed_tag.sh) $(hack/btrfs_tag.sh) $(hack/libdm_tag.sh) exclude_graphdriver_devicemapper"
go generate ./cmd/%{name}/varlink/...
BUILDTAGS=$BUILDTAGS make binaries docs

%install
install -dp %{buildroot}%{_unitdir}
make PREFIX=%{buildroot}%{_prefix} ETCDIR=%{buildroot}%{_sysconfdir} \
        install.bin install.man install.cni install.systemd install.completions install.docker

%{__make} DESTDIR=%{buildroot} install.python

install -Dp -m644 libpod.conf %{buildroot}%{_datadir}/containers/libpod.conf

%global license %doc

%files
%license LICENSE
%doc README.md CONTRIBUTING.md pkg/hooks/README-hooks.md install.md code-of-conduct.md transfer.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/*
%config(noreplace) %{_sysconfdir}/cni/net.d/87-%{name}-bridge.conflist
%{_datadir}/containers/libpod.conf
%{_unitdir}/{io.%{name}.service,io.%{name}.socket}
%{_usr}/lib/tmpfiles.d/%{name}.conf

%files -n python3-podman
%license LICENSE
%doc README.md CONTRIBUTING.md pkg/hooks/README-hooks.md install.md code-of-conduct.md transfer.md
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/*
%{python3_sitelib}/%{name}*.egg-info

%files -n python3-pypodman
%license LICENSE
%doc README.md CONTRIBUTING.md pkg/hooks/README-hooks.md install.md code-of-conduct.md transfer.md
%dir %{python3_sitelib}/py%{name}
%{python3_sitelib}/py%{name}/*
%{python3_sitelib}/py%{name}*.egg-info
%{_bindir}/py%{name}

%files docker
%{_bindir}/docker

%files help
%{_mandir}/man1/{docker*.1*,podman*.1*}
%{_mandir}/man5/*.5*

%changelog
* Mon Feb 8 2021 lingsheng <lingsheng@huawei.com> - 1:0.10.1-6
- Change BuildRequires to golang

* Sat Jan 9 2021 Shengjing Wei <weishengjing1@huawei.com> - 1:0.10.1-5
- Fixed podman pull failed with issue I2BF99

* Wed Sep 9 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 1:0.10.1-4
- Add conflicts with docker-engine for help package

* Thu Mar 12 2020 Ling Yang <lingyang2@huawei.com> - 1:0.10.1-3
- Fixed install fail

* Mon Dec 2 2019 shijian <shijian16@huawei.com> - 1:0.10.1-2
- Package init
