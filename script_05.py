"""Написати програму для циклічного виведення на екран пар ключ:значення.
"""
knights = {
    'school': '10 years',
    'bachelor': '4 years',
    'master': '1.5 years',
    'graduate student': '4 years'
}

for key, value in knights.items():
    print(f'{key}: {value}')
