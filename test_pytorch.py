import torch
print("PyTorch imported successfully!")
print(f"Version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

# Test creating a tensor
x = torch.rand(3, 3)
print("Sample tensor:")
print(x)