import os
import sys
from train import train
from utils import plot_losses
import torch

current_cwd = os.getcwd()
src_path = '/'.join(current_cwd.split('/')[:-1])
sys.path.append(src_path)

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

print(device)

g_losses_epoch, d_losses_epoch, d_gp_losses_epoch = train()

# plot_losses(g_losses_epoch, d_losses_epoch, d_gp_losses_epoch)
