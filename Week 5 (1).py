{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "45893cac-c69d-4f5a-9c65-a01417404616",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3]\n",
      "[4, 5, 6]\n",
      "[7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "matrix = [\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "]\n",
    "for row in matrix:\n",
    "    print(row)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0eb998b3-2dc8-445b-ae66-20db12a08750",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_matrices(matrix1, matrix2):\n",
    "    rows = len(matrix1)\n",
    "    columns = len(matrix1[0])\n",
    "    \n",
    "    result = []\n",
    "    for i in range(rows):\n",
    "        row = []\n",
    "        for j in range(columns):\n",
    "            row.append(matrix1[i][j] + matrix2[i][j])\n",
    "        result.append(row)\n",
    "    \n",
    "    return result\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "62d1b89b-3a59-4d01-830e-4c2162c95fc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 10, 10]\n",
      "[10, 10, 10]\n",
      "[10, 10, 10]\n"
     ]
    }
   ],
   "source": [
    "matrix1 = [\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "]\n",
    "\n",
    "matrix2 = [\n",
    "    [9, 8, 7],\n",
    "    [6, 5, 4],\n",
    "    [3, 2, 1]\n",
    "]\n",
    "\n",
    "result_matrix = add_matrices(matrix1, matrix2)\n",
    "\n",
    "for row in result_matrix:\n",
    "    print(row)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0b4813ca-24ce-4f7e-8972-a0f398241e75",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[30, 24, 18]\n",
      "[84, 69, 54]\n",
      "[138, 114, 90]\n"
     ]
    }
   ],
   "source": [
    "def multiply_matrices(matrix1, matrix2):\n",
    "    rows1 = len(matrix1)\n",
    "    columns1 = len(matrix1[0])\n",
    "    rows2 = len(matrix2)\n",
    "    columns2 = len(matrix2[0])\n",
    "    \n",
    "    if columns1 != rows2:\n",
    "        raise ValueError(\"Matrices cannot be multiplied due to incompatible dimensions.\")\n",
    "    \n",
    "    result = []\n",
    "    for i in range(rows1):\n",
    "        row = []\n",
    "        for j in range(columns2):\n",
    "            value = 0\n",
    "            for k in range(columns1):\n",
    "                value += matrix1[i][k] * matrix2[k][j]\n",
    "            row.append(value)\n",
    "        result.append(row)\n",
    "    \n",
    "    return result\n",
    "matrix1 = [\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "]\n",
    "\n",
    "matrix2 = [\n",
    "    [9, 8, 7],\n",
    "    [6, 5, 4],\n",
    "    [3, 2, 1]\n",
    "]\n",
    "\n",
    "result_matrix = multiply_matrices(matrix1, matrix2)\n",
    "for row in result_matrix:\n",
    "    print(row)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5b6e9457-fd74-45cc-92bb-7ca87bb99fe4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select operation:\n",
      "1. Add\n",
      "2. Subtract\n",
      "3. Multiply\n",
      "4. Divide\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter choice (1/2/3/4):  1\n",
      "Enter first number:  1\n",
      "Enter second number:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0 + 2.0 = 3.0\n"
     ]
    }
   ],
   "source": [
    "def add(x, y):\n",
    "    return x + y\n",
    "\n",
    "def subtract(x, y):\n",
    "    return x - y\n",
    "\n",
    "def multiply(x, y):\n",
    "    return x * y\n",
    "\n",
    "def divide(x, y):\n",
    "    if y == 0:\n",
    "        return \"Cannot divide by zero\"\n",
    "    return x / y\n",
    "\n",
    "print(\"Select operation:\")\n",
    "print(\"1. Add\")\n",
    "print(\"2. Subtract\")\n",
    "print(\"3. Multiply\")\n",
    "print(\"4. Divide\")\n",
    "\n",
    "choice = input(\"Enter choice (1/2/3/4): \")\n",
    "\n",
    "num1 = float(input(\"Enter first number: \"))\n",
    "num2 = float(input(\"Enter second number: \"))\n",
    "\n",
    "if choice == '1':\n",
    "    print(num1, \"+\", num2, \"=\", add(num1, num2))\n",
    "elif choice == '2':\n",
    "    print(num1, \"-\", num2, \"=\", subtract(num1, num2))\n",
    "elif choice == '3':\n",
    "    print(num1, \"*\", num2, \"=\", multiply(num1, num2))\n",
    "elif choice == '4':\n",
    "    print(num1, \"/\", num2, \"=\", divide(num1, num2))\n",
    "else:\n",
    "    print(\"Invalid Input\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "223108be-41c7-4e83-a89d-351329d9df1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "def fact(a):\n",
    "    if(a==0 or a==1):\n",
    "        return 1\n",
    "    else:\n",
    "        return a*fact(a-1)\n",
    "num=int(input(\"enter a number \"))\n",
    "factnum=fact(num)\n",
    "print(factnum)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "66afee4d-6a2c-4086-83f8-903ae50e20ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "def cumulative_product(list1):\n",
    "    a=len(list1)\n",
    "    for i in range(0,a):\n",
    "        if list1[i]==0 or list1[i]==1 :\n",
    "            a=1\n",
    "        else:\n",
    "            a= a*list1[i]\n",
    "    return a\n",
    "list1=[1,2,3,4,5]\n",
    "c=cumulative_product(list1)\n",
    "print(c)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "07afc91e-96d0-4c66-9c60-02980e979e9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 4, 3, 2, 1]\n"
     ]
    }
   ],
   "source": [
    "def reverse_list(list1):\n",
    "    list2=[]\n",
    "    for i in range(len(list1) -1,-1,-1):\n",
    "        list2.append(list1[i])\n",
    "    return list2\n",
    "list1=[1,2,3,4,5]\n",
    "list2=reverse_list(list1)\n",
    "print(list2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21416c73-a2c5-450c-9e5f-edb76094bbbd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
