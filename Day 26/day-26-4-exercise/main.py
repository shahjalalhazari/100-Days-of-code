sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ex nisi, commodo vitae tristique eu, volutpat vel leo. Phasellus commodo hendrerit dolor ac varius. Etiam eget convallis lectus."
# Don't change code above 👆

# Write your code below:
result = {word:len(word) for word in sentence.split()}

print(result)
