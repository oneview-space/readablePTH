from collections import OrderedDict
import torch
from json_tricks import dumps


def _tensor_to_numpy(dictionary):
    if type(dictionary) == torch.Tensor:
        return dictionary.numpy()
    elif type(dictionary) == dict or type(dictionary) == OrderedDict:
        d = {k: _tensor_to_numpy(v) for k, v in dictionary.items()}
        return d
    return dictionary


def pth_to_json(pth_path, output_path):
    print("Reading pth file")
    dic = torch.load(pth_path, map_location='cpu')
    dic_numpy = _tensor_to_numpy(dic)
    print("Writing json file")
    with open(output_path, 'w') as f:
        f.write(dumps(dic_numpy))
    print(f"Saved in {output_path}")
