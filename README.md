[![OneView Logo](https://one-view.ai/wp-content/themes/ov/assets/images/oneview-logo@2x.png)](https://one-view.ai/)
# Readable PTH 

[![Upload Python Package](https://github.com/oneview-space/readablePTH/actions/workflows/release.yml/badge.svg)](https://github.com/oneview-space/readablePTH/actions/workflows/release.yml)
[![GitHub license](https://img.shields.io/github/license/oneview-space/readablePTH?style=plastic)](https://github.com/oneview-space/readablePTH/blob/master/LICENSE)

## About this project
Make pth readable. \
This project can write json file from pth and can write the pth again from the json. \
model.pth <--> model.json

#### Limitation
model.pth must be the state_dict of a Pytorch model:
`torch.save(model.state_dict(), 'model.pth')`

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
rpth decode -i test/models/model_small.pth -o test/models/model_small.json 
```

### encode from json to pth
```bash
rpth encode -i test/models/model_small.json -o test/models/model_small_restored.pth
```

## Test
For testing with small model run:
```bash
cd test
python test_small_net.py
```

# TODO:
- [ ] Add the ability to use any torch version 
- [ ] Add args to map_location (CPU/GPU) when writing pth file
- [ ] Add compare state_dict or json methods for checking results

