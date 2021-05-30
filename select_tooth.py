import open3d as o3d
import copy


def registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    return source_temp.transform(transformation)


if __name__ == '__main__':
    pcd = o3d.io.read_point_cloud("copy_of_tooth.ply")
    array = pcd.points
    res = pcd.segment_plane(distance_threshold=0.12, ransac_n=14, num_iterations=10)
    a, b, c, d = res[0]

    """inlier_cloud = pcd.select_by_index(res[1])
    inlier_cloud.paint_uniform_color([0, 1.0, 0])
    o3d.visualization.draw_geometries([inlier_cloud], window_name="边缘")
    """

