from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the webdriver (you'll need to have the appropriate driver for your browser installed)
driver = webdriver.Edge()

# Navigate to the website where the multiple choice questions are
driver.get("https://achieve.hashtag-learning.co.uk/assess/question-page/")

# Find the element for the question
question_element = driver.find_element(By.ID, "question-1")

# Get the value of the data-correct attribute
correct_answer = question_element.get_attribute("data-correct")

# Print the correct answer
print("The correct answer is:", correct_answer)

# Close the webdriver

