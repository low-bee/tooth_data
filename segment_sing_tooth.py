import math

import open3d as o3d
import numpy as np
from sklearn.cluster import KMeans
import copy


"""
目标是通过 inlier_cloud 来分割出每一个牙齿
"""
if __name__ == '__main__':
    pcd = o3d.io.read_point_cloud("copy_of_tooth.ply")


    try:
        while True:
            a = eval(input(" 请输入要选择的牙齿: 从1-14: "))
            if 0 < a < 15:
                i = a
                break
            else:
                print("输入有误, 请输入从1-14之间的数字")
    except Exception as e:
        print("输入有误")
        i = 1
    isOK = True
    first = True
    while isOK:
        distance_list = []
        res = pcd.segment_plane(distance_threshold=0.05, ransac_n=14, num_iterations=300)
        inlier_cloud = pcd.select_by_index(res[1])
        if first:
            print("maximum bound: " + str(inlier_cloud.get_max_bound()))
            print("minimum bound: " + str(inlier_cloud.get_min_bound()))
            print(str(inlier_cloud.Image))
            first = False
        # o3d.visualization.draw_geometries([inlier_cloud])
        kd = o3d.geometry.KDTreeFlann(pcd)
        points: np.ndarray = np.asarray(inlier_cloud.points)
        seed = 5201314
        km = KMeans(n_clusters=14, random_state=seed)
        km.fit(points)
        temp = km.cluster_centers_
        temp = sorted(temp, key=lambda x: x[0], reverse=True)
        points_number = [15, 22, 23, 16, 15, 15, 16]
        [k, idx, _] = kd.search_knn_vector_3d(temp[i-1], points_number[i-1 if i < 8 else abs(i-14)] * 1_000)
        pcd_copy = copy.deepcopy(pcd)
        np.asarray(pcd_copy.colors)[idx[1:], :] = [236 / 256, 222 / 256, 215 / 256]
        o3d.visualization.draw_geometries([pcd_copy], zoom=0.5599,
                                          front=[-0.4958, 0.8229, 0.2773],
                                          lookat=[2.1126, 1.0163, -1.8543],
                                          up=[0.1007, -0.2626, 0.9596])
        ok = input("isOk? 1 yes else no")
        isOK = False if ok == "1" else True




