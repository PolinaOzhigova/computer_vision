import pyrealsense2 as rs
import time

# Создаем объект Pipeline - это верхнеуровневый API для потоков и обработки кадров
pipeline = rs.pipeline()

# Запускаем конфигурацию и поток
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

# Запускаем поток
profile = pipeline.start(config)

try:
    while True:
        # Ждем, пока появятся кадры
        frames = pipeline.wait_for_frames()

        # Получаем кадр глубины
        depth_frame = frames.get_depth_frame()

        # Получаем размеры кадра глубины
        width = depth_frame.get_width()
        height = depth_frame.get_height()

        # Запрашиваем расстояние от камеры до объекта в центре изображения
        dist_to_center = depth_frame.get_distance(width // 2, height // 2)

        # Выводим расстояние
        print("Камера направлена на объект, находящийся на расстоянии", dist_to_center, "метров")

        # Ждем 2 секунды перед следующей итерацией
        time.sleep(2)

finally:
    # Останавливаем поток при завершении
    pipeline.stop()
