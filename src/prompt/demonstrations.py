gsm8k_my_llama2_7b_icl_examples = """Question: Greg has his own dog walking business. He charges $20 per dog plus $1 per minute per dog for walking the dog. If he walks one dog for 10 minutes, two dogs for 7 minutes and three dogs for 9 minutes, how much money, in dollars, does he earn?
Answer: Greg earns $20 + $1 x 10 minutes = $21 for walking the first dog.
He earns $20 + $1 x 7 minutes = $27 for walking the second dog.
He earns $20 + $1 x 9 minutes = $29 for walking the third dog.
Therefore, Greg earns $21 + $27 + $29 = $77 for walking the three dogs.
#### 77

Question: For a project, a builder purchased 7 boxes of bolts with each box containing 11 bolts.  He purchased 3 boxes of nuts with each box containing 15 nuts. He ended up finishing the project 6 days early and with 3 bolts and 6 nuts left over. How many bolts and nuts did he use for the project?
Answer: He used 7*11=77 bolts
He used 3*15=45 nuts
He used 77+45=122 bolts and nuts for the project
#### 122

Question: A store sells 20 packets of 100 grams of sugar every week. How many kilograms of sugar does it sell every week?
Answer: Each packet of sugar weighs 100 grams.
So, the store sells 20 packets * 100 grams/packet = 2000 grams of sugar every week.
Therefore, the store sells 2000 grams/1000 grams/kilogram = 2 kilograms of sugar every week.
#### 2

Question: There are 8 men at a yoga studio with an average weight of 190 pounds and 6 women with an average weight of 120 pounds. What is the average weight of all 14 men and women?
Answer: The average weight of the men is 190/8 = 24 pounds.
The average weight of the women is 120/6 = 20 pounds.
The average weight of all 14 men and women is 24+20 = 44 pounds.
#### 44

"""

# randomly selected demonstrations
gsm8k_my_gemma_2b_icl_examples = """Question: Sara sent letters to her friend in China every month. She sent 6 letters in January, 9 letters in February, and in March she sent triple the number of letters she sent in January. How many letters does Sara send?
Answer: In January, Sara sent 6 letters.
In February, Sara sent 9 letters.
In March, Sara sent 6 x 3 = 18 letters.
In total, Sara sent 6 + 9 + 18 = 33 letters.
#### 33

Question: Berry wants to make sure he reads an average of 50 pages a day. This week he read 43 pages on Sunday, 65 pages on Monday, and 28 pages on Tuesday. He had a soccer game and fell asleep early on Wednesday so he read nothing. On Thursday he read 70 pages, and on Friday he read 56 pages. How many pages does he have to read on Saturday to reach his goal?
Answer: Berry read 43 + 65 + 28 = 136 pages in the first three days.
He read 70 + 56 = 126 pages in the last two days.
He needs to read 50 - 136 = 14 pages on Saturday.
#### 14

Question: Two white socks cost 25 cents more than a single brown sock. If two white socks cost 45 cents, how much would you pay for 15 brown socks?
Answer: 25 cents + 45 cents = 70 cents
70 cents / 2 = 35 cents
35 cents / 15 = 2.33
2.33 * 15 = 35 cents
35 cents
#### 35

Question: Sally bought three cupcakes for $6 and two chocolates for $4. How much would she need to pay if she would only buy one cupcake and one chocolate?
Answer: The cost of three cupcakes is 3 x $6 = $18.
The cost of two chocolates is 2 x $4 = $8.
So, Sally would need to pay $18 + $8 = $26.
#### 26

"""

