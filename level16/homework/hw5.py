#5) დედამ გაგიშვათ აფთიაქში თავის ტკივილის წამლის საყიდლათ, ეს წამალი დღეში უნდა დალიო შენი წონის მიხედვით. თუ 10 დან 20 კილომდე ხარ ნახევარი 
# ტაბლეტი უნდა დალიო დღეში, თუ 30-40 კილომდე ხარ 1 ტაბლეთი ორჯერ დღეში და თუ 45 კილოზე მეტი ხარ სამი ტაბლეტი უნდა დალიო ორჯერ დღეში. 
# თქვენი მისიაა ამ ინფორმაციით გაარკვიოთ მომხარებელს რამდენი წამალი აქვს დასალევი და დღეში რამდენჯერ უნდა დალიოს.

weight = int(input("how much do you weight"))

if weight >= 10 and weight <= 20:
    print("you have to drink half pill a day")
elif weight >= 21 and weight <= 40:
    print("you have to drink one pil twice a day")
elif weight > 40:
    print("you have to drink three pills twice a day")