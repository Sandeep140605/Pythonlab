{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "86d8ac26-118b-4c87-802a-09106e9b67c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    1\n",
      "1    2\n",
      "2    3\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "import pandas as p\n",
    "a = [1, 2, 3]\n",
    "s = p.Series(a) \n",
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ad7ae084-6801-4792-abb9-d802e4f8b0fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2c88e0e8-3662-44fc-9363-1fcebaf9c11c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\user\\anaconda3\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\user\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\user\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\user\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\user\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bbe8ceb5-e103-4da9-8d74-bc1e149488ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd \n",
    "a=[1,2,3] \n",
    "s=pd.Series(a) \n",
    "print(s[0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ee2956cd-248d-4be6-8cd5-ee6007f4cf77",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAigAAAGdCAYAAAA44ojeAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAABAaklEQVR4nO3de1iUBf7//+dwGg4CishJEVHxCCJomaZpaZalZpon2t36bLvf2sRDaAc7bNa20lHLMH9bu59OG2oHNdssoy1PWVtyUPGIeUIF8YCchAFm7t8f7fJZykwUvGfg9biuuS7nnntmXjMK8/J+33PfFsMwDERERESciJvZAURERER+TAVFREREnI4KioiIiDgdFRQRERFxOiooIiIi4nRUUERERMTpqKCIiIiI01FBEREREafjYXaAi+FwODh27Bj+/v5YLBaz44iIiMgFMAyDsrIyIiIicHM7/zYSlywox44dIzIy0uwYIiIichHy8/Pp0KHDeddxyYLi7+8P/PACAwICTE4jIiIiF6K0tJTIyMi6z/HzccmC8p+xTkBAgAqKiIiIi7mQ3TO0k6yIiIg4HRUUERERcToqKCIiIuJ0VFBERETE6aigiIiIiNNRQRERERGno4IiIiIiTkcFRURERJyOCoqIiIg4nQYVlNTUVK644gr8/f0JCQlh3Lhx7Nmzp946d955JxaLpd7lqquuqreOzWZj+vTpBAcH4+fnx9ixYzly5MilvxoRERFpFhpUUNavX8+0adP45ptvyMjIoLa2lpEjR1JRUVFvvRtvvJGCgoK6y5o1a+rdPmvWLFauXMmyZcvYtGkT5eXljB49GrvdfumvSERERFxeg87F8+mnn9a7/vrrrxMSEkJmZibXXHNN3XKr1UpYWNg5H6OkpIS//e1vvP3224wYMQKAv//970RGRvL5559zww03NPQ1iIiISDNzSfuglJSUABAUFFRv+bp16wgJCaFbt278/ve/p6ioqO62zMxMampqGDlyZN2yiIgIYmNj2bx58zmfx2azUVpaWu8iIiIija+qxs7cFdt4b0u+qTkuuqAYhkFKSgqDBw8mNja2bvmoUaN45513+OKLL3jhhRf47rvvuO6667DZbAAUFhbi5eVFmzZt6j1eaGgohYWF53yu1NRUAgMD6y6RkZEXG1tERER+xr6icsYt/oql3+Yzb/UOzpyt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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "xpoints = np.array([0, 6])\n",
    "ypoints = np.array([0, 250])\n",
    "plt.plot(xpoints, ypoints)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "54bce83d-b389-4e6b-91a7-7000baf7c4d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Fruits  Qty.   color\n",
      "0  apple     1     red\n",
      "1  mango     2  Yellow\n",
      "2   kiwi     3    Rust\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd \n",
    "a={\"Fruits\":[\"apple\",\"mango\",\"kiwi\"], \"Qty.\":[1,2,3], \"color\":[\"red\",\"Yellow\",\"Rust\"] } \n",
    "df=pd.DataFrame(a) \n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "947ea29a-77e9-4627-979a-25f39d3d8363",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Fruits  Qty\n",
      "x  apple    1\n",
      "y  mango    2\n",
      "z   kiwi    3\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "a={\n",
    "\"Fruits\":[\"apple\",\"mango\",\"kiwi\"],\n",
    "\"Qty\":[1,2,3]\n",
    "}\n",
    "df=pd.DataFrame(a,index=[\"x\",\"y\",\"z\"])\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a90645ee-126a-4f33-81cd-9240ce68b2a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fruits    apple\n",
      "Qty           1\n",
      "Name: x, dtype: object\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "a={\n",
    "\"Fruits\":[\"apple\",\"mango\",\"kiwi\"],\n",
    "\"Qty\":[1,2,3]\n",
    "}\n",
    "df=pd.DataFrame(a,index=[\"x\",\"y\",\"z\"])\n",
    "print(df.loc[\"x\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91d6049e-5939-481e-b807-9a879888a018",
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
