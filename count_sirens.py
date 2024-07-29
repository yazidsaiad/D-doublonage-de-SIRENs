import collections

def count_sirens(file_path):
    with open(file_path, 'r') as file:
        sirens = file.readlines()
    
    # Remove whitespace characters like `\n` at the end of each line
    sirens = [siren.strip() for siren in sirens]
    
    # Count the frequency of each SIREN
    counter = collections.Counter(sirens)
    
    # Calculate the required statistics
    count_at_least_twice = sum(1 for count in counter.values() if count >= 2)
    count_once = sum(1 for count in counter.values() if count == 1)
    
    return count_at_least_twice, count_once

if __name__ == "__main__":
    file_path = 'sirens_fxt_front_version.txt'
    count_at_least_twice, count_once = count_sirens(file_path)
    print(f'Number of SIRENs appearing at least twice: {count_at_least_twice}')
    print(f'Number of SIRENs appearing only once: {count_once}')

