import pyfiglet
from termcolor import colored
import random

# نامی که می‌خواهید چاپ کنید
name = "         _نام "

# ایجاد متن ASCII Art با فونت دلخواه
ascii_art = pyfiglet.figlet_format(name, font='slant')

# تعریف رنگ‌ها و افکت‌ها
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
effects = ['bold', 'underline', 'blink']

# متون حاشیه‌ای مرتبط با کدنویسی و هکری
border_text_top = "=== متن خود را بنویسید ==="
border_text_bottom = "=== متن خود را بنویسید ==="

# تولید رنگین کمانی از رنگ‌ها
def rainbow_colors(text):
    """
    این تابع متنی را دریافت می‌کند و آن را به رنگ‌های مختلف رنگین کمانی تبدیل می‌کند.
    """
    rainbow_text = ""
    color_index = 0
    for char in text:
        if char != ' ' and char != '\n':
            rainbow_text += colored(char, colors[color_index % len(colors)], attrs=['bold'])
            color_index += 1
        else:
            rainbow_text += char
    return rainbow_text

# افزودن افکت‌های مختلف به هر خط از متن ASCII Art
def add_effects(text):
    """
    این تابع افکت‌های مختلفی را به متن ASCII Art اضافه می‌کند.
    """
    lines = text.split('\n')
    colorful_text = ""
    for line in lines:
        colorful_line = rainbow_colors(line)
        colorful_text += colorful_line + '\n'
    return colorful_text

# اعمال افکت‌ها به متن ASCII Art
colored_ascii_art = add_effects(ascii_art)

# ایجاد خطوط حاشیه‌ای با متن‌های هکری
border_top = rainbow_colors(border_text_top)
border_bottom = rainbow_colors(border_text_bottom)

# ترکیب حاشیه‌ها با متن اصلی
bordered_ascii_art = f"{border_top}\n{colored_ascii_art}\n{border_bottom}"

# نوشتن متن رنگی در یک فایل جدید با کدگذاری UTF-8
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(bordered_ascii_art)

# چاپ متن رنگی در کنسول
print(bordered_ascii_art)
print("Colored ASCII art with effects and coding-themed borders has been written to output.txt")
