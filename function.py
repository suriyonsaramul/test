from urllib.request import urlopen
import json
import random
import pandas as pd

with urlopen('https://opentdb.com/api.php?amount=50&category=18&difficulty=medium&type=multiple') as webpage:
  data = json.loads(webpage.read().decode())
  df = pd.DataFrame(data['results'])
  print(df.columns)
  
def preload_data():
  question = df['question'][0]
  correct = df['correct_answer'][0]
  incorrect = df['incorrect_answers'][0]

  parameters['question'].append(question)
  parameters['correct'].append(correct)

  all_answers = incorrect + [correct]
  random.shuffle(all_answers)

  parameters['answer1'].append(all_answers[0])
  parameters['answer2'].append(all_answers[1])
  parameters['answer3'].append(all_answers[2])
  parameters['answer4'].append(all_answers[3])

  # print(all_answers)

parameters = {
  "question": [],
  "answer1": [],
  "answer2": [],
  "answer3": [],
  "answer4": [],
  "correct": []
}

preload_data()