#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
# Okay, so we've seen how the program is supposed to work and we're trying to create it from scratch
# by reverse engineering it, essentially.
# Now, the first thing our program should say is, "Welcome to the tip calculator."
# So that's easy enough. We just have to create a print statement. Perfect.
# And if you're creating a really enthusiastic tip calculator, you can replace the full stop with an exclamation mark.
# Okay, so let's run it step by step to make sure that we don't have any errors along the way.
# So the first step seems to be working.

print("Welcome to the tip calculator!")

# Now the next step is to ask the user for some inputs, and we want to know what was their total bill,
# what did it come to? So let's go ahead and create an input and ask them, "What was the total bill?"
# And then we will add a $ or whatever currency it is that you prefer to work with,
# because when we actually run this, you'll see that the input will go straight after the end of that string,
# so at the dollar sign. So now we can enter a dollar amount like this, but it's not really saved anywhere.

# input("What was the total bill? $")

# This data just disappears because we haven't stored it inside a variable.
# So let's go ahead and do that. Let's call this variable bill and we'll set it
# to equal whatever the user typed into this input. Now remember that this bill
# is going to have a data type of a string, right? So if I go ahead and hit run,
# and let's just type some numbers in here, you'll see that the data type of the bill is, as we said, a string.
# In order to be able to do maths, you might remember we have to change this into a number format, so a float or an int.
# Now in this case, because the bill is likely to have numbers after the decimal place,
# it's probably better that we turn it into a float so that we get the most accurate result possible.


bill = float(input("What was the total bill? $"))

# Now that we're done with the bill, the next question the tip calculator should ask is,
# what percentage tip would you like to give? 10, 12, or 15? Or you can of course switch this up
# depending on how much tip you normally give. So the next line is going to be another input.

# input("How much tip would you like to give? 10, 12, or 15? ")

# Here, I'm asking the user, "How much tip would you like to give?"
# and giving them some examples. And notice how in my examples,
# I don't actually have the percentage sign here because I don't really want them
# to type the percent sign into this input,  because if they do, when they say 12%,
# this is going to be really hard for me to turn the 12% into an actual number.
# So you could, in your input message, say something like, "How much tip would you like to give,
# 10, 12, or 15? Please don't add any percentage signs, just add the number," or something like that.
# But, again, once we've done this, it's not stored anywhere unless we add it into a variable.
# Now, we've got a bill that stores the total bill as a float, and we've got a tip,
# which is going to be a whole number 10, 12, or 15, right? 
# So depending on what you think is best, you can either turn this into a float,
# or in my case, I'm probably going to convert it into an integer. 



tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# So now we're onto the final step, which is how many people to split the bill between?
# So let's go ahead and create a variable called people, and I'm going to add an int() wrapper around this input
# so that even in the very beginning, we know that we have to convert the number of people
# into a whole number because I've never had a meal with 3.5 people before.
# So the input is going to be, "How many people to split the bill?" 
# And at this point, they should enter the number of people which will turn into an integer
# stored inside this variable called people. So now that we've got all the data collected from the user,
# we're finally ready to do some maths.

people = int(input("How many people to split the bill?"))

# And we said that the way to work out the tip is by multiplying it by 1. (one point) and then the number after the decimal point
# is whatever percentage they decided to give. So it would be 1.1 if it was 10% and 1.15 if it was 15%.
# Let's go ahead and calculate the bill_with_tip.
# So remember how we said that before the tip percentage is equal to the whole number 10, 12, or 15 divided by 100,
# which turns it into 0.1, 0.12, or 0.15, and then once this calculation is done,
# we can multiply it by the bill. And then finally, we add that to the original bill.
# So let's go ahead and print this and just check to see that it looks sensible.
# So bill_with_tip is what we're going to print, and let's put some easy numbers in there.
# Let's say that the bill was $100 and the tip was 10%, so then the 10% of $100 is $10.
# So the bill_with_tip, that's what's going to be printed next So the bill_with_tip,should be 110.
# So we can type anything in here because we're not using it,
# and you can see that this calculation, bill_with_tip, is 110, which is what we want.
# Now, there's a lot of other ways that you can express this, for example, you could say,
# bill * (1 + tip / 100). So this would actually give you the same result as well,
# but remember what we said previously about how Python is a little bit weird with floating point numbers,
# but essentially, this is still giving us the same result, which is 110.
# So you can choose whichever way you find most intuitive.

