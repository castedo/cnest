#!/bin/bash
set -o errexit
set -x

if [[ $1 ]]; then
    yum install -y "$1"
else
    yum -y install cnest
fi

