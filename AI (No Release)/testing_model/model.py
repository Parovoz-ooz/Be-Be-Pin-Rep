import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Подготовка обучающей выборки
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [0], [1], [1]])

# Создание модели нейросети
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Компиляция модели
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Обучение модели
model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=0)

# Проверка качества обучения на тестовой выборке
X_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_test = np.array([[0], [0], [0], [1]])
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'Test loss: {loss:.4f}\nTest accuracy: {accuracy:.4f}')

# Использование обученной модели для проверки знаний ребенка
X_child = np.array([[1, 0], [0, 0], [1, 1], [0, 1]])
y_child = model.predict(X_child)
y_child_rounded = np.round(y_child)
print(f'Child knowledge: {y_child_rounded}')

model.save('my_model.h5')
