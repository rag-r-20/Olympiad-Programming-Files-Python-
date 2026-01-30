**Questions**
  
1. Add two numbers:  
You are given 2 integers a, b as standard inputs to your program. Print the sum a+b on a single line.
  
2. Grid Sums:  
Given as input the integers N and M, and an NxM grid, print the sum of each row of the grid on a separate line.
  
3. Prime numbers:  
   Given a number k, find the smallest number n greater than 1 that is not divisible by the first k prime numbers, but is not prime.

4. Euclidean Algorithm:  
   The greatest common divisor of two positive integer numbers a,b, is calculated efficiently using the Euclidean algorithm. Two numbers
   a, b are relative prime if their greatest common divisor is 1 e.g.. gcd(a, b) = 1; same three numbers are relative primes if gcd(a, b, c) = 1. 
   This problem requires you to learn this Euclidean algorithm and apply it to the following problem.  
   Given 3 positive integers a, bandc you must determine if these numbers are relative prime.

6. String Transformations:
   - Reverse the order of words in the string.   
   - For each word, reverse the characters within the word if the word starts with a consonant and contains an odd number of characters.

7. Positronic Dillema:  
   In an intriguing fusion of technology and science fiction, Grey, an ambitious computer scientist, has embarked on creating a positronic brain,
   a concept borrowed from his favourite sci-fi narratives. These advanced artificial brains operate based on deterministically sequenced thought
   chains. However, Grey encountered a critical issue during his experimental trials: some positronic brains entered an unresponsive state, freezing
   indefinitely. Upon thorough investigation, Grey uncovered that these freezes were caused by the brains getting trapped in infinite thought cycles.
   This poses a significant risk to the functionality and reliability of these advanced artificial intelligence systems.  
   Grey seeks your expertise in analyzing the new designs of positronic brains. He has provided a map detailing all the possible thought connections
   in his designs. Your task is to analyze these newly designed architectures and determine if such loops are still possible.  
   *Input*  
   On the first line, an integer n counting the number of connections in the design On each subsequent line, a pair of integers a, b separated by
   commas with the meaning of thought a leads to thought b. A thought can be self-referencing, meaning that a thought can lead to itself.  
   *Output*  
   One capitalised word SAFE if the design contains no cycles, UNSAFE otherwise.
