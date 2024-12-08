{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c226aeaa-d581-4672-a697-4440354d9dcf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square area: 25\n",
      "Square perimeter: 20\n",
      "Circle area: 28.259999999999998\n",
      "Circle circumference: 18.84\n",
      "Triangle area: 12.0\n",
      "Triangle perimeter: 12\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "def square_area(side):\n",
    "    return side * side\n",
    "def square_perimeter(side):\n",
    "    return 4 * side\n",
    "def circle_area(radius):\n",
    "    return math.pi * radius**2\n",
    "def circle_circumference(radius):\n",
    "    return 2 * math.pi * radius\n",
    "def triangle_area(base, height):\n",
    "    return 0.5 * base * height\n",
    "def triangle_perimeter(side1, side2, side3):\n",
    "    return side1 + side2 + side3\n",
    "#import geometry\n",
    "side_length = 5\n",
    "radius = 3\n",
    "base = 4\n",
    "height = 6\n",
    "side1 = 3\n",
    "side2 = 4\n",
    "side3 = 5\n",
    "print(\"Square area:\", side_length*side_length)\n",
    "print(\"Square perimeter:\", 4*side_length)\n",
    "print(\"Circle area:\", 3.14*radius*radius)\n",
    "print(\"Circle circumference:\", 2*3.14*radius)\n",
    "print(\"Triangle area:\", 0.5*base*height)\n",
    "print(\"Triangle perimeter:\", side1+side2+side3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ad084948-8807-4f0f-aa75-0ab621e53424",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   \n",
      "    # # # # #      \n",
      "    #       #      \n",
      "    # # # # #      \n",
      "                   \n",
      "                   \n"
     ]
    }
   ],
   "source": [
    "class Canvas:\n",
    "    def __init__(self, width, height):  # Fixed to __init__\n",
    "        self.width = width\n",
    "        self.height = height\n",
    "        self.grid = [[' ' for _ in range(width)] for _ in range(height)]\n",
    "\n",
    "    def draw(self):\n",
    "        for row in self.grid:\n",
    "            print(' '.join(row))\n",
    "\n",
    "\n",
    "class Rectangle:\n",
    "    def __init__(self, x, y, width, height):  # Fixed to __init__\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        self.width = width\n",
    "        self.height = height\n",
    "\n",
    "\n",
    "def draw_rectangle(canvas, rectangle):\n",
    "    for row in range(rectangle.y, rectangle.y + rectangle.height):\n",
    "        for col in range(rectangle.x, rectangle.x + rectangle.width):\n",
    "            if (\n",
    "                row == rectangle.y\n",
    "                or row == rectangle.y + rectangle.height - 1\n",
    "                or col == rectangle.x\n",
    "                or col == rectangle.x + rectangle.width - 1\n",
    "            ):\n",
    "                canvas.grid[row][col] = '#'\n",
    "\n",
    "\n",
    "# Example usage\n",
    "canvas = Canvas(10, 6)\n",
    "rectangle = Rectangle(2, 1, 5, 3)\n",
    "draw_rectangle(canvas, rectangle)\n",
    "canvas.draw()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "931b4df8-d491-445a-b146-b928cafbaf48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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SEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFJiBABISowAAEmJEQAgKTECACQlRgCApMQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJIqOkb27NkTixcvjkmTJkUul4uXX3550PFtbW2Ry+Uuu7355pvDnTMAMIqUFXvC2bNnY9asWfHYY4/FkiVLhnze0aNHo6qqqvf+rbfeWuxLAwCjUNExsnDhwli4cGHRLzRhwoS4+eabiz4PABjdPrFrRmbPnh21tbXR2NgYu3fvHnRsoVCIfD7f5wYAjE7XPEZqa2tjw4YN0draGi+99FJMnz49GhsbY8+ePQOe09LSEtXV1b23urq6az1NACCRXJZl2bBPzuVi69at8fDDDxd13uLFiyOXy8W2bdv6fbxQKEShUOi9n8/no66uLnp6evpcd3K1Dh6MqK8fsacDgJJ14EDEvfeO7HPm8/morq6+4vt3kl/tnTt3brz11lsDPl5eXh5VVVV9bgDA6JQkRjo7O6O2tjbFSwMA15mif5vm/fffj//6r//qvX/s2LE4dOhQjBs3LqZMmRLNzc1x8uTJ2LRpU0RErFmzJm677baYMWNGnDt3LjZv3hytra3R2to6cqsAAEpW0THS0dERX/7yl3vvNzU1RUTE0qVL48UXX4yurq44fvx47+Pnzp2LVatWxcmTJ+PGG2+MGTNmxPbt22PRokUjMH0AoNRd1QWsn5ShXgBTLBewAsCHPnUXsAIAXCJGAICkxAgAkJQYAQCSEiMAQFJiBABISowAAEmJEQAgKTECACQlRgCApMQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFJiBABISowAAEmJEQAgKTECACQlRgCApMQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUkXHyJ49e2Lx4sUxadKkyOVy8fLLL1/xnPb29qivr4+KioqYNm1arF+/fjhzBQBGoaJj5OzZszFr1qx47rnnhjT+2LFjsWjRopg3b150dnbG6tWrY+XKldHa2lr0ZAGA0aes2BMWLlwYCxcuHPL49evXx5QpU2LNmjUREXHXXXdFR0dHPPPMM7FkyZJiXx4AGGWu+TUje/fujfnz5/c5tmDBgujo6Ijz589f65cHAK5zRX8yUqzu7u6oqanpc6ympiYuXLgQp0+fjtra2svOKRQKUSgUeu/n8/lrPU0AIJFP5Ldpcrlcn/tZlvV7/JKWlpaorq7uvdXV1V2TeX3ucxEVFdfkqQGgZFRUfPiemMo1/2Rk4sSJ0d3d3efYqVOnoqysLMaPH9/vOc3NzdHU1NR7P5/PX5MgmTIl4ujRiNOnR/ypAaBkfO5zH74npnLNY6ShoSFeeeWVPsd27twZc+bMiTFjxvR7Tnl5eZSXl1/rqUXEh//yU24AAHzaFf1jmvfffz8OHToUhw4diogPf3X30KFDcfz48Yj48FONRx99tHf8smXL4p133ommpqY4cuRIPP/887Fx48ZYtWrVyKwAAChpRX8y0tHREV/+8pd771/6ccrSpUvjxRdfjK6urt4wiYiYOnVqvPrqq/Hkk0/GD3/4w5g0aVKsXbvWr/UCABERkcsuXU16Hcvn81FdXR09PT1RVVWVejoAwBAM9f3b36YBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkNQ1/9s0I+HS97Ll8/nEMwEAhurS+/aVvl+1JGLkzJkzERHX5C/3AgDX1pkzZ6K6unrAx0vi6+B/85vfxLvvvhuVlZWRy+VG7Hnz+XzU1dXFiRMnRu3XzI/2NVpf6Rvtaxzt64sY/Wu0vuHLsizOnDkTkyZNihtuGPjKkJL4ZOSGG26IyZMnX7Pnr6qqGpX/gX3UaF+j9ZW+0b7G0b6+iNG/RusbnsE+EbnEBawAQFJiBABI6lMdI+Xl5fG9730vysvLU0/lmhnta7S+0jfa1zja1xcx+tdofddeSVzACgCMXp/qT0YAgPTECACQlBgBAJISIwBAUqM6Rvbs2ROLFy+OSZMmRS6Xi5dffvmK57S3t0d9fX1UVFTEtGnTYv369dd+osNU7Pra2toil8tddnvzzTc/mQkXqaWlJe67776orKyMCRMmxMMPPxxHjx694nmlsofDWV+p7eG6deti5syZvV+m1NDQEK+99tqg55TK/kUUv75S27+Pa2lpiVwuF9/5zncGHVdKe/hxQ1ljKe3jX/3VX102z4kTJw56Tor9G9Uxcvbs2Zg1a1Y899xzQxp/7NixWLRoUcybNy86Oztj9erVsXLlymhtbb3GMx2eYtd3ydGjR6Orq6v3dscdd1yjGV6d9vb2WL58eezbty927doVFy5ciPnz58fZs2cHPKeU9nA467ukVPZw8uTJ8fTTT0dHR0d0dHTEV77ylXjooYfijTfe6Hd8Ke1fRPHru6RU9u+j9u/fHxs2bIiZM2cOOq7U9vCjhrrGS0plH2fMmNFnnocPHx5wbLL9yz4lIiLbunXroGP+4i/+Irvzzjv7HPuzP/uzbO7cuddwZiNjKOvbvXt3FhHZf//3f38icxppp06dyiIia29vH3BMKe/hUNZX6nuYZVl2yy23ZD/+8Y/7fayU9++SwdZXqvt35syZ7I477sh27dqVPfjgg9kTTzwx4NhS3cNi1lhK+/i9730vmzVr1pDHp9q/Uf3JSLH27t0b8+fP73NswYIF0dHREefPn080q5E3e/bsqK2tjcbGxti9e3fq6QxZT09PRESMGzduwDGlvIdDWd8lpbiHFy9ejC1btsTZs2ejoaGh3zGlvH9DWd8lpbZ/y5cvj69//evx1a9+9YpjS3UPi1njJaWyj2+99VZMmjQppk6dGn/4h38Yb7/99oBjU+1fSfyhvE9Kd3d31NTU9DlWU1MTFy5ciNOnT0dtbW2imY2M2tra2LBhQ9TX10ehUIh/+qd/isbGxmhra4sHHngg9fQGlWVZNDU1xf333x/33HPPgONKdQ+Hur5S3MPDhw9HQ0NDfPDBB3HTTTfF1q1b4+677+53bCnuXzHrK8X927JlSxw8eDD2798/pPGluIfFrrGU9vF3f/d3Y9OmTfE7v/M78d5778UPfvCD+L3f+7144403Yvz48ZeNT7V/YuRjcrlcn/vZ/39B7cePl6Lp06fH9OnTe+83NDTEiRMn4plnnrnu/gf6uMcffzxef/31+MUvfnHFsaW4h0NdXynu4fTp0+PQoUPx61//OlpbW2Pp0qXR3t4+4Bt2qe1fMesrtf07ceJEPPHEE7Fz586oqKgY8nmltIfDWWMp7ePChQt7//kLX/hCNDQ0xOc///n4yU9+Ek1NTf2ek2L//JjmIyZOnBjd3d19jp06dSrKysr6LcjRYO7cufHWW2+lnsagVqxYEdu2bYvdu3fH5MmTBx1bintYzPr6c73v4dixY+P222+POXPmREtLS8yaNSueffbZfseW4v4Vs77+XM/7d+DAgTh16lTU19dHWVlZlJWVRXt7e6xduzbKysri4sWLl51Tans4nDX253rex4/67Gc/G1/4whcGnGuq/fPJyEc0NDTEK6+80ufYzp07Y86cOTFmzJhEs7q2Ojs7r8uPTSM+rPEVK1bE1q1bo62tLaZOnXrFc0ppD4ezvv5cz3vYnyzLolAo9PtYKe3fQAZbX3+u5/1rbGy87DcvHnvssbjzzjvjqaeeis985jOXnVNqezicNfbnet7HjyoUCnHkyJGYN29ev48n279renlsYmfOnMk6Ozuzzs7OLCKyv//7v886Ozuzd955J8uyLPvud7+bPfLII73j33777ey3fuu3sieffDL75S9/mW3cuDEbM2ZM9i//8i+pljCoYtf3D//wD9nWrVuz//zP/8z+4z/+I/vud7+bRUTW2tqaagmD+va3v51VV1dnbW1tWVdXV+/tf/7nf3rHlPIeDmd9pbaHzc3N2Z49e7Jjx45lr7/+erZ69ershhtuyHbu3JllWWnvX5YVv75S27/+fPw3TUp9D/tzpTWW0j7++Z//edbW1pa9/fbb2b59+7JvfOMbWWVlZfarX/0qy7LrZ/9GdYxc+vWrj9+WLl2aZVmWLV26NHvwwQf7nNPW1pbNnj07Gzt2bHbbbbdl69at++QnPkTFru9v//Zvs89//vNZRUVFdsstt2T3339/tn379jSTH4L+1hYR2QsvvNA7ppT3cDjrK7U9/Na3vpX99m//djZ27Njs1ltvzRobG3vfqLOstPcvy4pfX6ntX38+/kZd6nvYnyutsZT28Q/+4A+y2trabMyYMdmkSZOy3//938/eeOON3sevl/3LZdn/X5kCAJCAC1gBgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFL/BzWJj5Ej3CQpAAAAAElFTkSuQmCC",
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
    "import matplotlib.patches as patches\n",
    "\n",
    "class Canvas:\n",
    "\n",
    "    def __init__(self):\n",
    "        self.fig, self.ax = plt.subplots()\n",
    "\n",
    "    def draw_rectangle(self, rectangle):\n",
    "        x = rectangle.x\n",
    "        y = rectangle.y\n",
    "        width = rectangle.width\n",
    "        height = rectangle.height\n",
    "        color = rectangle.color\n",
    "        rect = patches.Rectangle((x, y), width, height, color=color)\n",
    "        self.ax.add_patch(rect)\n",
    "\n",
    "    def show(self):\n",
    "        plt.axis('equal')\n",
    "        plt.show()\n",
    "\n",
    "class Rectangle:\n",
    "\n",
    "    def __init__(self, x, y, width, height, color):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        self.width = width\n",
    "        self.height = height\n",
    "        self.color = color\n",
    "\n",
    "# Example usage:\n",
    "canvas = Canvas()\n",
    "rectangle1 = Rectangle(1, 1, 4, 3, \"blue\")\n",
    "canvas.draw_rectangle(rectangle1)\n",
    "canvas.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "1e2de707-a048-4f2d-8917-c221f84c6411",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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SpWwucISERGhxMTELnt8l8vFhg4SaxUa1it4rFXwWKvgsVbB66q1au/KSjNedAsAAKxHsAAAAOsRLBfgdDr1+9//Xk6n81JPxXqsVWhYr+CxVsFjrYLHWgXPhrUKmxfdAgCA8MUVFgAAYD2CBQAAWI9gAQAA1iNYAACA9S6rYCksLNSIESMUFxena6+9Vvfee6+qqqoueL+33npLw4YN0xVXXKF+/frpoYce0r///W//91evXi2Hw9Hi9u2333bl6XSpjq7VokWLNGTIEMXGxmrQoEFau3ZtizHFxcVKTU2V0+lUamqqNmzY0BWn0G26aq3CcV8tWbJEaWlp/g+fyszM1MaNG9u9z7Zt25Senq6YmBgNGDBAS5cubTEm3PaU1DVrFY57qlmo61VbW6spU6Zo0KBBioiI0MyZM1sdx94Kbq26ZW+Zy0h2drZZtWqVOXjwoKmsrDQTJ0401113nTlz5kyb99mxY4eJiIgwCxYsMF988YXZsWOHuemmm8y9997rH7Nq1SrjcrlMbW1twK0n68haLV682MTFxRmPx2M+//xzs379etO7d29TUlLiH1NaWmoiIyPNSy+9ZD799FPz0ksvmaioKLNr167uOK0u0VVrFY77qqSkxPz1r381VVVVpqqqysyaNctER0ebgwcPtjr+iy++MFdccYXJz883hw8fNsuXLzfR0dHm3Xff9Y8Jxz1lTNesVTjuqWahrtfRo0fNk08+adasWWNuueUWk5+f32IMe+ucYNaqO/bWZRUs56uvrzeSzLZt29oc88orr5gBAwYEHCsqKjKJiYn+r1etWmXcbndXTdMKwaxVZmam+c1vfhNwLD8/34wePdr/9eTJk81dd90VMCY7O9v8/Oc/79wJX0KdtVaXw74yxpg+ffqYFStWtPq9Z555xgwePDjg2KOPPmpGjRrl//py2FPNLnatLpc91ay99fqh22+/vdVfwuytltpaq+7YW5fVU0Lna2hokCRdddVVbY7JysrSsWPH9OGHH8oYoxMnTujdd9/VxIkTA8adOXNGycnJSkxM1KRJk1RRUdGlc+9uwayVz+dTTExMwLHY2Fjt2bNHjY2NkqSysjJNmDAhYEx2drZKS0s7ecaXTmetlRTe+6qpqUkej0fffPONMjMzWx3T1n4pLy+/rPZUZ62VFN57qlkw6xUM9lZounpvXbbBYozR008/rZ/85CcaOnRom+OysrL01ltvKTc3V7169VJCQoJ+9KMf6fXXX/ePGTx4sFavXq2SkhKtX79eMTExGj16tI4cOdIdp9Llgl2r7OxsrVixQvv27ZMxRuXl5Vq5cqUaGxt18uRJSVJdXZ3i4+MD7hcfH6+6urouPYfu0plrFa776sCBA+rdu7ecTqemT5+uDRs2KDU1tdWxbe2X77777rLYU529VuG6p5qFsl7BYG8Fr1v2Vpdev7HY448/bpKTk01NTU274w4dOmT69etnXn75ZbN//36zadMmc/PNN5uHH364zfs0NTWZYcOGmSeeeKKzp31JBLtWZ8+eNQ899JCJiooykZGRpn///uaZZ54xksyJEyeMMcZER0ebt99+O+B+69atM06ns8vm3506c63OFy77yufzmSNHjpi9e/ea5557zlx99dXm0KFDrY698cYbzUsvvRRwbOfOnUaS//nxcN5Tnb1W5wuXPdUslPX6obae5mBvtdTWWp2vK/bWZXmF5YknnlBJSYn+/ve/KzExsd2xhYWFGj16tH77298qLS1N2dnZWrx4sVauXKna2tpW7xMREaERI0aExZ9aQlmr2NhYrVy5UmfPntWXX36p6upqpaSkKC4uTldffbUkKSEhocWfTurr61v8KaYn6uy1Ol+47KtevXrphhtuUEZGhgoLCzVs2DAtWLCg1bFt7ZeoqCj17du33THhsKc6e63OFy57qlko6xUM9lbHdcXeuqyCxRijX//613rvvff0t7/9Tddff/0F73P27FlFRAQuU2RkpP/x2vo5lZWV6tev38VP+hLpyFo1i46OVmJioiIjI+XxeDRp0iT/GmZmZmrLli0B4zdv3qysrKxOnX936qq1au3n9PR91RpjjHw+X6vfa2u/ZGRkKDo6ut0xPXlPteVi16q1xwvHPdWsvfUKBnvr4h6v0/dWp12r6QEee+wx43a7zdatWwPednX27Fn/mOeee87k5eX5v161apWJiooyixcvNp9//rnZuXOnycjIMLfddpt/zAsvvGA2bdpkPv/8c1NRUeG/1L979+5uPb/O1JG1qqqqMm+++ab57LPPzO7du01ubq656qqrzNGjR/1jPv74YxMZGWnmzp1rPv30UzN37twe/zbBrlqrcNxXBQUFZvv27ebo0aPmH//4h5k1a5aJiIgwmzdvNsa0XKfmt+o+9dRT5vDhw+aNN95o8VbdcNxTxnTNWoXjnmoW6noZY0xFRYWpqKgw6enpZsqUKaaioiLgaRH21v+70Fp1x966rIJFUqu3VatW+cc8+OCD5vbbbw+4X1FRkUlNTTWxsbGmX79+ZurUqebYsWP+78+cOdNcd911plevXuaaa64xEyZMMKWlpd10Vl2jI2t1+PBhc8stt5jY2FjjcrlMTk6O+ec//9nisf/yl7+YQYMGmejoaDN48GBTXFzcDWfUdbpqrcJxXz388MMmOTnZf07jxo3z/0/SmNb/+9u6dasZPny46dWrl0lJSTFLlixp8bjhtqeM6Zq1Csc91awj69Xaf7fJyckBY9hb51xorbpjbzn+byIAAADWuqxewwIAAHomggUAAFiPYAEAANYjWAAAgPUIFgAAYD2CBQAAWI9gAQAA1iNYAACA9QgWAABgPYIFAABYj2ABAADWI1gAAID1/hck/1PVNDvUWQAAAABJRU5ErkJggg==",
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
    "import matplotlib.patches as patches\n",
    "\n",
    "class Canvas:\n",
    "\n",
    "    def __init__(self):\n",
    "        self.fig, self.ax = plt.subplots()\n",
    "\n",
    "    def draw_point(self, point):\n",
    "        x = point.x\n",
    "        y = point.y\n",
    "        plt.plot(x, y, 'ro')\n",
    "\n",
    "    def show(self):\n",
    "        plt.axis('equal')\n",
    "        plt.show()\n",
    "\n",
    "class Point:\n",
    "\n",
    "    def __init__(self, x, y):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "# Example usage:\n",
    "canvas = Canvas()\n",
    "point1 = Point(3, 4)\n",
    "canvas.draw_point(point1)\n",
    "canvas.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b98945eb-1986-4991-aa94-7c1902a2ca65",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAi4AAAGiCAYAAADA0E3hAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAcu0lEQVR4nO3db2yV5f348U9paaturRG0FkEEpxMl6mgDo6wandag0ZBskcVF1GliszmETqeMRYYxaXTRfXUKbgoaE3REReeDztEHG1Zxf2DFGCFxEWZBW0kxtqhbGXD/Hhj6W9fiOLV/uNrXK7kfnMv7Puc6uazn7X2fP3lZlmUBAJCAMcM9AQCAIyVcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGTkHC6vvPJKXHnllTFhwoTIy8uLF1988X8es2HDhqioqIji4uKYOnVqPProo/2ZKwAwyuUcLp988kmcd9558fDDDx/R/jt27IjLL788qquro7m5OX7yk5/EwoUL4/nnn895sgDA6Jb3RX5kMS8vL1544YWYN2/eYfe544474qWXXopt27Z1j9XW1sYbb7wRr7/+en8fGgAYhQoG+wFef/31qKmp6TF22WWXxapVq+Lf//53jB07ttcxXV1d0dXV1X374MGD8eGHH8a4ceMiLy9vsKcMAAyALMti7969MWHChBgzZmDeVjvo4dLW1hZlZWU9xsrKymL//v3R3t4e5eXlvY6pr6+P5cuXD/bUAIAhsHPnzpg4ceKA3Negh0tE9DpLcujq1OHOnixZsiTq6uq6b3d0dMSpp54aO3fujJKSksGbKAAwYDo7O2PSpEnx5S9/ecDuc9DD5eSTT462trYeY7t3746CgoIYN25cn8cUFRVFUVFRr/GSkhLhAgCJGci3eQz697jMnj07Ghsbe4ytX78+Kisr+3x/CwDA4eQcLh9//HFs2bIltmzZEhGffdx5y5Yt0dLSEhGfXeZZsGBB9/61tbXx7rvvRl1dXWzbti1Wr14dq1atittuu21gngEAMGrkfKlo06ZNcdFFF3XfPvRelOuuuy6efPLJaG1t7Y6YiIgpU6ZEQ0NDLF68OB555JGYMGFCPPTQQ/Gtb31rAKYPAIwmX+h7XIZKZ2dnlJaWRkdHh/e4AEAiBuP1228VAQDJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQjH6Fy4oVK2LKlClRXFwcFRUV0dTU9Ln7r1mzJs4777w49thjo7y8PG644YbYs2dPvyYMAIxeOYfL2rVrY9GiRbF06dJobm6O6urqmDt3brS0tPS5/6uvvhoLFiyIG2+8Md5666149tln469//WvcdNNNX3jyAMDoknO4PPDAA3HjjTfGTTfdFNOmTYv/+7//i0mTJsXKlSv73P9Pf/pTnHbaabFw4cKYMmVKfOMb34ibb745Nm3a9IUnDwCMLjmFy759+2Lz5s1RU1PTY7ympiY2btzY5zFVVVWxa9euaGhoiCzL4oMPPojnnnsurrjiisM+TldXV3R2dvbYAAByCpf29vY4cOBAlJWV9RgvKyuLtra2Po+pqqqKNWvWxPz586OwsDBOPvnkOP744+OXv/zlYR+nvr4+SktLu7dJkyblMk0AYITq15tz8/LyetzOsqzX2CFbt26NhQsXxl133RWbN2+Ol19+OXbs2BG1tbWHvf8lS5ZER0dH97Zz587+TBMAGGEKctl5/PjxkZ+f3+vsyu7du3udhTmkvr4+5syZE7fffntERJx77rlx3HHHRXV1ddxzzz1RXl7e65iioqIoKirKZWoAwCiQ0xmXwsLCqKioiMbGxh7jjY2NUVVV1ecxn376aYwZ0/Nh8vPzI+KzMzUAAEcq50tFdXV18fjjj8fq1atj27ZtsXjx4mhpaem+9LNkyZJYsGBB9/5XXnllrFu3LlauXBnbt2+P1157LRYuXBgzZ86MCRMmDNwzAQBGvJwuFUVEzJ8/P/bs2RN33313tLa2xvTp06OhoSEmT54cERGtra09vtPl+uuvj71798bDDz8cP/rRj+L444+Piy++OO69996BexYAwKiQlyVwvaazszNKS0ujo6MjSkpKhns6AMARGIzXb79VBAAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMvoVLitWrIgpU6ZEcXFxVFRURFNT0+fu39XVFUuXLo3JkydHUVFRnH766bF69ep+TRgAGL0Kcj1g7dq1sWjRolixYkXMmTMnfvWrX8XcuXNj69atceqpp/Z5zNVXXx0ffPBBrFq1Kr7yla/E7t27Y//+/V948gDA6JKXZVmWywGzZs2KGTNmxMqVK7vHpk2bFvPmzYv6+vpe+7/88svxne98J7Zv3x4nnHBCvybZ2dkZpaWl0dHRESUlJf26DwBgaA3G63dOl4r27dsXmzdvjpqamh7jNTU1sXHjxj6Peemll6KysjLuu+++OOWUU+LMM8+M2267Lf75z38e9nG6urqis7OzxwYAkNOlovb29jhw4ECUlZX1GC8rK4u2trY+j9m+fXu8+uqrUVxcHC+88EK0t7fH97///fjwww8P+z6X+vr6WL58eS5TAwBGgX69OTcvL6/H7SzLeo0dcvDgwcjLy4s1a9bEzJkz4/LLL48HHnggnnzyycOedVmyZEl0dHR0bzt37uzPNAGAESanMy7jx4+P/Pz8XmdXdu/e3esszCHl5eVxyimnRGlpaffYtGnTIsuy2LVrV5xxxhm9jikqKoqioqJcpgYAjAI5nXEpLCyMioqKaGxs7DHe2NgYVVVVfR4zZ86ceP/99+Pjjz/uHnv77bdjzJgxMXHixH5MGQAYrXK+VFRXVxePP/54rF69OrZt2xaLFy+OlpaWqK2tjYjPLvMsWLCge/9rrrkmxo0bFzfccENs3bo1Xnnllbj99tvje9/7XhxzzDED90wAgBEv5+9xmT9/fuzZsyfuvvvuaG1tjenTp0dDQ0NMnjw5IiJaW1ujpaWle/8vfelL0djYGD/84Q+jsrIyxo0bF1dffXXcc889A/csAIBRIefvcRkOvscFANIz7N/jAgAwnIQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAkQ7gAAMkQLgBAMoQLAJAM4QIAJKNf4bJixYqYMmVKFBcXR0VFRTQ1NR3Rca+99loUFBTE+eef35+HBQBGuZzDZe3atbFo0aJYunRpNDc3R3V1dcydOzdaWlo+97iOjo5YsGBBfPOb3+z3ZAGA0S0vy7IslwNmzZoVM2bMiJUrV3aPTZs2LebNmxf19fWHPe473/lOnHHGGZGfnx8vvvhibNmy5bD7dnV1RVdXV/ftzs7OmDRpUnR0dERJSUku0wUAhklnZ2eUlpYO6Ot3Tmdc9u3bF5s3b46ampoe4zU1NbFx48bDHvfEE0/EO++8E8uWLTuix6mvr4/S0tLubdKkSblMEwAYoXIKl/b29jhw4ECUlZX1GC8rK4u2trY+j/n73/8ed955Z6xZsyYKCgqO6HGWLFkSHR0d3dvOnTtzmSYAMEIdWUn8l7y8vB63syzrNRYRceDAgbjmmmti+fLlceaZZx7x/RcVFUVRUVF/pgYAjGA5hcv48eMjPz+/19mV3bt39zoLExGxd+/e2LRpUzQ3N8ctt9wSEREHDx6MLMuioKAg1q9fHxdffPEXmD4AMJrkdKmosLAwKioqorGxscd4Y2NjVFVV9dq/pKQk3nzzzdiyZUv3VltbG1/96ldjy5YtMWvWrC82ewBgVMn5UlFdXV1ce+21UVlZGbNnz45f//rX0dLSErW1tRHx2ftT3nvvvXjqqadizJgxMX369B7Hn3TSSVFcXNxrHADgf8k5XObPnx979uyJu+++O1pbW2P69OnR0NAQkydPjoiI1tbW//mdLgAA/ZHz97gMh8H4HDgAMLiG/XtcAACGk3ABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGQIFwAgGcIFAEiGcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGQIFwAgGcIFAEiGcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGQIFwAgGcIFAEiGcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGQIFwAgGcIFAEiGcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGQIFwAgGcIFAEiGcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZPQrXFasWBFTpkyJ4uLiqKioiKampsPuu27durj00kvjxBNPjJKSkpg9e3b8/ve/7/eEAYDRK+dwWbt2bSxatCiWLl0azc3NUV1dHXPnzo2WlpY+93/llVfi0ksvjYaGhti8eXNcdNFFceWVV0Zzc/MXnjwAMLrkZVmW5XLArFmzYsaMGbFy5crusWnTpsW8efOivr7+iO7jnHPOifnz58ddd93V5z/v6uqKrq6u7tudnZ0xadKk6OjoiJKSklymCwAMk87OzigtLR3Q1++czrjs27cvNm/eHDU1NT3Ga2pqYuPGjUd0HwcPHoy9e/fGCSeccNh96uvro7S0tHubNGlSLtMEAEaonMKlvb09Dhw4EGVlZT3Gy8rKoq2t7Yju4/77749PPvkkrr766sPus2TJkujo6Ojedu7cmcs0AYARqqA/B+Xl5fW4nWVZr7G+PPPMM/Gzn/0sfvvb38ZJJ5102P2KioqiqKioP1MDAEawnMJl/PjxkZ+f3+vsyu7du3udhflva9eujRtvvDGeffbZuOSSS3KfKQAw6uV0qaiwsDAqKiqisbGxx3hjY2NUVVUd9rhnnnkmrr/++nj66afjiiuu6N9MAYBRL+dLRXV1dXHttddGZWVlzJ49O379619HS0tL1NbWRsRn709577334qmnnoqIz6JlwYIF8eCDD8bXv/717rM1xxxzTJSWlg7gUwEARrqcw2X+/PmxZ8+euPvuu6O1tTWmT58eDQ0NMXny5IiIaG1t7fGdLr/61a9i//798YMf/CB+8IMfdI9fd9118eSTT37xZwAAjBo5f4/LcBiMz4EDAINr2L/HBQBgOAkXACAZwgUASIZwAQCSIVwAgGQIFwAgGcIFAEiGcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGQIFwAgGcIFAEiGcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGQIFwAgGcIFAEiGcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGQIFwAgGcIFAEiGcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASIZwAQCSIVwAgGQIFwAgGcIFAEiGcAEAkiFcAIBkCBcAIBnCBQBIhnABAJIhXACAZAgXACAZwgUASEa/wmXFihUxZcqUKC4ujoqKimhqavrc/Tds2BAVFRVRXFwcU6dOjUcffbRfkwUARrecw2Xt2rWxaNGiWLp0aTQ3N0d1dXXMnTs3Wlpa+tx/x44dcfnll0d1dXU0NzfHT37yk1i4cGE8//zzX3jyAMDokpdlWZbLAbNmzYoZM2bEypUru8emTZsW8+bNi/r6+l7733HHHfHSSy/Ftm3busdqa2vjjTfeiNdff73Px+jq6oqurq7u2x0dHXHqqafGzp07o6SkJJfpAgDDpLOzMyZNmhQfffRRlJaWDsydZjno6urK8vPzs3Xr1vUYX7hwYXbBBRf0eUx1dXW2cOHCHmPr1q3LCgoKsn379vV5zLJly7KIsNlsNpvNNgK2d955J5fc+FwFkYP29vY4cOBAlJWV9RgvKyuLtra2Po9pa2vrc//9+/dHe3t7lJeX9zpmyZIlUVdX1337o48+ismTJ0dLS8vAFRv9cqienf0aftbi6GEtji7W4+hx6IrJCSecMGD3mVO4HJKXl9fjdpZlvcb+1/59jR9SVFQURUVFvcZLS0v9S3iUKCkpsRZHCWtx9LAWRxfrcfQYM2bgPsSc0z2NHz8+8vPze51d2b17d6+zKoecfPLJfe5fUFAQ48aNy3G6AMBollO4FBYWRkVFRTQ2NvYYb2xsjKqqqj6PmT17dq/9169fH5WVlTF27NgcpwsAjGY5n7upq6uLxx9/PFavXh3btm2LxYsXR0tLS9TW1kbEZ+9PWbBgQff+tbW18e6770ZdXV1s27YtVq9eHatWrYrbbrvtiB+zqKgoli1b1uflI4aWtTh6WIujh7U4uliPo8dgrEXOH4eO+OwL6O67775obW2N6dOnxy9+8Yu44IILIiLi+uuvj3/84x/xxz/+sXv/DRs2xOLFi+Ott96KCRMmxB133NEdOgAAR6pf4QIAMBz8VhEAkAzhAgAkQ7gAAMkQLgBAMo6acFmxYkVMmTIliouLo6KiIpqamj53/w0bNkRFRUUUFxfH1KlT49FHHx2imY58uazFunXr4tJLL40TTzwxSkpKYvbs2fH73/9+CGc7suX6d3HIa6+9FgUFBXH++ecP7gRHkVzXoqurK5YuXRqTJ0+OoqKiOP3002P16tVDNNuRLde1WLNmTZx33nlx7LHHRnl5edxwww2xZ8+eIZrtyPXKK6/ElVdeGRMmTIi8vLx48cUX/+cxA/LaPWC/evQF/OY3v8nGjh2bPfbYY9nWrVuzW2+9NTvuuOOyd999t8/9t2/fnh177LHZrbfemm3dujV77LHHsrFjx2bPPffcEM985Ml1LW699dbs3nvvzf7yl79kb7/9drZkyZJs7Nix2d/+9rchnvnIk+taHPLRRx9lU6dOzWpqarLzzjtvaCY7wvVnLa666qps1qxZWWNjY7Zjx47sz3/+c/baa68N4axHplzXoqmpKRszZkz24IMPZtu3b8+ampqyc845J5s3b94Qz3zkaWhoyJYuXZo9//zzWURkL7zwwufuP1Cv3UdFuMycOTOrra3tMXbWWWdld955Z5/7//jHP87OOuusHmM333xz9vWvf33Q5jha5LoWfTn77LOz5cuXD/TURp3+rsX8+fOzn/70p9myZcuEywDJdS1+97vfZaWlpdmePXuGYnqjSq5r8fOf/zybOnVqj7GHHnoomzhx4qDNcTQ6knAZqNfuYb9UtG/fvti8eXPU1NT0GK+pqYmNGzf2eczrr7/ea//LLrssNm3aFP/+978Hba4jXX/W4r8dPHgw9u7dO6C/BDoa9XctnnjiiXjnnXdi2bJlgz3FUaM/a/HSSy9FZWVl3HfffXHKKafEmWeeGbfddlv885//HIopj1j9WYuqqqrYtWtXNDQ0RJZl8cEHH8Rzzz0XV1xxxVBMmf8wUK/d/fp16IHU3t4eBw4c6PUjjWVlZb1+nPGQtra2Pvffv39/tLe3R3l5+aDNdyTrz1r8t/vvvz8++eSTuPrqqwdjiqNGf9bi73//e9x5553R1NQUBQXD/qc9YvRnLbZv3x6vvvpqFBcXxwsvvBDt7e3x/e9/Pz788EPvc/kC+rMWVVVVsWbNmpg/f37861//iv3798dVV10Vv/zlL4diyvyHgXrtHvYzLofk5eX1uJ1lWa+x/7V/X+PkLte1OOSZZ56Jn/3sZ7F27do46aSTBmt6o8qRrsWBAwfimmuuieXLl8eZZ545VNMbVXL5uzh48GDk5eXFmjVrYubMmXH55ZfHAw88EE8++aSzLgMgl7XYunVrLFy4MO66667YvHlzvPzyy7Fjxw4/OzNMBuK1e9j/t2z8+PGRn5/fq5Z3797dq8wOOfnkk/vcv6CgIMaNGzdocx3p+rMWh6xduzZuvPHGePbZZ+OSSy4ZzGmOCrmuxd69e2PTpk3R3Nwct9xyS0R89uKZZVkUFBTE+vXr4+KLLx6SuY80/fm7KC8vj1NOOSVKS0u7x6ZNmxZZlsWuXbvijDPOGNQ5j1T9WYv6+vqYM2dO3H777RERce6558Zxxx0X1dXVcc899zhDP4QG6rV72M+4FBYWRkVFRTQ2NvYYb2xsjKqqqj6PmT17dq/9169fH5WVlTF27NhBm+tI15+1iPjsTMv1118fTz/9tOvGAyTXtSgpKYk333wztmzZ0r3V1tbGV7/61diyZUvMmjVrqKY+4vTn72LOnDnx/vvvx8cff9w99vbbb8eYMWNi4sSJgzrfkaw/a/Hpp5/GmDE9X+ry8/Mj4v//3z5DY8Beu3N6K+8gOfTxtlWrVmVbt27NFi1alB133HHZP/7xjyzLsuzOO+/Mrr322u79D32kavHixdnWrVuzVatW+Tj0AMl1LZ5++umsoKAge+SRR7LW1tbu7aOPPhqupzBi5LoW/82nigZOrmuxd+/ebOLEidm3v/3t7K233so2bNiQnXHGGdlNN900XE9hxMh1LZ544omsoKAgW7FiRfbOO+9kr776alZZWZnNnDlzuJ7CiLF3796subk5a25uziIie+CBB7Lm5ubuj6YP1mv3UREuWZZljzzySDZ58uSssLAwmzFjRrZhw4buf3bddddlF154YY/9//jHP2Zf+9rXssLCwuy0007LVq5cOcQzHrlyWYsLL7wwi4he23XXXTf0Ex+Bcv27+E/CZWDluhbbtm3LLrnkkuyYY47JJk6cmNXV1WWffvrpEM96ZMp1LR566KHs7LPPzo455pisvLw8++53v5vt2rVriGc98vzhD3/43P/+D9Zrd16WOVcGAKRh2N/jAgBwpIQLAJAM4QIAJEO4AADJEC4AQDKECwCQDOECACRDuAAAyRAuAEAyhAsAkAzhAgAk4/8BrQWhjBP+6s8AAAAASUVORK5CYII=",
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
    "import matplotlib.patches as patches\n",
    "\n",
    "class Canvas:\n",
    "\n",
    "    def __init__(self):\n",
    "        self.fig, self.ax = plt.subplots()\n",
    "\n",
    "    def draw_circle(self, circle):\n",
    "        x = circle.x\n",
    "        y = circle.y\n",
    "        radius = circle.radius\n",
    "        color = circle.color\n",
    "        circle = patches.Circle((x, y), radius, color=color)\n",
    "        self.ax.add_patch(circle)\n",
    "\n",
    "    def show(self):\n",
    "        plt.axis('equal')\n",
    "        plt.show()\n",
    "\n",
    "class Circle:\n",
    "\n",
    "    def __init__(self, x, y, radius, color):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        self.radius = radius\n",
    "        self.color = color\n",
    "# Example usage:\n",
    "canvas = Canvas()\n",
    "circle1 = Circle(6, 4, 1, \"green\")\n",
    "canvas.draw_circle(circle1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "99bc2a21-8674-477b-ae6f-46cd1692ba10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
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
    "import matplotlib.patches as patches\n",
    "\n",
    "class Canvas:\n",
    "\n",
    "    def __init__(self):\n",
    "        self.fig, self.ax = plt.subplots()\n",
    "\n",
    "    def draw_circle(self, circle):\n",
    "        x = circle.x\n",
    "        y = circle.y\n",
    "        radius = circle.radius\n",
    "        color = circle.color\n",
    "        circle = patches.Circle((x, y), radius, color=color)\n",
    "        self.ax.add_patch(circle)\n",
    "\n",
    "    def show(self):\n",
    "        plt.axis('equal')\n",
    "        plt.show()\n",
    "\n",
    "class Circle:\n",
    "\n",
    "    def __init__(self, x, y, radius, color):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        self.radius = radius\n",
    "        self.color = color\n",
    "# Example usage:\n",
    "canvas = Canvas()\n",
    "circle1 = Circle(6, 4, 1, \"green\")\n",
    "canvas.draw_circle(circle1)\n",
    "canvas.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "7e8d11ff-cc1c-4718-b37e-6de2b3eb0df5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "D class method\n",
      "[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]\n"
     ]
    }
   ],
   "source": [
    "class A:\n",
    "    def show(self):\n",
    "        print(\"A class method\")\n",
    "\n",
    "class B(A):\n",
    "    def show(self):\n",
    "        print(\"B class method\")\n",
    "\n",
    "class C(A):\n",
    "    def show(self):\n",
    "        print(\"C class method\")\n",
    "\n",
    "class D(B, C):\n",
    "    def show(self):\n",
    "        print(\"D class method\")\n",
    "d_obj = D()\n",
    "d_obj.show()\n",
    "print(D.mro())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e03540c-95cd-46b7-b709-c89cce52fb57",
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
