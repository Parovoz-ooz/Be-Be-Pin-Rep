from keras.models import Sequential
from keras.layers import Dense, Dropout, Input
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

# Задаем числовые данные и текстовые описания задач
numbers = [[8, 4], [3, 2], [6, 5], [10, 7], [9, 4]]
texts = ['Если у меня было 8 машинок, а я купила еще 4, сколько машинок у меня есть всего?',
         '3 яблока были в корзине, а потом я добавил еще 2. Сколько яблок стало в корзине?',
         'У меня было 6 карандашей, а я купила еще 5. Сколько карандашей у меня теперь?',
         'В книжном магазине было 10 книг, а затем пришло еще 7. Сколько книг стало в магазине?',
         'У меня было 9 конфет, а я докупила еще 4. Сколько конфет у меня теперь?']

# Создаем токенизатор для преобразования текстовых описаний задач в последовательности чисел
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index

# Добавляем паддинг для последовательностей чисел
data = pad_sequences(sequences, maxlen=10)

# Создаем модель нейронной сети
model = Sequential()

# Добавляем слои к модели
model.add(Embedding(len(word_index) + 1, 32, input_length=10))
model.add(LSTM(64, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(64))
model.add(Dropout(0.2))
model.add(Dense(2, activation='softmax'))

# Компилируем модель
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Обучаем модель на данных
model.fit(data, to_categorical(numbers), epochs=50, batch_size=32)

# Прогнозируем на новых данных
new_texts = ['У меня было 5 яблок, а я докупила еще 3. Сколько яблок у меня теперь?']
new_sequences = tokenizer.texts_to_sequences(new_texts)
new_data = pad_sequences(new_sequences, maxlen=10)
prediction = model.predict(new_data)

# Выводим результаты
print('Формула: {} + {} = {}'.format(numbers[0][0], numbers[0][1], sum(numbers[0])))
print('Прогноз: {} + {} = {}'.format(int(prediction[0][0]), int(prediction[0][1]), int(prediction[0][0] + prediction[0][1])))








