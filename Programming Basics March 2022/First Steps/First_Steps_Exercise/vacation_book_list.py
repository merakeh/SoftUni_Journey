#Broy stranici za chetene
pages_current = int(input())
#Broy stranici procheteni na chas
pages_hour = int(input())
#Broy dni za chetene na knigata
days_to_read = int(input())
#Obshto vreme za chetene na nastoyashtata kniga
hours_total = pages_current / pages_hour
#Kolko chasa na den shte otneme da se prochete knigata
hoursaday = hours_total//days_to_read
print(hoursaday)