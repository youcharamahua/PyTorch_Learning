import torch
from torchvision import datasets, transforms
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# 设置 Numpy 和 PyTorch 的打印选项，确保控制台输出完整不省略
np.set_printoptions(threshold=np.inf, linewidth=200, formatter={'float': '{: 0.4f}'.format})
torch.set_printoptions(threshold=float('inf'), linewidth=200, sci_mode=False)

def main():
    # 获取当前脚本所在的绝对路径
    # 用户指出数据在 MNIST_handwriting\MNIST\raw
    # torchvision.datasets.MNIST 的 root 参数应该指向包含 MNIST 文件夹的父目录
    # 即 d:\...\MNIST_handwriting
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"正在加载 MNIST 数据...")
    print(f"数据根目录 (root): {current_dir}")
    print(f"预期数据路径: {os.path.join(current_dir, 'MNIST', 'raw')}")

    # 1. 加载原始数据 (Raw)
    # transform=None，Dataset 会返回原始的 PIL Image
    # download=False 表示不下载，直接使用现有数据
    try:
        dataset_raw = datasets.MNIST(root=current_dir, train=True, download=False, transform=None)
    except RuntimeError as e:
        print(f"\n错误: 无法加载数据。请确认数据文件位于 '{os.path.join(current_dir, 'MNIST', 'raw')}'")
        print(f"详细错误: {e}")
        return

    # 2. 加载处理后的数据 (Transformed)
    # 使用与 Notebook 中相同的 transform
    transform = transforms.Compose([
        transforms.Pad(2),               # 28 -> 32
        transforms.ToTensor(),           # [0,255] -> [0.0,1.0]
        transforms.Normalize((0.1307,), (0.3081,)) # (x-mean)/std
    ])
    dataset_trans = datasets.MNIST(root=current_dir, train=True, download=False, transform=transform)

    # 获取第 0 个样本
    idx = 0
    img_raw, label = dataset_raw[idx]       # img_raw 是 PIL.Image
    img_trans, label_t = dataset_trans[idx] # img_trans 是 Tensor

    print(f"\n{'='*40}")
    print(f"样本索引: {idx}, 标签: {label}")
    print(f"{'='*40}")

    # --- 打印原始数据 ---
    print("\n[1] 原始数据 (PIL Image)")
    print(f"尺寸: {img_raw.size} (W, H)")
    print(f"模式: {img_raw.mode}")
    
    # 转 numpy 打印像素矩阵
    arr_raw = np.array(img_raw)
    print(f"\n原始像素内容 (28x28, uint8):\n")
    print(arr_raw)

    # --- 打印 Transform 后数据 ---
    print("\n" + "-"*40)
    print("\n[2] Transform 后数据 (Tensor)")
    print(f"形状: {img_trans.shape} (C, H, W)")
    print(f"数据类型: {img_trans.dtype}")
    print(f"\n处理后像素内容 (1x32x32, float32, Normalized):\n")
    print(img_trans.numpy())

    # --- 可视化 ---
    print("\n正在启动可视化窗口...")
    
    # 使用 Matplotlib 创建一个单独的窗口来展示对比
    # 左边放原始 PIL 图片，右边放处理后的 Tensor
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    fig.canvas.manager.set_window_title('MNIST Data Inspection')

    # 1. 绘制原始图片
    axes[0].imshow(img_raw, cmap='gray')
    axes[0].set_title(f"Original (PIL)\nSize: {img_raw.size}")
    axes[0].axis('off')

    # 2. 绘制处理后的图片
    # Tensor 维度是 (1, 32, 32)，imshow 需要 (32, 32)
    # 注意：数据经过 Normalize，包含负数。imshow 会自动处理显示范围。
    img_trans_np = img_trans.squeeze().numpy()
    axes[1].imshow(img_trans_np, cmap='gray')
    axes[1].set_title(f"Transformed (Tensor)\nShape: {img_trans.shape}\n(Pad=2, Normalized)")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