# bill_with_tip = tip / 100 * bill + bill
# bill_with_tip = bill * (1 + tip / 100)
# print(bill_with_tip)

# And if you want, you can even split this up into several steps, right?
# We could say that tip_as_percent = tip / 100.

tip_as_percent = tip / 100

# And then we can multiply the bill by the tip_as_percent to get the total_tip_amount.

total_tip_amount = bill * tip_as_percent

# And then finally, we can get the total_bill by adding the bill to the total_tip_amount.
# Feel free to do this whichever way makes sense to you, but I'm going to leave it with as many steps as possible
# so that you can actually work through the logic if you got stuck on these maths.

total_bill = bill + total_tip_amount

# Now the next thing we need to do is to divide the total_bill by the number of people.
# So if we had five people, then we would divide it five ways, right?
# So let's call this bill_per_person, which is going to be equal to the total_bill
# divided by the number of people. 

bill_per_person = total_bill / people

# Now at this stage, this bill_per_person is a floating point number, so it could have many, many digits after the decimal point.
#  If we want to round this to two decimal places, then you might remember from some of the lessons today,
# we have access to a function called round.  And here, we can add the number that we want to round, which is the bill_per_person,
# and then after a comma, we can specify how precise, how many numbers or how many decimal places
# do we want to round this bill to. And in our case, it's two decimal places.
# So now, this is the final amount,

# round(bill_per_person, 2)

# which I'll call final_amount, which is the bill_per_person rounded to two decimal places.

# final_amount = round(bill_per_person, 2) #initial
final_amount = "{:.2f}".format(bill_per_person)  #final


# And we can now finally print this to the user and say, "Each person should pay..."
# And remember, you can either use string concatenation, which will require you to convert this number
# into a string again, or use the trick that we learned in the previous lessons
# where we can create an F-string by adding f in front of the string and then using some curly braces
# to insert the final amount right here. And we can write the {final_amount} dollars,
# or we can put a $ in front and maybe a colon on here.


print(f"Each person should pay: ${final_amount}")

# And now if we clear our console and run our code, then you'll see it work.
# So, "Welcome to the tip calculator! What was the total bill?"
# Let's make up some random number.(153.45) "What percentage tip?"
# Let's say we're going to give 15, and then we're splitting it between five people.
# And it calculates everything doing all of that maths. And finally, it rounds it to two decimal places
# giving us the final amount each person should pay.
# But what if we test out with the initial numbers?
# Let's hit Run and let's try to put in $150 as the total_bill
# and then we're going to give a 12% tip and we're going to split it between five people.
# Notice that it's telling us that each person should pay $33.6,
# but normally, we are used to seeing that rounded to two decimal places,
# but we have that round function here already so why is it not doing its job?
# Well, if you think about it, the result of this calculation is just 33.6.
# There's nothing after the 6, but we want it to display a zero.
# And this is a formatting problem rather than a mathematical rounding problem.
# So what do we do?
# Well, we go to our good friend Google whenever we're stuck, and we're going to search for 
# how to round number to 2 decimal places in Python.
# And if we take a look at the first Stack Overflow question, you can see that this person
# had pretty much the same problem that we had. And if we are scrolling down, you can see that the solution
# is to use some sort of formatting. And we can try out each of these examples one by one in code to see how they work
# and we can also take a look at the documentation that they link to.
# So the actual way that we do this is by using a colon and then dot, and then we specify that after the dot,
# we want two decimal points in our float, ( {:.2f} ) and we use the format function to do this.
# So instead of using round, we can create this final amount variable by creating a string using that format "{:.2f}",
# and then we can use the format() function to pass in that bill_per_person.
# And now, when we run this again using the same inputs, we now get a .60 at the very end.
# And this has basically turned this bill_per_person, which is a float, into a string,
# and that string is abiding by this particular format, which is the two decimal places.
# How did you get on with this project? Did you manage to get it in one go without having to look at the solution?
# If you got stuck at any point or if your code didn't work as you expect it to,
# this is a time to go back to it, fix it, and make sure that you've understood everything
# that's been covered through this exercise.

# final_amount = "{:.2f}".format(bill_per_person)