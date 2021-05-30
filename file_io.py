import numpy as np
import open3d as o3d
import pandas as pd
from pyntcloud import PyntCloud
import matplotlib.pyplot as plt


def Point_Cloud_Show(points):
    fig = plt.figure(dpi=150)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], cmap='spectral', s=2, linewidths=0, alpha=1, marker=".")
    plt.title('Point Cloud')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


if __name__ == '__main__':
    # txt
    # data = np.genfromtxt(fname=r"data/bed_0053.txt", delimiter=",")
    # point_cloud_raw = pd.DataFrame(data[:, 0:3])
    # point_cloud_raw.columns = ['x', 'y', 'z']
    # point_cloud_pynt = PyntCloud(point_cloud_raw)
    # data = point_cloud_pynt.to_instance("open3d", mesh=False)
    # o3d.visualization.draw_geometries([data])

    # std格式
    # TODO 读入stl格式数据
    mesh = o3d.io.read_triangle_mesh("data/dental_0173.stl")
    # TODO 写为ply格式数据
    o3d.io.write_triangle_mesh("data/output/test_out.ply", mesh)
    # 为什么不直接使用  o3d.io.read_point_cloud() 读入点云数据
    # 不支持stl格式, 具体支持格式参见3表

    # data = np.genfromtxt(fname=r"data/bed_0053.txt", delimiter=",")[:, :3]
    # Point_Cloud_Show(data)
