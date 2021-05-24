[![OneView Logo](https://one-view.ai/wp-content/themes/ov/assets/images/oneview-logo@2x.png)](https://one-view.ai/)
# Readable PTH 

[![Upload Python Package](https://github.com/oneview-space/readablePTH/actions/workflows/release.yml/badge.svg)](https://github.com/oneview-space/readablePTH/actions/workflows/release.yml)
[![GitHub license](https://img.shields.io/github/license/oneview-space/readablePTH?style=plastic)](https://github.com/oneview-space/readablePTH/blob/master/LICENSE)

## About this project
Make pth readable. \
model.pth <--> model.json

## Installation
```bash
pip install readablePTH
```

### For develop
Please clone the project
```bash
git clone https://github.com/oneview-space/readablePTH.git
```
And then install
```bash
cd readablePTH
pip install -e .
```

## Usage

*For now this is only working with [`encode`, `decode`] commands*

### decode from pth to json
```bash
rpth decode -i model.pth -o model.json 
```

### encode from json to pth
```bash
rpth encode -i model.json -o model.pth 
```


# TODO:
- [ ] Add the ability to use any torch version 
- [ ] add args to map_location (CPU/GPU) when writing pth file
