import pyrealsense2 as rs
import cv2
import numpy as np

# Инициализация камеры RealSense
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

try:
    while True:
        # Ждем, пока появятся кадры
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue

        # Получаем данные изображения
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Преобразовываем глубинное изображение в метры
        depth_image_meters = depth_frame.get_distance(depth_frame.width // 2, depth_frame.height // 2)

        # Задаем порог для определения близких объектов (например, меньше 1 метра)
        threshold_distance = 1.0

        # Находим пиксели, близкие к объектам
        close_object_mask = (depth_image < threshold_distance)

        # Изменяем цвет пикселей, близких к объектам, на красный
        color_image[close_object_mask] = [0, 0, 255]  # BGR

        # Отображаем изображение
        cv2.imshow('RealSense Image', color_image)

        # Завершаем цикл по нажатию клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Останавливаем поток при завершении
    pipeline.stop()
    cv2.destroyAllWindows()
