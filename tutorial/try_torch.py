import numpy as np
import torch

# A torch tensor represents a multi-dimensional array (element type
# will be float by default, here we are forcing float64, aka double).
# A vector is a special case (1D array). It can be initialized
# directly by specifying the values.
v = torch.tensor([0.11, 0.01, 0.98, 0.12, 0.98, 0.85, 0.03,
                  0.55, 0.49, 0.99, 0.02, 0.31, 0.55, 0.87,
                  0.63], dtype=torch.float64)


# Individual elements of the vector can be accessed through
# the square bracket operator with indices of the desired
# element  within thosesquare brackets.
# Index starts from zero, not one.
first_element = v[0]
third_element = v[2]
print("first element = {} third_element = {}".\
      format(first_element, third_element))


# Negative indices are to be counted from the end of array.
# E.g., -1 refers to the last array element.
#       -2 refers to the second from last element.
last_element = v[-1]
second_last_element = v[-2]
print("last_element = {} second_last_element = {}".\
      format(last_element, second_last_element))

# A range of elements can be sliced off a vector using the
# colon operator
second_to_fifth_elements = v[1:4]
print("second_to_fifth_elements: {}".format(second_to_fifth_elements))

# If nothing is specified on the left of the arrow, it implies beginning
# of array.
# If nothing is specified after the  colon it implies end of array.
first_to_third_elements = v[:2]
last_two_elements = v[-2:]
print("first_to_third_elements: {}  Last two elements: {}".\
      format(first_to_third_elements, last_two_elements))

# Size of the vector
num_elements_in_v = len(v)
print("Number of elements in v: {}".format(num_elements_in_v))

# A torch tensor can also be initialized from a numpy array.
u = np.array([0.11, 0.01, 0.98, 0.12, 0.98, 0.85, 0.03,
              0.55, 0.49, 0.99, 0.02, 0.31, 0.55, 0.87,
              0.63])
u = torch.from_numpy(u)

# One can add subtract tensors. Here we do diff = v1 - u.
# Since v1 and u contain the same values, their difference
# is all zeros.
diff = v.sub(u)
print(u)
print(v)
print(diff)

# torch tensors can be converted to numpy arrays too.
u1 = u.numpy()