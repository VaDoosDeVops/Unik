---

# **1) Открытие изображения и вывод информации**

### Используем библиотеку `Pillow`

```python
from PIL import Image

img = Image.open("input.jpg")

img.show()
print("Размер:", img.size)
print("Формат:", img.format)      # JPEG, PNG и т.д.
print("Цветовая модель:", img.mode)  # RGB, L и т.д.
```

---

# **2) Уменьшение и зеркальные отражения**

```python
from PIL import Image

img = Image.open("input.jpg")

width, height = img.size
small = img.resize((width // 3, height // 3))
small.save("small.jpg")

# Горизонтальное отражение
mirror_h = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_h.save("mirror_horizontal.jpg")

# Вертикальное отражение
mirror_v = img.transpose(Image.FLIP_TOP_BOTTOM)
mirror_v.save("mirror_vertical.jpg")
```

---

# **3) Применение фильтра к нескольким изображениям**

(например, сделаем Ч/Б фильтр — это не размытие ✅)

```python
import os
from PIL import Image

os.makedirs("output", exist_ok=True)

for i in range(1, 6):
    img = Image.open(f"{i}.jpg")
    gray = img.convert("L")
    gray.save(f"output/gray_{i}.jpg")
```

---

# **4) Добавление водяного знака**

```python
from PIL import Image, ImageDraw, ImageFont

img = Image.open("input.jpg")

draw = ImageDraw.Draw(img)
text = "мое не трогай"

width, height = img.size
position = (width - 150, height - 30)

draw.text(position, text, fill=(255, 255, 255))
img.save("watermark.jpg")
```
