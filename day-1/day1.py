from collections import Counter

def process_file(input_file: str):
    """Reads file and returns left and right lists."""
    with open(input_file, 'r') as file:
        left_list, right_list = [], []
        for line in file:
            # Convert list of strings into list of ints and unpack them
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def calculate_distance(left_list: str, right_list: str):
    """Calculate distance based on sorted list"""
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    # Pair up left_sorted and right_sorted to process them in distance calculation
    return sum(abs(left - right) for left, right in zip(left_sorted, right_sorted))

def calculate_similarity_score(left_list: str, right_list: str):
    """Calculate similarity score based on occurence of number in right list"""
    right_count = Counter(right_list)
    return sum((number * right_count.get(number, 0)) for number in left_list)
    # Prevent unnecessary variable initialisation, suggested straight return to prevent local variable referenced before assignment

def main(input_file):
    # Parse file to get left and right lists 
    left_list, right_list = process_file(input_file)

    # Process calculations
    distance = calculate_distance(left_list, right_list)
    similarity_score = calculate_similarity_score(left_list, right_list)

    # Output
    print(f"Distance: {distance}")
    print(f"Similarity score: {similarity_score}")

input_file = 'input.txt'
main(input_file)