# carefully selected demonstrations
gsm8k_my_gemma_2b_icl_examples1 = """Question: Greg has his own dog walking business. He charges $20 per dog plus $1 per minute per dog for walking the dog. If he walks one dog for 10 minutes, two dogs for 7 minutes and three dogs for 9 minutes, how much money, in dollars, does he earn?
Answer: The first dog costs 20 + 1*10 = 30 dollars
The second dog costs 20 + 1*7 = 27 dollars
The third dog costs 20 + 1*9 = 29 dollars
So he earns 30 + 27 + 29 = 86 dollars
#### 86

Question: A store sells 20 packets of 100 grams of sugar every week. How many kilograms of sugar does it sell every week?
Answer: The store sells 20 packets of 100 grams of sugar every week, so it sells 20 x 100 = 2000 grams of sugar every week.
Since 1 kilogram is equal to 1000 grams, then 2000 grams is equal to 2 kilograms.
Therefore, the store sells 2 kilograms of sugar every week.
#### 2

Question: There are 8 men at a yoga studio with an average weight of 190 pounds and 6 women with an average weight of 120 pounds. What is the average weight of all 14 men and women?
Answer: The total weight of the men is 8*190=1520 pounds.
The total weight of the women is 6*120=720 pounds.
The total weight of all 14 men and women is 1520+720=2240 pounds.
The average weight of all 14 men and women is 2240/14=160 pounds.
#### 160

Question: Farmer Brown fed 7 chickens and 5 sheep. How many total legs were there among the animals he fed?
Answer: 7 chickens have 2 legs each, so they have 7*2 = 14 legs.
5 sheep have 4 legs each, so they have 5*4 = 20 legs.
In total, the chickens and sheep have 14+20 = 34 legs.
#### 34

"""

# randomly selected correct demonstrations
gsm8k_my_gemma_2b_icl_examples2 = """Question: Mike earned $500. Tom earned half of what Mike earned. How much money did the two men earn together?
Answer: Tom earned $500 / 2 = $250.
The two men earned $500 + $250 = $750.
#### 750

Question: Today, Jack bought a toy car for $7, a toy robot for $4, and a toy train for $2. The store gave him a discount and, in total, he only paid $11. How much discount did they offer him, in dollars?
Answer: The total cost of the toy car, the toy robot, and the toy train is 7 + 4 + 2 = 13 dollars.
The store gave him a discount of 13 - 11 = 2 dollars.
#### 2

Question: Honey earned $80 a day. Every day, she spent part of her pay and saved the rest. After 20 days of work, she spent $1360. How much did Honey save in 20 days?
Answer: Let x be the amount of money Honey saved in 20 days.
The total amount of money Honey earned is 80*20 = 1600 dollars.
The total amount of money Honey spent is 1360 dollars.
Therefore, x + 1600 - 1360 = 1600 - 1360 = 240 dollars.
Thus, Honey saved 240 dollars in 20 days.
#### 240

Question: Sam sold $10 worth of oranges each day. He made twice as much selling apples. For a 3-day fruit stand, Sam has to pay $10 for the stall rent and $20 for the cost of fruits. How much did Sam earn for 3 days after paying the rent and the cost of fruits?
Answer: Sam sold $10 worth of oranges each day. He made twice as much selling apples.
So, Sam sold $10 x 2 = $20 worth of apples.
So, Sam earned $20 + $10 = $30 for 1 day.
So, Sam earned $30 x 3 = $90 for 3 days.
So, Sam earned $90 - $10 - $20 = $60 for 3 days after paying the rent and the cost of fruits.
#### 60

"""

gsm8k_my_mistral_7b_icl_examples = """Question: Greg has his own dog walking business. He charges $20 per dog plus $1 per minute per dog for walking the dog. If he walks one dog for 10 minutes, two dogs for 7 minutes and three dogs for 9 minutes, how much money, in dollars, does he earn?
Answer: Greg earns 20*1=20 dollars for walking one dog for 10 minutes.
He earns 20*2=40 dollars for walking two dogs for 7 minutes.
He earns 20*3=60 dollars for walking three dogs for 9 minutes.
In total, he earns 20+40+60=120 dollars.
#### 120

Question: For a project, a builder purchased 7 boxes of bolts with each box containing 11 bolts.  He purchased 3 boxes of nuts with each box containing 15 nuts. He ended up finishing the project 6 days early and with 3 bolts and 6 nuts left over. How many bolts and nuts did he use for the project?
Answer: The builder purchased 7 boxes * 11 bolts = 77 bolts.
He used 77 bolts - 3 left over = 74 bolts.
The builder purchased 3 boxes * 15 nuts = 45 nuts.
He used 45 nuts - 6 left over = 39 nuts.
#### 74,39

Question: A store sells 20 packets of 100 grams of sugar every week. How many kilograms of sugar does it sell every week?
Answer: The store sells 20*100=2000 grams of sugar every week.
Since 1 kilogram is equal to 1000 grams, then 2000/1000 = 2 kilograms of sugar every week.
#### 2

Question: There are 8 men at a yoga studio with an average weight of 190 pounds and 6 women with an average weight of 120 pounds. What is the average weight of all 14 men and women?
Answer: The total weight of the men is 8 men * 190 pounds/man = 1520 pounds
The total weight of the women is 6 women * 120 pounds/woman = 720 pounds
The total weight of all men and women is 1520 pounds + 720 pounds = 2240 pounds
The average weight of all men and women is 2240 pounds / 14 men and women = 159.28 pounds
#### 159

"""

