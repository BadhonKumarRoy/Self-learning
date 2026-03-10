#Day 5 - Lists
#Level 1
#1
lst = list()
lst1 = []
print(lst)
print(lst1)
#2
lstNum = [1, 2, 3, 4, 5, 6, 7]
#3
length = len(lstNum)
print(length)
#4
print(lstNum[0], lstNum[length//2], lstNum[length-1])
#5
lst_mixed_data_types = ["Badhon", 22, 5.9, True, "Bangladesh"]
print(lst_mixed_data_types)
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[len(it_companies)-1])
#10
it_companies[3] = "Twitter"
print(it_companies)
#11
it_companies.append("Netflix")
print(it_companies)
#12
it_companies.insert(len(it_companies)//2, "LinkedIn")
print(it_companies)
#13
it_companies[3] = it_companies[3].upper()
print(it_companies)
#14
print('#'.join(it_companies))
#15
print('Apple' in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.reverse()
print(it_companies)
#18
it_companies2 = it_companies[0:3]
print(it_companies2)
#19
it_companies3 = it_companies[-3:]
print(it_companies3)
#20
length = len(it_companies)
if length % 2 == 0:
    print(it_companies[length//2 - 1], it_companies[length//2])
else:
    print(it_companies[len(it_companies)//2])
#21
it_companies.remove(it_companies[0])
print(it_companies)
#22
length = len(it_companies)
print(length)
if length % 2 == 0:
    it_companies.remove(it_companies[length//2])
    it_companies.remove(it_companies[length//2 - 1])
else:
    it_companies.remove(it_companies[length//2])
print(it_companies)
#23
it_companies.remove(it_companies[-1])
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
print("Front End:", front_end)
print("Back End:", back_end)
full_stack = front_end + back_end
print("Full Stack:", full_stack)
#27
copied_full_stack = full_stack.copy()
print(len(copied_full_stack))
copied_full_stack.insert(len(copied_full_stack)//2 + 1, "Python")
copied_full_stack.insert(len(copied_full_stack)//2 + 2, "SQL")
print(copied_full_stack)
#Level 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
ages.append(min_age)
ages.append(max_age)
print(min_age, max_age)
print(ages)
if len(ages) % 2 == 0:
    median_age = (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
else:
    median_age = ages[len(ages)//2]
print(median_age)
average_age = sum(ages) / len(ages)
print('Average age:', average_age)
range_of_ages = max_age - min_age
print('Range of ages:', range_of_ages)
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print('Min diff:', min_diff, 'Max diff:', max_diff)
#1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
length = len(countries)
print('Number of countries:', length)
if length % 2 == 0:
    middle_countries = countries[length//2 - 1:length//2 + 1]
    print('Middle countries:', middle_countries)
else:
    middle_country = countries[length//2]
    print('Middle country:', middle_country)
#2
if len(countries) % 2 == 0:
    divided_countries = (countries[:len(countries)//2], countries[len(countries)//2:])
else:
    divided_countries = (countries[:len(countries)//2 + 1], countries[len(countries)//2 + 1:])
print('First half:', divided_countries[0])
print('Second half:', divided_countries[1])
#3
country1, country2, country3, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(country1)
print(country2)
print(country3)
print(scandic_countries)
#The End