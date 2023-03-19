from django.shortcuts import render
from .models import Portfolio
import random
import math


# Create your views here.
start_capital = 100000.00
cash = 0
month = 0
volatility = 0.2  # волатильность акции (стандартное отклонение ежемесячных процентных изменений цены)
time_horizon = 120  # количество месяцев наблюдения


# Счетчик времени
def months(num):
    num += 1
    return num


# Блок по сбросу к начальным настройкам
def start_training():
    stocks = Portfolio.objects.all()[0]
    bonds = Portfolio.objects.all()[1]
    stocks.title, stocks.num, stocks.price, stocks.month = 'Акции', 500, 100, 1
    bonds.title, bonds.num, bonds.price, bonds.month = 'Облигации', 50, 1000, 1
    stocks.save()
    bonds.save()


# Блок по расчету новой цены акции и облигации
def prices(stock_price, bond_price):
    monthly_return = math.exp(random.gauss(0.0, volatility)) - 1.0
    stock_price *= 1.0 + monthly_return
    if stock_price < 50:
        stock_price *= 2
    elif stock_price > 3000:
        stock_price -= 300
    bond_price = round(bond_price + 5)
    return round(stock_price), round(bond_price)


# Блок оценки стоимости портфеля
def briefcase(stock_num, bond_num, stock_price, bond_price):
    stocks_sum = round(stock_price * stock_num)
    bonds_sum = round(bond_price * bond_num)
    capital = round(stocks_sum + bonds_sum)
    stock_interest = round(stocks_sum / (capital / 100))
    bond_interest = 100 - stock_interest
    return stocks_sum, bonds_sum, capital, stock_interest, bond_interest


# Блок по уравниванию портфеля
def equalize(capital, stocks_price):
    half_capital = round(capital / 2)
    stocks_num = round(half_capital / stocks_price)
    bonds_num = round(half_capital / 1000)
    return stocks_num, bonds_num


# Обновление в начале запуска
start_training()


def index(request):

    # Блок инициализации данных из Базы Данных
    stocks = Portfolio.objects.all()[0]
    bonds = Portfolio.objects.all()[1]

    # Блок определения цен
    stocks.price, bonds.price = prices(stocks.price, bonds.price)

    # Блок оценки портфеля
    stocks_sum, bonds_sum, capital, stocks_interest, bonds_interest = briefcase(stocks.num, bonds.num, stocks.price, bonds.price)

    # Блок выравнивания портфеля
    if stocks_interest > 59 or bonds_interest > 59:
        stocks.num, bonds.num = equalize(capital, stocks.price)
        bonds.price = 1000

    # Блок сохранения данных в Базе Данных
    stocks.save()
    bonds.save()

    # Блок данных для страницы
    data = {'item1_title': stocks.title,
            'item1_num': stocks.num,
            'item1_sum': stocks_sum,
            'item1_price': stocks.price,
            'item1_int': stocks_interest,
            'item2_title': bonds.title,
            'item2_num': bonds.num,
            'item2_sum': bonds_sum,
            'item2_price': bonds.price,
            'item2_int': bonds_interest,
            'capital': capital,
            'cash': cash}

    # Блок отправки данных на страницу
    return render(request, 'main/index.html', context=data)