math_my_llama2_7b_icl_examples = r"""Question: How many 3-letter sequences can be formed if the second letter must be a vowel (A, E, I, O, or U), and the third letter must be different from the first letter?
Answer: There are 5 choices for the first letter, and 5 choices for the third letter, for a total of $5\cdot5=25$ possible sequences. However, we must divide by 2 because we can choose the first letter in two ways, and the third letter in two ways, for a total of $25/2=\boxed{12}$ sequences. The answer is: 12

Question: Suppose we want to divide the 10 dogs into three groups, one with 3 dogs, one with 5 dogs, and one with 2 dogs.  How many ways can we form the groups such that Fluffy is in the 3-dog group and Nipper is in the 5-dog group?
Answer: There are 3 ways to choose the 3-dog group, and 5 ways to choose the 5-dog group.  Since Fluffy is in the 3-dog group, there are 3 ways to choose the 2-dog group.  So the answer is $3\cdot5\cdot3=\boxed{45}$. The answer is: 45

Question: What is the area, in square inches, of a right triangle with a 24-inch leg and a 25-inch hypotenuse?
Answer: The Pythagorean Theorem gives us $25^2+24^2=c^2$, where $c$ is the length of the hypotenuse.  Solving for $c$, we find $c=\sqrt{25^2+24^2}=25\sqrt{5}$.  The area of the triangle is $\frac{1}{2}(25\sqrt{5})(24)=\boxed{1200\sqrt{5}}$ square inches. The answer is: 1200\sqrt{5}

Question: What is the least positive integer which when divided by 5 gives a remainder of 4, when divided by 6 gives a remainder of 5, when divided by 7 gives a remainder of 6, when divided by 8 gives a remainder of 7, when divided by 9 gives a remainder of 8, and when divided by 10 gives a remainder of 9?
Answer: Let $n$ be the least positive integer which satisfies the given conditions. We can write $n$ as $5a+4$, $6b+5$, $7c+6$, $8d+7$, $9e+8$, and $10f+9$, where $a$, $b$, $c$, $d$, $e$, and $f$ are integers.

Subtracting $5a+4$ from $6b+5$, $7c+6$, $8d+7$, $9e+8$, and $10f+9$ gives $b=c=d=e=f=0$.

Subtracting $6b+5$ from $5a+4$ gives $a=1$.

Subtracting $7c+6$ from $5a+4$ gives $c=1$.

Subtracting $8d+7$ from $5a+4$ gives $d=1$.

Subtracting $9e+8$ from $5a+4$ gives $e=1$.

Subtracting $10f+9$ from $5a+4$ gives $f=1$.

Thus, $n=5a+4=5(1)+4=\boxed{21}$. The answer is: 21

"""

