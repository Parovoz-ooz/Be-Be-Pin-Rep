import numpy as np
from keras.models import load_model

# Загрузка обученной модели
model = load_model('my_model.h5')

# Создание тестовой выборки
X_test = np.array([[1, 0], [0, 0], [1, 1], [0, 1]])

# Определение ожидаемых ответов
expected_answers = ['Истина', 'Ложь', 'Истина', 'Истина']

# Получение ответов от модели
predicted_answers = model.predict(X_test)
predicted_answers = np.round(predicted_answers).astype(int)

# Сравнение ожидаемых и полученных ответов
for i in range(len(X_test)):
    if predicted_answers[i] == 1:
        answer = 'Истина'
    else:
        answer = 'Ложь'
        
    print(f'Вопрос {i+1}: Результат {answer}. Ожидаемый ответ: {expected_answers[i]}')