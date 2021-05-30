import open3d as o3d

import numpy as np


if __name__ == '__main__':
    pcd = o3d.io.read_point_cloud("copy_of_tooth.ply")

    """
    // 可以这样将数据转到 numpy 上处理
    points = np.asarray(pcd.points)
    mask = your_plane_test(points) # this function could compute the distance to your plane and threshold it
    pcd.points = o3d.utility.Vector3dVector(points[mask])
    """

    # Tuple[numpy.ndarray[float64[4, 1]], List[int]]
    res = pcd.segment_plane(distance_threshold=0.02, ransac_n=14, num_iterations=500)
    a, b, c, d = res[0]
    inlier_cloud = pcd.select_by_index(res[1])
    inlier_cloud.paint_uniform_color([0, 1.0, 0])
    kd = o3d.geometry.KDTreeFlann(pcd)
    # 可视化显示
    for i in res[1]:
        # 选点
        [k, idx, _] = kd.search_knn_vector_3d(pcd.points[i], 11000)
        # 变色
        np.asarray(pcd.colors)[idx[1:], :] = [236/256, 222/256, 215/256]  # 将这些点变色

    o3d.visualization.draw_geometries([pcd], zoom=0.5599,
                                      front=[-0.4958, 0.8229, 0.2773],
                                      lookat=[2.1126, 1.0163, -1.8543],
                                      up=[0.1007, -0.2626, 0.9596])

    outlier_cloud = pcd.select_by_index(res[1], invert=True)
    outlier_cloud.paint_uniform_color([179 / 256, 49 / 256, 52 / 256])

    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
    #print(res)
    o3d.visualization.draw_geometries([pcd], window_name="tooth", mesh_show_wireframe=True)


