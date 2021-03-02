{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# -*- coding: UTF-8 -*-\n",
    "\"\"\"PyRamen Homework Starter.\"\"\"\n",
    "\n",
    "# @TODO: Import libraries\n",
    "import csv\n",
    "from pathlib import Path\n",
    "\n",
    "menu_list = Path(r\"C:\\Users\\goshl\\OneDrive\\Documents\\fIN_Tech\\Homework\\02-Python\\Instructions\\PyRamen\\Resources\\menu_data.csv\")\n",
    "                 \n",
    "# @TODO: Set file paths for menu_data.csv and sales_data.csv\n",
    "menu_filepath = Path(r\"C:\\Users\\goshl\\OneDrive\\Documents\\fIN_Tech\\Homework\\02-Python\\Instructions\\PyRamen\\Resources\\menu_data.csv\")\n",
    "sales_filepath = Path(r\"C:\\Users\\goshl\\OneDrive\\Documents\\fIN_Tech\\Homework\\02-Python\\Instructions\\PyRamen\\Resources\\sales_data.csv\")\n",
    "\n",
    "# @TODO: Initialize list objects to hold our menu and sales data\n",
    "menu = []\n",
    "sales = []\n",
    "sales_item = {}\n",
    "\n",
    "\n",
    "# @TODO: Read in the menu data into the menu list\n",
    "\n",
    "with open(menu_filepath, 'r') as file:\n",
    "    csvreader = csv.reader(file, delimiter = ',')\n",
    "    csv_header = next(csvreader)\n",
    "    print(csv_header)\n",
    "    #csv_header.append('Average')\n",
    "    \n",
    "    for row in csvreader:\n",
    "        print(row)\n",
    "        menu.append(row)\n",
    "        \n",
    "       \n",
    "    # @TODO: Read in the sales data into the sales list\n",
    "\n",
    "\n",
    "with open(sales_filepath, 'r') as file_sale:\n",
    "    csvreader_sales = csv.reader(file_sale, delimiter = ',')\n",
    "    csv_header_sales = next(csvreader_sales)\n",
    "    print(csv_header_sales)\n",
    "    #csv_header.append('Average')\n",
    "    \n",
    "    for row_sales in csvreader_sales:\n",
    "        #print(row_sales)\n",
    "        sales.append(row_sales)\n",
    "             \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "count = []\n",
    "revenue = []\n",
    "cogs = []\n",
    "profit = []\n",
    "quantity = []\n",
    "menu_item = []\n",
    "row_count = 0\n",
    "\n",
    "\n",
    "# @TODO: Initialize dict object to hold our key-value pairs of items and metrics\n",
    "report = {}\n",
    "# Initialize a row counter variable\n",
    "row_count = 0\n",
    "\n",
    "sales_item = {\"01-count\": 0,\"02-revenue\": 0,\"03-cogs\": 0,\"04-profit\": 0,}\n",
    "\n",
    "# @TODO: Loop over every row in the sales list object\n",
    "\n",
    "    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item\n",
    "    # @TODO: Initialize sales data variables\n",
    "\n",
    "with open(sales_filepath, 'r') as file_sale:\n",
    "    csvreader_sales = csv.reader(file_sale, delimiter = ',')\n",
    "    csv_header_sales = next(csvreader_sales)\n",
    "    print(csv_header_sales)\n",
    "    #csv_header.append('Average')\n",
    "    \n",
    "    for row_sales in csvreader_sales:\n",
    "        #print(row_sales)\n",
    "        sales.append(row_sales)\n",
    "             \n",
    "        if \"sales_item\" not in csv_header_sales: \n",
    "            csv_header_sales.append(\"sales_item\")\n",
    "        elif():\n",
    "            print(\"sales_item included in the report\")\n",
    "\n",
    "\n",
    "cost = []\n",
    "price = []\n",
    "profit = []\n",
    "\n",
    "with open(menu_filepath, 'r') as file:\n",
    "    csvreader = csv.reader(file, delimiter = ',')\n",
    "    csv_header = next(csvreader)\n",
    "    print(csv_header)\n",
    "    #csv_header.append('Average')\n",
    "    \n",
    "    for row in csvreader:\n",
    "        print(row)\n",
    "        menu.append(row)\n",
    "        cost.append(row[3])\n",
    "        price.append(row[4])\n",
    "        \n",
    "         # @TODO: Calculate profit of each item in the menu data\n",
    "        price1 = list(map(int, price))\n",
    "        cost1 = list(map(int, cost))\n",
    "        profit.append(price1-cost1)\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\goshl\\\\Jupyter-Workspace'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\goshl\\OneDrive\\Documents\\Fintech Files\\PyRame\n"
     ]
    }
   ],
   "source": [
    "cd \"C:\\Users\\goshl\\OneDrive\\Documents\\Fintech Files\\PyRame\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
