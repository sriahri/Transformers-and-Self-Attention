# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
from tqdm import tqdm

import utils

evaluation_path = "birth_dev.tsv"
length = len(open(evaluation_path).readlines())
predictions = ["London"] * length
total, correct = utils.evaluate_places(evaluation_path, predictions)
if total > 0:
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
else:
    print('No targets provided!')