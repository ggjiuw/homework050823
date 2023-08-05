from decimal import Decimal

PRICE_KILLO_CALORIE = Decimal(0.32541).quantize(Decimal('0.00001'))

OSTRICH_EGG_CALORIES = 118
RABBIT_CALORIES = 197
SEA_BASS_CALORIES = 123
SWEET_RED_PEPPER_CALORIES = 26
PARSLEY_CALORIES = 45
BANANA_CALORIES = 87
WAFFLES_CALORIES = 425
BREAD_CALORIES = 246
PISTACHIOS_CALORIES = 555
KEFIR_CALORIES = 51

total_calories = 0

egg_gram = Decimal(input('\nВведіть бажану порцію страусиних яєць\U0001F95A,грам (118 кКал/100гр): ')).quantize(Decimal('0.1'))
egg_final_calories = Decimal(OSTRICH_EGG_CALORIES / Decimal(100).quantize(Decimal('0.1')) * egg_gram).quantize(Decimal('0.1'))
total_calories = total_calories + egg_final_calories
print(f"Калорійність: {egg_final_calories}\n"
    f'Загальна накопичена калорійність: {total_calories}')

rabbit_gram = Decimal(input('\nВведіть бажану порцію кролика\U0001F407,грам (197 кКал/100гр): ')).quantize(Decimal('0.1'))
rabbit_final_calories = Decimal(RABBIT_CALORIES / Decimal(100).quantize(Decimal('0.1')) * rabbit_gram).quantize(Decimal('0.1'))
total_calories = total_calories + rabbit_final_calories
print(f"Калорійність: {rabbit_final_calories}\n"
    f'Загальна накопичена калорійність: {total_calories}')

sea_bass_gram = Decimal(input('\nВведіть бажану порцію морського окуня\U0001F41F,грам (123 кКал/100гр): ')).quantize(Decimal('0.1'))
bass_final_calories = Decimal(SEA_BASS_CALORIES / Decimal(100).quantize(Decimal('0.1')) * sea_bass_gram).quantize(Decimal('0.1'))
total_calories = total_calories + bass_final_calories
print(f"Калорійність: {bass_final_calories}\n"
    f'Загальна накопичена калорійність: {total_calories}')

pepper_gram = Decimal(input('\nВведіть бажану порцію червоного солодкого перцю\U0001F336,грам (26 кКал/100гр): ')).quantize(Decimal('0.1'))
pepper_final_calories = Decimal(SWEET_RED_PEPPER_CALORIES / Decimal(100).quantize(Decimal('0.1')) * pepper_gram).quantize(Decimal('0.1'))
total_calories = total_calories + pepper_gram
print(f"Калорійність: {pepper_final_calories}\n"
    f'Загальна накопичена калорійність: {total_calories}')

parsley_gram = Decimal(input('\nВведіть бажану порцію петрушки,грам (45 кКал/100гр): ')).quantize(Decimal('0.1'))
parsley_final_calories = Decimal(PARSLEY_CALORIES / Decimal(100).quantize(Decimal('0.1')) * parsley_gram).quantize(Decimal('0.1'))
total_calories = total_calories + parsley_gram
print(f"Калорійність: {parsley_final_calories}\n"
    f'Загальна накопичена калорійність: {total_calories}')

banana_gram = Decimal(input('\nВведіть бажану порцію банана\U0001F34C,грам (87 кКал/100гр): ')).quantize(Decimal('0.1'))
banana_final_calories = Decimal(BANANA_CALORIES / Decimal(100).quantize(Decimal('0.1')) * banana_gram).quantize(Decimal('0.1'))
total_calories = total_calories + banana_gram
print(f"Калорійність: {banana_final_calories}\n"
    f'Загальна накопичена калорійність: {total_calories}')

waffles_gram = Decimal(input('\nВведіть бажану порцію вафель\U0001F9C7 ,грам (425 кКал/100гр): ')).quantize(Decimal('0.1'))
waffles_final_calories = Decimal(WAFFLES_CALORIES / Decimal(100).quantize(Decimal('0.1')) * waffles_gram).quantize(Decimal('0.1'))
total_calories = total_calories + waffles_gram
print(f"Калорійність: {waffles_final_calories}\n"
    f'Загальна накопичена калорійність: {total_calories}')

bread_gram = Decimal(input('\nВведіть бажану порцію хліба\U0001F35E ,грам (246 кКал/100гр): ')).quantize(Decimal('0.1'))
bread_final_calories = Decimal(BREAD_CALORIES / Decimal(100).quantize(Decimal('0.1')) * bread_gram).quantize(Decimal('0.1'))
total_calories = total_calories + bread_gram
print(f"Калорійність: {bread_final_calories}\n"
    f'Загальна накопичена калорійність: {total_calories}')

pistachios_gram = Decimal(input('\nВведіть бажану порцію фісташок\U0001F95C ,грам (555 кКал/100гр): ')).quantize(Decimal('0.1'))
pistachios_final_calories = Decimal(PISTACHIOS_CALORIES / Decimal(100).quantize(Decimal('0.1')) * pistachios_gram).quantize(Decimal('0.1'))
total_calories = total_calories + pistachios_gram
print(f"Калорійність: {pistachios_final_calories}\n"
    f'Загальна накопичена калорійність: {total_calories}')

kefir_gram = Decimal(input('\nВведіть бажану порцію кефіру 2.5%\U0001F95B ,грам (51 кКал/100гр): ')).quantize(Decimal('0.1'))
kefir_final_calories = Decimal(KEFIR_CALORIES / Decimal(100).quantize(Decimal('0.1')) * kefir_gram).quantize(Decimal('0.1'))
total_calories = total_calories + kefir_gram
print(f"Калорійність: {kefir_final_calories}\n"
    f'Загальна накопичена калорійність: {total_calories}')

if total_calories < 1000:
    print('\nВи мабуть залишитеся голодними🚫')
    print(f"З вас: {Decimal(PRICE_KILLO_CALORIE * total_calories).quantize(Decimal('0.01'))}грн")
elif total_calories >= 1000:
    if total_calories > 1500:
        print('Ви стільки не зїсте, це гроші в смітник')
        print(f"З вас: {Decimal(PRICE_KILLO_CALORIE * total_calories).quantize(Decimal('0.01'))}грн")
    else:
        print('Це саме ваш варіант вечері👍')
        print(f"З вас: {Decimal(PRICE_KILLO_CALORIE * total_calories).quantize(Decimal('0.01'))}грн")

pass
