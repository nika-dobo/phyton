import datetime as d # as d არის სახელი რომელიაც შევძლებს გამოძახებას (არ არის აუცილებელი)

print(d.datetime.now().time().hour) #ამ კოდით გვიბრუნებს დროს ამ შემთხვევში საათს
print(d.datetime.now().time())# ეს დააბრუნებს ახლანდელ დროს (საათს, წუთს, წამს,)
print(d.datetime.now()) # ეს აბრუნებს ახლანდელ დროს და თარიღს(წელს, თვეს, დღეს, საათს, წუთს, წამს,)