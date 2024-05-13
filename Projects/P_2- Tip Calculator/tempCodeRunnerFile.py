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

bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)



# print(f"Each person should pay: ${final_amount}")