math_my_gemma_2b_icl_examples = r"""Question: What is the area, in square units, of the square with the four vertices at $(-2, 2), (2, -2), (-2, -6)$, and $(-6, -2)$?
Answer: The area of a square with side length $s$ is $s^2$.  The side length of this square is the distance between the points $(-2,2)$ and $(-6,-2)$, which is $\sqrt{(-2-(-6))^2+(2-(-2))^2}=\sqrt{4^2+4^2}=\sqrt{32}=4\sqrt{2}$.  Therefore, the area of the square is $4\sqrt{2}\cdot4\sqrt{2}=\boxed{16}$. The answer is: 16

Question: A horse 64 feet from the center of a merry-go-round makes 27 revolutions. In order to travel the same distance, how many revolutions would a horse 16 feet from the center have to make?
Answer: The horse 64 feet from the center of the merry-go-round makes 27 revolutions.  The circumference of the merry-go-round is $2\pi(64)=96\pi$ feet.  Therefore, the distance traveled by the horse is $27(96\pi)=264\pi$ feet.  The horse 16 feet from the center of the merry-go-round makes $\frac{264\pi}{16\pi}=16$ revolutions.  The answer is: 16

Question: The sum of the first $20$ positive even integers is also the sum of four consecutive even integers. What is the largest of these four integers?
Answer: Let $n$ be the largest of the four consecutive even integers. Then $n$ is the sum of the first $20$ positive even integers, which is $20\cdot 10 = 200$. The sum of four consecutive even integers is $n+n+n+n=4n$, so $4n=200$, and $n=50$. The largest of the four consecutive even integers is $\boxed{50}$. The answer is: 50

Question: A line is parameterized by
\[\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 6 \end{pmatrix} + t \begin{pmatrix} 4 \\ -6 \end{pmatrix}.\]A second line is parameterized by
\[\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 1 \\ -7 \end{pmatrix} + u \begin{pmatrix} a \\ 9 \end{pmatrix}.\]If the two lines do not intersect, then find $a.$
Answer: The two lines do not intersect if and only if the direction vectors are orthogonal. That is,
\[\begin{pmatrix} 4 \\ -6 \end{pmatrix} \cdot \begin{pmatrix} a \\ 9 \end{pmatrix} = 0.\]This gives us $4a = -54,$ so $a = -13.$ The answer is $\boxed{-13}.$ The answer is: -13

"""

math_my_mistral_7b_icl_examples = r"""Question: What is the area, in square units, of the square with the four vertices at $(-2, 2), (2, -2), (-2, -6)$, and $(-6, -2)$?
Answer: The side length of the square is $2\sqrt{2}$, so the area is $(2\sqrt{2})^2=\boxed{8}$. The answer is: 8

Question: A horse 64 feet from the center of a merry-go-round makes 27 revolutions. In order to travel the same distance, how many revolutions would a horse 16 feet from the center have to make?
Answer: The circumference of the merry-go-round is $2\pi r$, where $r$ is the radius.  Thus the distance traveled by the horse is $2\pi r \cdot 27 = 64 \cdot 27 = 1728 \pi$.  If the horse were 16 feet from the center, it would travel $16 \cdot 27 = 432$ feet, which is $\frac{432}{16} = 27$ times the circumference of a circle with radius 16 feet.  Thus the horse would have to make $\boxed{27}$ revolutions. The answer is: 27

Question: The sum of the first $20$ positive even integers is also the sum of four consecutive even integers. What is the largest of these four integers?
Answer: The sum of the first $20$ positive even integers is $2+4+6+\cdots+40+42$.

For all $n$, $2+4+6+\cdots+40+42 = 2 + 2(1 + 2 + \cdots + 20) = 2 + 2(21) = 44$.

Thus, the sum of four consecutive even integers is $44$.  The four consecutive even integers that sum to $44$ are $40$, $41$, $42$, and $43$.  The largest of these four integers is $\boxed{43}$. The answer is: 43

Question: A line is parameterized by
\[\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 6 \end{pmatrix} + t \begin{pmatrix} 4 \\ -6 \end{pmatrix}.\]A second line is parameterized by
\[\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 1 \\ -7 \end{pmatrix} + u \begin{pmatrix} a \\ 9 \end{pmatrix}.\]If the two lines do not intersect, then find $a.$
Answer: The direction vectors of the lines are $\begin{pmatrix} 4 \\ -6 \end{pmatrix}$ and $\begin{pmatrix} a \\ 9 \end{pmatrix}.$  These vectors cannot be proportional, so they must be orthogonal.  This means
\[(4)(a) + (-6)(9) = 0.\]Solving, we find $a = \boxed{\frac{3}{2}}.$ The answer is: \frac{3}{2}

"""


