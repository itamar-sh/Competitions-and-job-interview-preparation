# Competition Google Kick Start 2022 ROUND E 
My place was 3204 out of 10K+ participants.
I succeeded to complete only 3 questions while 1 of them only Partially.

## first question: Coloring Game
### overview
John loves to play computer games. He recently discovered an interesting game. In the game there are N cells, which are aligned in a row from left to right and are numbered with consecutive integers starting from 1. Initially, all cells are coloured white. A cell is valid if it has white color and it does not have any adjacent red colored cell. On each turn, a player paints any valid cell with the red color. The game ends when no valid cells are present. The score of the player is equal to the number of cells they paint.

To master the game, John is practicing against a bot. The bot is poorly trained and it always paints the first valid cell from the left. John on the other hand is playing the game very carefully and he can choose any valid cell. The bot makes the first move and the players take turns alternately.

Find the maximum achievable score by the bot, assuming that John is playing optimally to minimize the score of his opponent.

### Input
The first line of the input gives the number of test cases, T. T test cases follow.
The only line of each test case contains an integer N representing the number of cells in the game.
### Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum achievable score by the bot given that John is playing optimally.

## second question: Students and Mentors
A group of N students prepares together for upcoming programming competitions such as Kick Start and Code Jam by Google. To help each other prepare, it was decided that each student will pick a mentor among other students. A mentor will help their mentee to solve problems, learn algorithms, track their progress, and will generally support them throughout preparation.

Each student will have exactly one mentor among all other students, and a person can be a mentor to multiple people. For every student i we know their rating Ri which approximates how good that student is at programming competitions. Because it is believed that a mentor should not be much stronger than their mentee, a student j can be a mentor of student i only if Rj≤2×Ri. Note that a mentor can even have a rating that is lower or equal to their mentee's rating.

Unsurprisingly, each student wants to have the strongest possible mentor. For each student, can you help to figure out what is the highest possible rating of a mentor they can pick?

### Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of two lines.

The first line of each test case contains an integer N, representing the number of students in a group.

The second line of each test case contains N integers R1 R2 R3 … RN where Ri is a rating of the i-th student.

### Output
For each test case, output one line containing Case #x: M1 M2 M3 … MN where x is the test case number (starting from 1), and Mi is the maximum possible rating of the i-th student's mentor or −1 if there are no suitable mentors for that student.

## Matching Palindrome
You are given a palindrome string P of length N consisting of only lowercase letters of the English alphabet. Find the shortest non-empty palindrome string Q such that P concatenated with Q forms a palindrome. Formally, the string PQ forms a palindrome.

### Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of two lines. The first line of each test case contains an integer N denoting the length of the string P. The second line of each test case contains a palindrome string P of length N.

### Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the non-empty palindrome string Q as described above.