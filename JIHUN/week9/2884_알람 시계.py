{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "not enough values to unpack (expected 2, got 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m a, b \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mmap\u001b[39m(\u001b[38;5;28mint\u001b[39m, \u001b[38;5;28minput\u001b[39m()\u001b[38;5;241m.\u001b[39msplit())\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m b \u001b[38;5;241m-\u001b[39m \u001b[38;5;241m45\u001b[39m \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m0\u001b[39m:\n\u001b[0;32m      4\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m a \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m0\u001b[39m:\n",
      "\u001b[1;31mValueError\u001b[0m: not enough values to unpack (expected 2, got 0)"
     ]
    }
   ],
   "source": [
    "a, b = map(int, input().split())\n",
    "\n",
    "if b < 45:\n",
    "    b += 15\n",
    "    if a == 0:\n",
    "        a = 23\n",
    "    else:\n",
    "        a -=1\n",
    "else:\n",
    "    b -= 45\n",
    "\n",
    "print(a, b)"
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
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
