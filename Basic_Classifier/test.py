import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 设置全局样式
plt.style.use('ggplot')

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(14, 8), dpi=100)

# 生成数据点
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
sin_y = np.sin(x)
cos_y = np.cos(x)
tan_y = np.tan(x)

# 避免正切函数的不连续点
tan_y = np.clip(tan_y, -4, 4)  # 限制y值在[-4, 4]范围内

# 绘制三角函数曲线
sin_line, = ax.plot(x, sin_y, color='#E74C3C', linewidth=2.5, alpha=0.9,
                   label=r'$\sin(x)$', marker='', linestyle='-')
cos_line, = ax.plot(x, cos_y, color='#3498DB', linewidth=2.5, alpha=0.9,
                   label=r'$\cos(x)$', marker='', linestyle='-')
tan_line, = ax.plot(x, tan_y, color='#2ECC71', linewidth=2.5, alpha=0.9,
                   label=r'$\tan(x)$', marker='', linestyle='-')

# 添加渐变色填充
ax.fill_between(x, sin_y, 0, color='#E74C3C', alpha=0.1)
ax.fill_between(x, cos_y, 0, color='#3498DB', alpha=0.1)
ax.fill_between(x, tan_y, 0, color='#2ECC71', alpha=0.1)

# 设置标题和标签
ax.set_title('Trigonometric Functions', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('x (radians)', fontsize=14, labelpad=10)
ax.set_ylabel('f(x)', fontsize=14, labelpad=10)

# 设置x轴刻度（以π为单位）
ax.set_xticks([-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0,
               np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels([r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$',
                   r'$-\frac{\pi}{2}$', '0',
                   r'$\frac{\pi}{2}$', r'$\pi$',
                   r'$\frac{3\pi}{2}$', r'$2\pi$'], fontsize=12)

# 设置y轴刻度和网格
ax.set_yticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
ax.set_yticklabels([-4, -3, -2, -1, 0, 1, 2, 3, 4], fontsize=12)
ax.yaxis.set_minor_locator(MultipleLocator(0.5))

# 添加网格线
ax.grid(True, linestyle='--', alpha=0.7, which='both')
ax.grid(True, linestyle=':', alpha=0.4, which='minor')

# 添加零线
ax.axhline(0, color='black', linewidth=0.8, alpha=0.7)
ax.axvline(0, color='black', linewidth=0.8, alpha=0.7)

# 设置坐标轴范围
ax.set_xlim(-2*np.pi, 2*np.pi)
ax.set_ylim(-4, 4)

# 添加图例
legend = ax.legend(loc='upper right', frameon=True, shadow=True,
                  fontsize=12, framealpha=0.95)
legend.get_frame().set_facecolor('#F8F9F9')

# 添加关键点的注释
key_points = [
    (0, 0, r'$(0, 0)$', '#7F8C8D'),
    (np.pi/2, 1, r'$(\frac{\pi}{2}, 1)$', '#E74C3C'),
    (np.pi, 0, r'$(\pi, 0)$', '#7F8C8D'),
    (3*np.pi/2, -1, r'$(\frac{3\pi}{2}, -1)$', '#3498DB')
]

for x_val, y_val, text, color in key_points:
    ax.plot(x_val, y_val, 'o', markersize=8, color=color)
    ax.annotate(text, (x_val, y_val),
                xytext=(x_val + 0.3, y_val + 0.3),
                fontsize=12, color=color,
                arrowprops=dict(arrowstyle='->', color=color, alpha=0.7))

# 添加数学公式注释
ax.text(0.5, 0.95, r'$\sin(x) = \frac{opposite}{hypotenuse}$',
        transform=ax.transAxes, fontsize=14, color='#E74C3C')
ax.text(0.5, 0.88, r'$\cos(x) = \frac{adjacent}{hypotenuse}$',
        transform=ax.transAxes, fontsize=14, color='#3498DB')
ax.text(0.5, 0.81, r'$\tan(x) = \frac{\sin(x)}{\cos(x)}$',
        transform=ax.transAxes, fontsize=14, color='#2ECC71')

# 添加图表说明
ax.text(0.5, -0.12, 'Figure 1: Trigonometric functions visualization',
        transform=ax.transAxes, fontsize=10, ha='center', color='#7F8C8D')

# 添加边距使图形更美观
plt.tight_layout(pad=3.0)

# 显示图形
plt.show()