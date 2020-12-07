from math import sqrt


def prepare_pattern(pettern):
    '''
    Create vectors based on values from loaded files
    '''
    value_pattern = list(pettern.replace('#', '1').replace('-', '0'))
    value = list(map(int, value_pattern))
    x = sum(value)
    root = sqrt(x)
    for index, number in enumerate(value):
        value[index] /= root
    return value


def load_data(filename):
    '''
    Load and prepare values stored in files
    '''
    with open(filename, newline='') as file:
        data = file.read().strip().split('\r\n')

    patterns = []
    letters = []
    number_of_patterns = int(data.pop(0))
    horizontal_resolution = int(data.pop(0))
    vertical_resolution = int(data.pop(0))
    for index in range(number_of_patterns):
        letter = data.pop(0)
        pattern = ''
        for row in range(horizontal_resolution):
            pattern += data.pop(0)
        patterns.append(prepare_pattern(pattern))
        letters.append(letter)
    return letters, patterns


def training_data(data):
    '''
    Preparing a training set
    '''
    patterns = data[1]
    weights = []
    layers = []

    for i in range(len(patterns)):
        for j in range(len(patterns[i])):
            weight = patterns[i][j]
            weights.append(weight)
        layers.append(weights)
        weights = []
    return layers


def compute(test, layer, layer_index):
    '''
    Calculate the degree of fit
    '''
    value = 0
    for i in range(len(layer[layer_index])):
        value += layer[layer_index][i] * test[i]
    return value


def madaline(layer, test_data):
    '''
    Comparison of test and training results
    '''
    outputs = []
    layer_index = 0
    for letter in test_data[0]:
        print(f'Letter {letter}')
        for test in test_data[1]:
            output = compute(test, layer, layer_index)
            print(output)
            outputs.append(output)
        found_result = max(outputs)
        found_letter = test_data[0][outputs.index(found_result)]
        layer_index += 1
        outputs = []
        print(f'Letter {found_letter} was recognized. Level of confidence = {round(found_result, 2)}')


# 4x4
train_data = load_data('train_4x4.txt')
test_data = load_data('test_4x4.txt')
layers = training_data(train_data)
madaline(layers, test_data)
# 16x16
train_data = load_data('train_16x16.txt')
test_data = load_data('test_16x16.txt')
layers = training_data(train_data)
madaline(layers, test_data)
