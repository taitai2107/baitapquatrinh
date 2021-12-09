# In:
import numpy as np
scores = np.array([8, 6, 4, 3, 9, 4, 7, 4, 4, 9, 7, 3, 9, 4, 2, 3, 8, 5, 9, 6])
print("Q1 = : ", np.quantile(scores, 0.25))
print("Q2 = : ", np.quantile(scores, 0.5))
print("Q3 = : ", np.quantile(scores, 0.75))
# Out:
# Q1 = :  4.0
# Q2 = :  5.5
# Q3 = :  8.0