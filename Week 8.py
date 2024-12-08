{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bf70690e-088f-4626-8c33-3e5fb91050f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "file1=open(\"t1.txt\",\"w\",encoding=\"utf-8\")\n",
    "file2=open(\"t2.txt\",\"w\")\n",
    "file1.write(\"hello\")\n",
    "file2.write(\"world!\")\n",
    "file1.close()\n",
    "file2.close()\n",
    "file1=open(\"t1.txt\",\"r\")\n",
    "data1=file1.read()\n",
    "file2=open(\"t2.txt\",\"r\")\n",
    "data2=file2.read()\n",
    "file1.close()\n",
    "file2.close()\n",
    "file3=open(\"t3.txt\",\"w\")\n",
    "file3.write(data1+\" \"+data2)\n",
    "file3.close()\n",
    "file3=open(\"t3.txt\",\"r\")\n",
    "data=file3.read()\n",
    "file3.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dbedc9c8-ac9e-4eef-abcc-7ad7683bbfc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter word to be searched: hello\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "word found\n"
     ]
    }
   ],
   "source": [
    "file=open(\"t3.txt\",\"r\")\n",
    "data=file.read()                 \n",
    "file.close()\n",
    "def check_word(data,word):\n",
    "    \n",
    "    words=data.split(\" \")\n",
    "    for i in words:\n",
    "        if word==i:\n",
    "            print(\"word found\")\n",
    "            break\n",
    "    else:\n",
    "            print(\"not found\")\n",
    "word=input(\"Enter word to be searched:\")\n",
    "check_word(data,word)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7cf1bb54-0f1a-45cd-b3e2-59af4ee8ed0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Most repeated word: mango\n"
     ]
    }
   ],
   "source": [
    "count=0\n",
    "max_count=0\n",
    "words=[]\n",
    "file=open(\"text.txt\",\"w\") \n",
    "# apple banana apple mango banana mango orange mango\n",
    "file.write(\"apple banana apple mango banana mango orange mango\")\n",
    "file.close()\n",
    "file=open(\"text.txt\",\"r\") \n",
    "for line in file:\n",
    "    string=line.lower().replace(',','').replace('.','').split(\" \")\n",
    "    for s in string:\n",
    "        words.append(s)\n",
    "for i in range (0,len(words)):\n",
    "    count=1\n",
    "    for j in range (i+1,len(words)):\n",
    "        if words[i]==words[j]:\n",
    "            count=count+1\n",
    "        if count>max_count:\n",
    "            max_count=count\n",
    "            word=words[i]\n",
    "print(\"Most repeated word:\",word)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "dbc074d5-6b3e-447e-9f9d-8cdb24f5494e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total words: 8\n",
      "Total Vowels:\n",
      "19\n",
      "Total con:\n",
      "24\n",
      "Total lower:\n",
      "43\n",
      "Total upper:\n",
      "0\n",
      "Total space:\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "file1 = open(\"text.txt\", \"r\")\n",
    "data=file1.read()  #hello world\n",
    "file1.close()\n",
    "def diaplay():\n",
    "    vowel= 0\n",
    "    space=0\n",
    "    con=0\n",
    "    lower=0\n",
    "    upper=0\n",
    "    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']\n",
    "    words=data.split()\n",
    "    print(\"Total words:\",len(words))\n",
    "    for letter in data:\n",
    "        if letter in vowels:\n",
    "            vowel = vowel+1\n",
    "        elif letter==\" \":\n",
    "                space=space+1\n",
    "        else:\n",
    "            con=con+1\n",
    "        if letter.islower():\n",
    "            lower=lower+1\n",
    "        if letter.isupper():\n",
    "            upper=upper+1\n",
    "\n",
    "    print(\"Total Vowels:\")\n",
    "    print(vowel)\n",
    "    print(\"Total con:\")\n",
    "    print(con)\n",
    "    print(\"Total lower:\")\n",
    "    print(lower)\n",
    "    print(\"Total upper:\")\n",
    "    print(upper)\n",
    "    print(\"Total space:\")\n",
    "    print(space)\n",
    "diaplay()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b911f300-21eb-40e5-8c22-b3bde711556f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'apple', 'mango', 'banana', 'mango', 'orange', 'mango']\n",
      "['elppa', 'ananab', 'elppa', 'ognam', 'ananab', 'ognam', 'egnaro', 'ognam']\n"
     ]
    }
   ],
   "source": [
    "file = open (\"text.txt\",\"r\")\n",
    "r=file.read()\n",
    "word=r.split() \n",
    "print(word)\n",
    "l1 =[]\n",
    "for i in word:\n",
    "    l1.append(i[::-1])\n",
    "print (l1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fcb06571-574c-47c4-9bf8-b6ff9cd4ab60",
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
