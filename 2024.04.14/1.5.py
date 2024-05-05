text = input("Введите текст: ")
tlg_Len = len (text)
count = 0
for i in text:
 if i == ' ':
  count += 1
  tlg_Len1 = tlg_Len - count
  sum = int((tlg_Len1 * 0.3)//1)
  sum1 = int((tlg_Len1 * 0.3) % 1 * 100)
print (sum, "руб.", sum1, "коп.")



