import cv2


def detect_shape(image_path: None):
    """
    Функция
    """
    # Загрузка изображения
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Бинаризация изображения
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Обнаружение контуров
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Нахождение индекса контура, представляющего всё изображение
    image_contour_idx = 0
    while hierarchy[0][image_contour_idx][3] != -1:
        image_contour_idx = hierarchy[0][image_contour_idx][3]

    # Анализ контуров
    for i, contour in enumerate(contours):
        # Пропуск контура, представляющего всё изображение
        if i == image_contour_idx:
            continue

        # Вычисление площади контура
        area = cv2.contourArea(contour)

        # Фильтрация контуров по площади
        if area < 100:
            continue

        # Аппроксимация контура
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

        # Определение типа фигуры
        if len(approx) == 3:
            return "Треугольник"
        elif len(approx) == 4:
            return "Квадрат или прямоугольник"
        else:
            return'Круг'
        