#broi paketi himikali
pens_package = int(input())

#broi paketi markeri
markers_package = int(input())

litres_clean = int(input())

discount = int(input()) / 100

#Kolko pari shte trybvat na Ani da si plati smetkata

total = pens_package*5.8 + markers_package*7.2 + litres_clean*1.2
final_price = total - (total*discount)
print(final_price)
