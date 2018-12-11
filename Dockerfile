FROM quay.io/pypa/manylinux1_x86_64

# sadly this is v0.9.8, and the system perl is too old to build openssl from source
RUN yum install -y openssl-devel

COPY hashstate /hashstate
COPY test /test
COPY README.md /README.md
COPY setup.py /setup.py
COPY build_manylinux.sh /build_manylinux.sh

ENTRYPOINT ["/build_manylinux.sh"]
