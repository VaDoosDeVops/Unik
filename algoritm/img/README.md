## **Библиотека: NumPy**

### **1. Изменение яркости изображения**

Мы просто прибавляем число ко всем пикселям.

**Параметры:**

* массив изображения
* значение, на которое увеличиваем яркость

**Пример:**

```python
import numpy as np
from PIL import Image

img = np.array(Image.open("input.jpg"))

# увеличиваем яркость
bright = img + 50

# ограничиваем значения (0–255)
bright = np.clip(bright, 0, 255)

Image.fromarray(bright.astype(np.uint8)).save("bright.jpg")
```

---

### **2. Инверсия (негатив изображения)**

Меняем цвета на противоположные.

**Формула:**
`255 - значение пикселя`

**Пример:**

```python
negative = 255 - img

Image.fromarray(negative.astype(np.uint8)).save("negative.jpg")
```

---

### **3. Обрезка изображения (crop)**

Работаем с массивом как с таблицей.

**Параметры:**

* диапазоны по высоте и ширине

**Пример:**

```python
cropped = img[50:200, 50:200]

Image.fromarray(cropped.astype(np.uint8)).save("crop.jpg")
```

---

### **4. Перевод в черно-белое**

Берем среднее значение каналов RGB.

**Пример:**

```python
gray = np.mean(img, axis=2)

Image.fromarray(gray.astype(np.uint8)).save("gray.jpg")
```

