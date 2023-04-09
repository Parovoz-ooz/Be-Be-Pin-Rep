import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Данные для обучения
x_train = [
    'Меня зовут Миша. У моей сестры два брата. Как зовут одного из братьев моей сестры?',
    'Меня зовут Миша. У моей сестры только один брат. Как зовут брата моей сестры?'
]

y_train = [
    'Ваня',
    'Ваня'
]

x_val = [
    'Меня зовут Миша. У сестры есть брат. Как его зовут?'
]

y_val = [
    'Ваня'
]

x_test = [
    'Меня зовут Миша. У моей сестры только один брат. Как зовут брата моей сестры?'
]

# Подготовка текста
tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_train)

x_train_seq = tokenizer.texts_to_sequences(x_train)
x_val_seq = tokenizer.texts_to_sequences(x_val)
x_test_seq = tokenizer.texts_to_sequences(x_test)

max_len = max([len(x) for x in x_train_seq])

x_train_padded = pad_sequences(x_train_seq, maxlen=max_len, padding='post')
x_val_padded = pad_sequences(x_val_seq, maxlen=max_len, padding='post')
x_test_padded = pad_sequences(x_test_seq, maxlen=max_len, padding='post')

vocab_size = len(tokenizer.word_index) + 1

# Создаем модель
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, 128, input_length=max_len),
    tf.keras.layers.LSTM(128),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

# Компилируем модель
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Подготовка меток
y_train_labels = tokenizer.texts_to_sequences(y_train)
y_val_labels = tokenizer.texts_to_sequences(y_val)

y_train_labels = np.array([item[0] - 1 if item else 0 for item in y_train_labels])  # Индексация с 0
y_val_labels = np.array([item[0] - 1 if item else 0 for item in y_val_labels])  # Индексация с 0

# Обучаем модель
model.fit(x_train_padded, y_train_labels, epochs=10, validation_data=(x_val_padded, y_val_labels))

# Предсказание ответа
prediction = model.predict(x_test_padded)
predicted_label = np.argmax(prediction, axis=-1) + 1  # Индексация с 1

answer = tokenizer.sequences_to_texts([predicted_label])
print(answer)