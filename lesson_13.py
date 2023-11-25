

number_of_countries = int(input("How many countries do you want to enter: "))


countries = []
for _ in range(number_of_countries):
    country_code = int(input("Enter country code: "))
    countries.append(country_code)


unique_stamps = set()
updated_countries = set()


for country in countries:
    if country in unique_stamps:
        updated_countries.add(country)
    else:
        unique_stamps.add(country)


num_stamps_to_give = len(updated_countries)
num_unique_stamps = len(unique_stamps)

print(f"Leonard should give David {num_stamps_to_give} stamp(s) whose country code(s) are: {', '.join(map(str, updated_countries))}")
print(f"Leonard has {num_unique_stamps} unique stamp(s).")
