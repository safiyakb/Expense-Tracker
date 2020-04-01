from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from expense.models import Expense, Income, Wallet
from datetime import datetime

def signup(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		email = request.POST["email"]

		user = User.objects.create_user(
			username=username,
			password=password,
			email=email)
		login(request, user)

		return redirect("/dashboard/")

	return render(request, "signup.html")

def signin(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(username=username, password=password)

		if user != None:
			login(request, user)
			return redirect("/dashboard/")

	return render(request, "signin.html")

def signout(request):
	logout(request)
	return redirect("/signin/")

def dashboard(request):
	user = request.user
	all_wallets = Wallet.objects.filter(user=user)
	all_expenses = Expense.objects.filter(user=user)
	all_incomes = Income.objects.filter(user=user)
	return render(request, "dashboard.html", {"all_wallets":all_wallets, "all_expenses":all_expenses, "all_incomes":all_incomes})

def get_all_wallet(request):
	user = request.user
	all_wallets = Wallet.objects.filter(user=user)
	return render(request, "wallet.html", {"all_wallets":all_wallets})

def get_all_expense(request):
	user = request.user
	all_wallets = Wallet.objects.filter(user=user)
	all_expenses = Expense.objects.filter(user=user)
	return render(request, "expense.html", {"all_wallets":all_wallets, "all_expenses":all_expenses})

def get_all_income(request):
	user = request.user
	all_wallets = Wallet.objects.filter(user=user)
	all_incomes = Income.objects.filter(user=user)
	return render(request, "income.html", {"all_wallets":all_wallets, "all_incomes":all_incomes})

def create_wallet(request):
	if request.method == "POST":
		wallet_name = request.POST["wallet_name"]
		wallet_balance = request.POST["wallet_balance"]

		wallet_instance = Wallet.objects.create(
			name = wallet_name,
			balance = wallet_balance,
			last_transaction = datetime.now(),
			user = request.user
			)

		return redirect("/wallet/")

	return redirect("/wallet/")

def create_expense(request):
	if request.method == "POST":
		wallet_id = request.POST["wallet"]
		expense_title = request.POST["expense_title"]
		expense_amount = request.POST["expense_amount"]
		expense_description = request.POST["expense_description"]

		wallet_instance = Wallet.objects.get(pk=wallet_id)

		expense_instance = Expense.objects.create(
			title = expense_title,
			amount = expense_amount,
			description = expense_description,
			timestamp = datetime.now(),
			user = request.user,
			wallet = wallet_instance
			)

		wallet_instance.balance -= int(expense_amount)
		wallet_instance.save()

		return redirect("/expense/")

	return redirect("/expense/")

def create_income(request):
	if request.method == "POST":
		wallet_id = request.POST["wallet"]
		income_title = request.POST["income_title"]
		income_amount = request.POST["income_amount"]
		income_description = request.POST["income_description"]

		wallet_instance = Wallet.objects.get(pk=wallet_id)

		income_instance = Income.objects.create(
			title = income_title,
			amount = income_amount,
			description = income_description,
			timestamp = datetime.now(),
			user = request.user,
			wallet = wallet_instance
			)

		wallet_instance.balance += int(income_amount)
		wallet_instance.save()

		return redirect("/income/")

	return redirect("/income/")

def delete_wallet(request, wallet_id):
	wallet_instance = Wallet.objects.get(pk=wallet_id)
	wallet_instance.delete()

	return redirect("/wallet/")

def delete_expense(request, expense_id):
	expense_instance = Expense.objects.get(pk=expense_id)
	expense_instance.delete()

	return redirect("/expense/")

def delete_income(request, income_id):
	income_instance = Income.objects.get(pk=income_id)
	income_instance.delete()

	return redirect("/income/")

def edit_wallet(request, wallet_id):
	wallet_instance = Wallet.objects.get(pk=wallet_id)

	if request.method == "POST":
		wallet_name = request.POST["wallet_name"]
		wallet_balance = request.POST["wallet_balance"]

		wallet_instance = Wallet.objects.get(pk=wallet_id)

		wallet_instance.name = wallet_name
		wallet_instance.balance = wallet_balance
		wallet_instance.last_transaction = datetime.now()

		wallet_instance.save()

		return redirect("/wallet/")

	return render(request, "edit_wallet.html", {"wallet":wallet_instance})


def edit_expense(request, expense_id):
	expense_instance = Expense.objects.get(pk=expense_id)

	if request.method == "POST":
		expense_title = request.POST["expense_title"]
		expense_amount = request.POST["expense_amount"]
		expense_description = request.POST["expense_description"]

		expense_instance = Expense.objects.get(pk=expense_id)

		expense_instance.title = expense_title
		expense_instance.amount = expense_amount
		expense_instance.description = expense_description
		expense_instance.timestamp = datetime.now()

		expense_instance.save()

		return redirect("/expense/")

	return render(request, "edit_expense.html", {"expense":expense_instance})

def edit_income(request, income_id):
	income_instance = Income.objects.get(pk=income_id)

	if request.method == "POST":
		income_title = request.POST["income_title"]
		income_amount = request.POST["income_amount"]
		income_description = request.POST["income_description"]

		income_instance = Income.objects.get(pk=income_id)

		income_instance.title = income_title
		income_instance.amount = income_amount
		income_instance.description = income_description
		income_instance.timestamp = datetime.now()

		income_instance.save()

		return redirect("/income/")

	return render(request, "edit_income.html", {"income":income_instance})