from collections import OrderedDict
import torch
import numpy as np
from json_tricks import loads


def _numpy_to_tensor(dictionary):

    if type(dictionary) == np.ndarray:
        return torch.from_numpy(dictionary)
    elif type(dictionary) == dict or type(dictionary) == OrderedDict:
        d = type(dictionary)({k: _numpy_to_tensor(v) for k, v in dictionary.items()})
        return d
    return dictionary


def json_to_pth(json_path, output_path):
    print("Reading json file")
    with open(json_path, 'r') as f:
        string_back = f.read()
    dic_back = loads(string_back)
    dic_tensor = _numpy_to_tensor(dic_back)
    print("Writing pth file")
    torch.save(dic_tensor, output_path)
    print(f"Saved in {output_path}")
