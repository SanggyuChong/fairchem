import torch
ff = "/home/chong/.cache/fairchem/models--facebook--UMA/snapshots/abaa274e3612b2cfcc5be2d900ffa2a03cb42ee7/checkpoints/uma-s-1.pt"
ckpt = torch.load(ff, map_location="cpu", weights_only=False)
print(ckpt)

