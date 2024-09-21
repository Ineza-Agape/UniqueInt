import os

class UniqueInt:
    @staticmethod
    def process_file(input_file_path, output_file_path):
        seen = set()  # To store unique integers in the range
        try:
            with open(input_file_path, 'r') as infile:
                for line in infile:
                    line = line.strip()  # Remove whitespaces
                    if line:  # Check if the line is not empty
                        try:
                            num = int(line)  # to convert the line to an integer
                            if -1023 <= num <= 1023:  # Check if the number is in the specified range
                                seen.add(num)  # Add the integer to the set
                            else:
                                print("Number {} is out of the specified range.".format(num))
                        except ValueError:
                            print("Skipping non-integer value: {}".format(line))
            
            sorted_numbers = sorted(seen)  # Sort the unique numbers in ascending order

            with open(output_file_path, 'w') as outfile:
                for num in sorted_numbers:
                    outfile.write("{}\n".format(num)) 
        except FileNotFoundError:
            print("Error: File {} not found.".format(input_file_path))

    @staticmethod
    def process_directory(input_dir, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for filename in os.listdir(input_dir):
            if filename.endswith(".txt"):  # Only process .txt files
                input_file_path = os.path.join(input_dir, filename)
                output_file_path = os.path.join(output_dir, "results_{}".format(filename))
                UniqueInt.process_file(input_file_path, output_file_path)
                print("Processed {} and saved results to {}".format(filename, output_file_path))

if __name__ == "__main__":
    input_dir = 'input'
    output_dir = 'results'

    UniqueInt.process_directory(input_dir, output_dir)