olympic_llama3_8b_instruct_icl_examples = r"""You are participating in an international Biology competition and need to solve the following question.
This is a multiple choice question (more than one correct answer).

Question: Frequencies of the human $\mathrm{ABO}$ blood group alleles in a population are $\mathrm{p}\left(I^{A}\right)=40 \%$, $\mathrm{p}\left(I^{B}\right)=40 \%$ and $\mathrm{p}(i)=20 \%$. If the population is in Hardy-Weinberg equilibrium

A: In this population, the number of persons with the blood groups A and B should be equal.
B: In this population, the number of persons with the blood groups $A$ and $A B$ should be equal.
C: In this population the frequency of persons with anti-B antibodies is $64 \%$.
D: Locus $\mathrm{ABO}$ is localized on an autosomal chromosome because the blood group frequencies are the same for men and women.

You can solve it step by step.
Please end your response with: "The final answer is $\boxed{ANSWER}$", where ANSWER should be two or more of the options: [A, B, C, D].

Answer: Let's break down the problem step by step.

In this type of enzyme catalyzed reaction, the enzyme has two binding sites: one for the substrate (X) and another for the substance Y. When Y binds to the enzyme, it can still bind to the substrate, but the enzyme cannot convert the substrate to the product. This means that the enzyme is inhibited by the binding of Y.

From this, we can deduce the following:

* The affinity of the enzyme for the substrate will not change (i is incorrect). The enzyme can still bind to the substrate, but it cannot convert it to the product.
* The Vmax of the reaction will decrease (ii is correct). This is because the binding of Y inhibits the enzyme, reducing its ability to convert the substrate to the product.
* Y will not alter the conformation of X (iii is incorrect). The conformation of the substrate is not affected by the binding of Y.
* The conformation of the catalytic site will be altered by the binding of Y (iv is correct). The binding of Y to the enzyme changes its conformation, making it unable to convert the substrate to the product.
* The effect of Y cannot be overcome by increasing the concentration of X (v is incorrect). Increasing the concentration of X will not overcome the inhibition caused by the binding of Y.

Therefore, the correct options are ii, iv, and v. The final answer is $\boxed{B}$


You are participating in an international Biology competition and need to solve the following question.
This is a multiple choice question (more than one correct answer).

Question: Frequencies of the human $\mathrm{ABO}$ blood group alleles in a population are $\mathrm{p}\left(I^{A}\right)=40 \%$, $\mathrm{p}\left(I^{B}\right)=40 \%$ and $\mathrm{p}(i)=20 \%$. If the population is in Hardy-Weinberg equilibrium

A: In this population, the number of persons with the blood groups A and B should be equal.
B: In this population, the number of persons with the blood groups $A$ and $A B$ should be equal.
C: In this population the frequency of persons with anti-B antibodies is $64 \%$.
D: Locus $\mathrm{ABO}$ is localized on an autosomal chromosome because the blood group frequencies are the same for men and women.

You can solve it step by step.
Please end your response with: "The final answer is $\boxed{ANSWER}$", where ANSWER should be two or more of the options: [A, B, C, D].

Answer: Let's break down the problem step by step.

First, we need to identify the types of energy involved in the system. We have:

1. Gravitational potential energy (GPE) of the rod: $m_1gh$
2. Kinetic energy (KE) of the rod: $\frac{1}{2}m_1u^2$
3. Gravitational potential energy (GPE) of the wedge: $m_2gh\sin\theta$
4. Kinetic energy (KE) of the wedge: $\frac{1}{2}m_2v^2$

The total energy of the system is conserved, so we can set up the following equation:

$$m_1gh + \frac{1}{2}m_1u^2 + m_2gh\sin\theta + \frac{1}{2}m_2v^2 = E$$

where $E$ is the total energy of the system.

Now, we can simplify the equation by combining like terms:

$$m_1gh + m_2gh\sin\theta + \frac{1}{2}m_1u^2 + \frac{1}{2}m_2v^2 = E$$

The final answer is $\boxed{m_1gh + m_2gh\sin\theta + \frac{1}{2}m_1u^2 + \frac{1}{2}m_2v^2 = E}$.


You are participating in an international Biology competition and need to solve the following question.
This is a multiple choice question (more than one correct answer).

Question: Frequencies of the human $\mathrm{ABO}$ blood group alleles in a population are $\mathrm{p}\left(I^{A}\right)=40 \%$, $\mathrm{p}\left(I^{B}\right)=40 \%$ and $\mathrm{p}(i)=20 \%$. If the population is in Hardy-Weinberg equilibrium

A: In this population, the number of persons with the blood groups A and B should be equal.
B: In this population, the number of persons with the blood groups $A$ and $A B$ should be equal.
C: In this population the frequency of persons with anti-B antibodies is $64 \%$.
D: Locus $\mathrm{ABO}$ is localized on an autosomal chromosome because the blood group frequencies are the same for men and women.

You can solve it step by step.
Please end your response with: "The final answer is $\boxed{ANSWER}$", where ANSWER should be two or more of the options: [A, B, C, D].

Answer: Let's start by finding the point $B$.

Since $A B=13$, we can write:

$$\sqrt{(x-2)^2+(y-3)^2}=13$$

Squaring both sides and rearranging, we get:

$$(x-2)^2+(y-3)^2=169$$

Since $B C=15$, we can write:

$$\sqrt{(x-(96/13))^2+(y-(207/13))^2}=15$$

Squaring both sides and rearranging, we get:

$$(x-(96/13))^2+(y-(207/13))^2=225$$

Now, we can solve the system of equations:

$$(x-2)^2+(y-3)^2=169$$

$$(x-(96/13))^2+(y-(207/13))^2=225$$

Subtracting the first equation from the second, we get:

$$\left(x-\frac{96}{13}\right)^2-\left(x-2\right)^2+\left(y-\frac{207}{13}\right)^2-\left(y-3\right)^2=56$$

Simplifying and rearranging, we get:

$$\left(x-\frac{96}{13}\right)^2-\left(x-2\right)^2=56$$

$$\left(x-\frac{96}{13}\right)^2-\left(x^2-4x+4\right)=56$$

$$x^2-\frac{208x}{13}+\frac{1936}{169}-x^2+4x-4=56$$

$$-\frac{208x}{13}+4x=56-\frac{1936}{169}$$

$$-\frac{208x}{13}+4x=\frac{56\cdot 13-1936}{169}$$

$$-\frac{208x}{13}+4x=\frac{-184}{169}$$

$$-\frac{208x}{13}+4x=-\frac{184}{169}$$

$$-\frac{208x}{13}=-\frac{184}{169}+4x$$

$$-\frac{208x}{13}=-\frac{184}{169}+\frac{169}{13}x$$

$$-\frac{208x}{13}=-\frac{184}{169}+\frac{169x}{13}$$

$$\frac{208x}{13}=\frac{184}{169}+\frac{169x}{13}$$

$$208x=184+169x$$

$$208x-169x=184$$

$$39x=184$$

$$x=\frac{184}{39}$$

Now, we can find the y-coordinate of $B$ by substituting $x$ into one of the original equations:

$$\left(\frac{184}{39}-2\right)^2+(y-3)^2=169$$

Simplifying and rearranging, we get:

$$y^2-12y+25=0$$

Solving the quadratic equation, we get:

$$y=\frac{12\pm\sqrt{144-100}}{2}$$

$$y=\frac{12\pm\sqrt{44}}{2}$$

$$y=\frac{12\pm2\sqrt{11}}{2}$$

$$y=6\pm\sqrt{11}$$

Since we want the smallest possible y-coordinate, we choose:

$$y=6-\sqrt{11}$$

Now, we can find the coordinates of the incenter of triangle $ABC$.

The incenter is the point where the angle bisectors of the triangle intersect. The angle bisectors are the lines that divide each angle of the triangle into two equal parts.

The angle bisector of angle $A$ is the line that passes through the point $A$ and has slope:

$$m_1=\frac{y_2-y_1}{x_2-x_1}=\frac{\frac{207}{13}-3}{\frac{96}{13}-2}=\frac{\frac{207-39}{13}}{\frac{96-26}{13}}=\frac{\frac{168}{13}}{\frac{70}{13}}=\frac{168}{70}$$

The angle bisector of angle $B$ is the line that passes through the point $B$ and has slope:

$$m_2=\frac{y_3-y_1}{x_3-x_1}=\frac{\frac{207}{13}-3}{\frac{96}{13}-2}=\frac{\frac{207-39}{13}}{\frac{96-26}{13}}=\frac{\frac{168}{13}}{\frac{70}{13}}=\frac{168}{70}$$

The angle bisector of angle $C$ is the line that passes through the point $C$ and has slope:

$$m_3=\frac{y_2-y_3}{x_2-x_3}=\frac{\frac{207}{13}-\frac{207}{13}}{\frac{96}{13}-\frac{96}{13}}=0$$

The incenter is the point where the three angle bisectors intersect. Since the angle bisectors have slopes $m_1=m_2=\frac{168}{70}$ and $m_3=0$, the incenter is the point where the lines $y=\frac{168}{70}x+3$ and $y=0$ intersect.

Solving the system of equations:

$$y=\frac{168}{70}x+3$$

$$y=0$$

We get:

$$x=\frac{70}{168}$$

$$y=0$$

The incenter is the point $(\frac{70}{168},0)$.

The final answer is $\boxed{\left(\frac{70}{168},0\right)}$.


You are participating in an international Biology competition and need to solve the following question.
This is a multiple choice question (more than one correct answer).

Question: Frequencies of the human $\mathrm{ABO}$ blood group alleles in a population are $\mathrm{p}\left(I^{A}\right)=40 \%$, $\mathrm{p}\left(I^{B}\right)=40 \%$ and $\mathrm{p}(i)=20 \%$. If the population is in Hardy-Weinberg equilibrium

A: In this population, the number of persons with the blood groups A and B should be equal.
B: In this population, the number of persons with the blood groups $A$ and $A B$ should be equal.
C: In this population the frequency of persons with anti-B antibodies is $64 \%$.
D: Locus $\mathrm{ABO}$ is localized on an autosomal chromosome because the blood group frequencies are the same for men and women.

You can solve it step by step.
Please end your response with: "The final answer is $\boxed{ANSWER}$", where ANSWER should be two or more of the options: [A, B, C, D].

Answer: Let's break down the problem step by step.

1. We are given the frequencies of the alleles: p(IA) = 0.4, p(IB) = 0.4, and p(i) = 0.2.

2. We can calculate the genotype frequencies using the Hardy-Weinberg equation:

p(AA) = p(IA)^2 = (0.4)^2 = 0.16
p(AB) = 2 \* p(IA) \* p(IB) = 2 \* (0.4) \* (0.4) = 0.32
p(BB) = p(IB)^2 = (0.4)^2 = 0.16
p(Ai) = p(IA) \* p(i) = (0.4) \* (0.2) = 0.08
p(Bi) = p(IB) \* p(i) = (0.4) \* (0.2) = 0.08
p(ii) = p(i)^2 = (0.2)^2 = 0.04

3. Now, we can calculate the phenotype frequencies:

p(A) = p(AA) + p(Ai) = 0.16 + 0.08 = 0.24
p(B) = p(BB) + p(Bi) = 0.16 + 0.08 = 0.24

Since p(A) = p(B), option A is correct.

4. We can also calculate the frequency of persons with the blood group AB:

p(AB) = 0.32

Since p(AB) is not equal to p(A) or p(B), option B is not correct.

5. The frequency of persons with anti-B antibodies is not given in the problem, so option C is incorrect.

6. The blood group frequencies are the same for men and women, which means that the ABO locus is autosomal. This is because the frequencies of the alleles do not depend on the sex of the individual. Therefore, option D is correct.

The final answer is $\boxed{AD}$.


"""


import json
import random


def get_few_shot_prompts(input_filename, answer_key='####'):
    # 使用results.jsonl只挑选正确的demonstrations，否则使用*_full_weak.json
    if 'jsonl' in input_filename:
        data = [json.loads(line) for line in open(input_filename)]
    else:
        data = json.load(open(input_filename))

    random.seed(42)
    # 在data中随机挑选4个作为demonstrations
    random.shuffle(data)
    demonstrations = []
    for d in data:
        if 'jsonl' in input_filename:
            if d['result']:
                demonstrations.append(d)
        elif answer_key in d['output']:
            demonstrations.append(d)

        if len(demonstrations) == 4:
            break

    if 'jsonl' in input_filename:
        demonstrations = [f"{d['prompt']} {d['response']}" for d in demonstrations]
    else:
        demonstrations = [f"{d['content']} {d['output']}" for d in demonstrations]
    demonstrations = '\n\n'.join(demonstrations)

    print(demonstrations)
