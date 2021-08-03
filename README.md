# Quick assemble kit

Quick assemble kit is a too which customized iso image from IronOS.

<img src="images/Quick_assemble_kit.png" height="80%" width="50%">

## Build

* Python
* Shell script
* YAML

## Jenkins

<img src="images/Jenkins.png" height="50%" width="50%">

## Installation

```bash
yum install wget -y
yum install squashfs-tools -y
yum install mkisofs -y
yum install python3 -y

pip3 install wget
pip3 install shortuuid
pip3 install pyyaml
```

## Usage

Write yaml file first.

Execute bundle_manager.py
```bash
python3 bundle_builder.py
```



