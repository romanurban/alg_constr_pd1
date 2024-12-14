import subprocess

test_cases = ['sample0', 'sample1', 'sample2', 'sample3']

for test in test_cases:
    with open(f'{test}_expected.txt', 'r') as expected_file:
        expected_sum = expected_file.read().strip()

    with open(f'{test}.txt', 'r') as infile:
        result = subprocess.run(['python3', 'solution.py'], stdin=infile, capture_output=True, text=True)
    
    output = result.stdout.strip()
    output_sum = output.split()[1]
    
    if output_sum == expected_sum:
        print(f'{test}: Passed')
    else:
        print(f'{test}: Failed')
        print(f'Expected Sum: {expected_sum}')
        print(f'Actual Sum: {output_sum}')