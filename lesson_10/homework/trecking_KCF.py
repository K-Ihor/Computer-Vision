import cv2

# Шаг 1: Инициализируем трекер KCF

tracker = cv2.legacy.TrackerKCF_create()

# Чтение видео
video = cv2.VideoCapture('train.mp4')

# Проверяем, удалось ли открыть видео
if not video.isOpened():
    print("Не удалось открыть видео")
    exit()

# Чтение первого кадра
ok, frame = video.read()
if not ok:
    print("Не удалось прочитать видеофайл")
    exit()

# Выбираем объект для трекинга
bbox = cv2.selectROI(frame, False)

# Инициализация трекера с начальным положением объекта
ok = tracker.init(frame, bbox)

# Шаг 2: Запускаем трекер на первых 350 кадрах видео чтоб результат был виден,15 кадров как-то мало
for i in range(350):
# while True:
    # Чтение нового кадра
    ok, frame = video.read()
    if not ok:
        break

    # Обновление трекера
    ok, bbox = tracker.update(frame)

    # Отображение результатов
    if ok:
        # Отрисовка границ трекера
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Сообщение, если трекер не смог отследить объект
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Отображение кадра
    cv2.imshow("Tracking", frame)

    # Выход по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
video.release()
cv2.destroyAllWindows()

