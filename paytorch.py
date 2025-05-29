import torch

# Verifica que PyTorch está instalado
print("PyTorch version:", torch.__version__)

# Verifica si la GPU está disponible
print("CUDA disponible:", torch.cuda.is_available())

# Si hay GPU, haz una prueba en ella
if torch.cuda.is_available():
    x = torch.rand(3, 3).cuda()
    print("Tensor en GPU:\n", x)
else:
    x = torch.rand(3, 3)
    print("Tensor en CPU:\n", x)
