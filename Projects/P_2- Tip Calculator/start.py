# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# welcome to the final project of today. And in this final project, we're going to be building a Tip Calculator.
# It's going to print "Welcome to the tip calculator!"
# and it's going to ask you for an input for how much the total bill came to.
# Let's say that we and a couple of friends went out for lunch and it came to $124.56.
# And then it'll ask you, what percentage tip would you like to give? 
# So let's say we want to give a 12% tip. So we enter 12 and hit Enter.
# And then finally it asks, how many people are splitting this bill?
# Let's say there's seven of us.And then hit Enter.
# Finally, it's going to tell us that each person should pay about $19.93.
# Notice how the final bill, even though after all of these calculations,
# it's probably got more numbers after the decimal point, we only want two decimal places of accuracy,
# so it should be rounded to two decimal places.
# The second thing to remember is that these are percentages, and in order to calculate a percentage of something,
# you can multiply a number by the percentage number divided by 100.
# Let me show you this in a little bit more detail, if you head over to, https://replit.com/@abhiupadh/tip-calculator-start,
# then you've got the starting file for this project.
#  And here, I just want to quickly show you how the maths works, because this project is not about testing your maths,
# it's about seeing how well you've understood the programming concepts.
# Let's say that we had a bill of $150, if we were to apply a 12% tip on top of that,
# then 12% is going to be equal to 12 divided by 100, which is equal to 0.12.
# Now the next step is we can multiply 150, the total bill, by 0.12 and this will give us what 12% of 150 is, which is 18.
# Now, we of course have to add the tip onto the final bill so it becomes 150 + 18.
# So $150 with 12% tip is equal to $168.
# Now, a shorthand way of doing all of this is simply multiplying 150 by 1.12.
# So the 1, is 150 and then it's 0.12 on top of that. So when we do this, it gives us pretty much the same number.
# Now, if during your testing and your coding, you come across some sort of number
# that looks a little bit strange because you think 150 multiplied by 1.12 should actually equal 168 precisely.
# So what are all of these extra numbers at the end? Now, the short answer is you don't have to worry about it.
# It's simply related to how Python processes these floating point numbers.
# If you're really interested and you want to read about this, then I'll link to this page in the Python documentation
# where they tell you why this is happening, but be warned, it's pretty dense and it's pretty heavy.
# But the final conclusion is it's just the way that Python is approximating this number.
# So you don't actually have to worry about this. Now, once we've gotten to 168,
# the next step is to split it between five people. So 168 divided by 5 is equal to 33.6.
# Now, what we want to show the user is we want to show them the amount that they have to pay
# with two decimal places of accuracy. So we want to say something like 33.60 if this is the case
# 'cause that's normally how we represent numbers when it comes to money.
# So what I want you to do is to also be able to round any of these numbers to two decimal places.
# If you have successfully created this program, then it should work exactly as this example version would,
# and you'll be able to see the formatting where it actually tells you each person should pay this particular dollar amount
# and it's rounded to two decimal places. And this is the amount after taking into consideration
# these three different inputs from the user.
# This is going to test everything that you've learned so far, including F-strings,
# including complex mathematical operations, including PEMDAS and calculating numbers
# and the order in which mathematical operations are run by a computer, as well as everything you've learned
# in the previous lessons and previous days as well.


# 12/100
# 150 * 0.12
# 150+18
# 150 * 1.12
# 168 /5 
