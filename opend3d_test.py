import open3d as o3d

if __name__ == '__main__':
    down_tooth_mesh = o3d.io.read_triangle_mesh("data/dental_0173.stl")
    down_tooth_mesh = down_tooth_mesh.compute_adjacency_list()
    down_tooth_mesh.paint_uniform_color([0.99, 0.99, 0.99])

    o3d.visualization.draw_geometries([down_tooth_mesh], window_name="tooth", mesh_show_wireframe=True)




