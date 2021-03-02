{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "from pathlib import Path\n",
    "#import Numpy_financial as npf\n",
    "\n",
    "budget_data_path = Path(r\"C:\\Users\\goshl\\OneDrive\\Documents\\fIN_Tech\\Homework\\02-Python\\Instructions\\PyBank\\Resources\\budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_number_of_months = 0\n",
    "sum_of_profit_losses = 0\n",
    "months = []\n",
    "profit_losses = []\n",
    "months_profit_losses = {}\n",
    "net2=0\n",
    "\n",
    "with open(budget_data_path, 'r') as data:\n",
    "    \n",
    "    data_read = csv.reader(data, delimiter = ',')\n",
    "    csv_header = next(data_read)\n",
    "    #print(csv_header)\n",
    "    \n",
    "    for row in data_read:\n",
    "        #print(row)\n",
    "        profit_losses.append(int(row[1]))\n",
    "        months.append(row[0])\n",
    "        \n",
    "        #The total number of months included in the dataset.\n",
    "        total_number_of_months = 1 + total_number_of_months    \n",
    "        \n",
    "print(total_number_of_months)        \n",
    "    \n",
    "            \n",
    "#The net total amount of Profit/Losses over the entire period.\n",
    "\n",
    "for row_profit in profit_losses:\n",
    "    row_profit_losses = int(row_profit)\n",
    "    sum_of_profit_losses += row_profit_losses\n",
    "    \n",
    "    #The average of the changes in Profit/Losses over the entire period.\n",
    "    net =int(row_profit) - net2\n",
    "    net2 = int(row_profit)\n",
    "    Average = net2/total_number_of_months\n",
    "\n",
    "#The greatest increase in profits (date and amount) over the entire period.\n",
    "\n",
    "if net > profit_losses :\n",
    "    max_value = profit_losses\n",
    "    max_month = months\n",
    "    print(\"The greatest increase in profits {max_value} {max_month}\")\n",
    "#The greatest decrease in profits (date and amount) over the entire period.    \n",
    "if net < profit_losses :\n",
    "    max_value1 = profit_losses\n",
    "    max_month1 = months\n",
    "    print(\"The greatest decrease in profits {max_value} {max_month}\")\n",
    "\n",
    "               \n",
    "    \n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(f\"The total number of months included in the dataset. {total_number_of_months}\")\n",
    "print(f\"total amount of Profit/Losses is {sum_of_profit_losses}\")\n",
    "print(f\"The average of the changes in Profit/Losses over the entire period is {Average}\")\n",
    "print(f\"{month} {value}\")\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
