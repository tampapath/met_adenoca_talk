import splitfolders

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.

splitfolders.ratio('data', output="output", seed=1337, ratio=(.7, .2, .1)) # default values

# Split val/test with a fixed number of items e.g. 100 for each set.
# To only split into training and validation set, use a single number to `fixed`, i.e., `10`.

#split_folders.fixed('input_folder', output="output", seed=1337, fixed=(100, 100), oversample=False) # default values
