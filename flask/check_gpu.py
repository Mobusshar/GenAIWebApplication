import torch
from pynvml import *

nvmlInit()
handle = nvmlDeviceGetHandleByIndex(0)
info = nvmlDeviceGetMemoryInfo(handle)

print(f"PyTorch: {torch.__version__}")
print(f"CUDA: {torch.version.cuda}")
print(f"VRAM Total: {info.total/1024**3:.1f}GB")
print(f"VRAM Free: {info.free/1024**3:.1f}GB")